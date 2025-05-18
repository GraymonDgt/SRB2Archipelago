from __future__ import annotations

import collections
import copy
import logging
import asyncio
import urllib.parse
import colorama
import typing
import time
import functools
import warnings
import sys
import ModuleUpdate

ModuleUpdate.update()
from tkinter import filedialog
import websockets
import Utils
import struct
import math

if __name__ == "__main__":
    Utils.init_logging("TextClient", exception_logger="Client")

from MultiServer import CommandProcessor
from NetUtils import (Endpoint, decode, NetworkItem, encode, JSONtoTextParser, ClientStatus, Permission, NetworkSlot,
                      RawJSONtoTextParser, add_json_text, add_json_location, add_json_item, JSONTypes,
                      SlotType)  # HintStatus
from Utils import Version, stream_input, async_start, ByValue
from worlds import network_data_package, AutoWorldRegister
import os
import ssl
import enum


class HintStatus(ByValue, enum.IntEnum):
    HINT_UNSPECIFIED = 0
    HINT_NO_PRIORITY = 10
    HINT_AVOID = 20
    HINT_PRIORITY = 30
    HINT_FOUND = 40


if typing.TYPE_CHECKING:
    import kvui
    import argparse

logger = logging.getLogger("Client")

# without terminal, we have to use gui mode
gui_enabled = not sys.stdout or "--nogui" not in sys.argv


@Utils.cache_argsless
def get_ssl_context():
    import certifi
    return ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=certifi.where())


class ClientCommandProcessor(CommandProcessor):
    """
    The Command Processor will parse every method of the class that starts with "_cmd_" as a command to be called
    when parsing user input, i.e. _cmd_exit will be called when the user sends the command "/exit".

    The decorator @mark_raw can be imported from MultiServer and tells the parser to only split on the first
    space after the command i.e. "/exit one two three" will be passed in as method("one two three") with mark_raw
    and method("one", "two", "three") without.

    In addition all docstrings for command methods will be displayed to the user on launch and when using "/help"
    """

    def __init__(self, ctx: CommonContext):
        self.ctx = ctx

    def output(self, text: str):
        """Helper function to abstract logging to the CommonClient UI"""
        logger.info(text)

    def _cmd_exit(self) -> bool:
        """Close connections and client"""
        self.ctx.exit_event.set()
        return True

    def _cmd_connect(self, address: str = "") -> bool:
        """Connect to a MultiWorld Server"""
        if address:
            self.ctx.server_address = None
            self.ctx.username = None
            self.ctx.password = None
        elif not self.ctx.server_address:
            self.output("Please specify an address.")
            return False
        async_start(self.ctx.connect(address if address else None), name="connecting")
        return True

    def _cmd_disconnect(self) -> bool:
        """Disconnect from a MultiWorld Server"""
        async_start(self.ctx.disconnect(), name="disconnecting")
        return True

    def _cmd_received(self) -> bool:
        """List all received items"""
        item: NetworkItem
        self.output(f'{len(self.ctx.items_received)} received items, sorted by time:')
        for index, item in enumerate(self.ctx.items_received, 1):
            parts = []
            add_json_item(parts, item.item, self.ctx.slot, item.flags)
            add_json_text(parts, " from ")
            add_json_location(parts, item.location, item.player)
            add_json_text(parts, " by ")
            add_json_text(parts, item.player, type=JSONTypes.player_id)
            self.ctx.on_print_json({"data": parts, "cmd": "PrintJSON"})
        return True

    def _cmd_missing(self, filter_text="") -> bool:
        """List all missing location checks, from your local game state.
        Can be given text, which will be used as filter."""
        if not self.ctx.game:
            self.output("No game set, cannot determine missing checks.")
            return False
        count = 0
        checked_count = 0
        for location, location_id in AutoWorldRegister.world_types[self.ctx.game].location_name_to_id.items():
            if filter_text and filter_text not in location:
                continue
            if location_id < 0:
                continue
            if location_id not in self.ctx.locations_checked:
                if location_id in self.ctx.missing_locations:
                    self.output('Missing: ' + location)
                    count += 1
                elif location_id in self.ctx.checked_locations:
                    self.output('Checked: ' + location)
                    count += 1
                    checked_count += 1

        if count:
            self.output(
                f"Found {count} missing location checks{f'. {checked_count} location checks previously visited.' if checked_count else ''}")
        else:
            self.output("No missing location checks found.")
        return True

    def _cmd_items(self):
        """List all item names for the currently running game."""
        if not self.ctx.game:
            self.output("No game set, cannot determine existing items.")
            return False
        self.output(f"Item Names for {self.ctx.game}")
        for item_name in AutoWorldRegister.world_types[self.ctx.game].item_name_to_id:
            self.output(item_name)

    def _cmd_item_groups(self):
        """List all item group names for the currently running game."""
        if not self.ctx.game:
            self.output("No game set, cannot determine existing item groups.")
            return False
        self.output(f"Item Group Names for {self.ctx.game}")
        for group_name in AutoWorldRegister.world_types[self.ctx.game].item_name_groups:
            self.output(group_name)

    def _cmd_locations(self):
        """List all location names for the currently running game."""
        if not self.ctx.game:
            self.output("No game set, cannot determine existing locations.")
            return False
        self.output(f"Location Names for {self.ctx.game}")
        for location_name in AutoWorldRegister.world_types[self.ctx.game].location_name_to_id:
            self.output(location_name)

    def _cmd_location_groups(self):
        """List all location group names for the currently running game."""
        if not self.ctx.game:
            self.output("No game set, cannot determine existing location groups.")
            return False
        self.output(f"Location Group Names for {self.ctx.game}")
        for group_name in AutoWorldRegister.world_types[self.ctx.game].location_name_groups:
            self.output(group_name)

    def _cmd_ready(self):
        """Send ready status to server."""
        self.ctx.ready = not self.ctx.ready
        if self.ctx.ready:
            state = ClientStatus.CLIENT_READY
            self.output("Readied up.")
        else:
            state = ClientStatus.CLIENT_CONNECTED
            self.output("Unreadied.")
        async_start(self.ctx.send_msgs([{"cmd": "StatusUpdate", "status": state}]), name="send StatusUpdate")

    def default(self, raw: str):
        """The default message parser to be used when parsing any messages that do not match a command"""
        raw = self.ctx.on_user_say(raw)
        if raw:
            async_start(self.ctx.send_msgs([{"cmd": "Say", "text": raw}]), name="send Say")


class CommonContext:
    # The following attributes are used to Connect and should be adjusted as needed in subclasses
    tags: typing.Set[str] = {"AP"}
    game: typing.Optional[str] = None
    items_handling: typing.Optional[int] = None
    items_handling: typing.Optional[int] = None
    want_slot_data: bool = True  # should slot_data be retrieved via Connect

    class NameLookupDict:
        """A specialized dict, with helper methods, for id -> name item/location data package lookups by game."""

        def __init__(self, ctx: CommonContext, lookup_type: typing.Literal["item", "location"]):
            self.ctx: CommonContext = ctx
            self.lookup_type: typing.Literal["item", "location"] = lookup_type
            self._unknown_item: typing.Callable[[int], str] = lambda key: f"Unknown {lookup_type} (ID: {key})"
            self._archipelago_lookup: typing.Dict[int, str] = {}
            self._flat_store: typing.Dict[int, str] = Utils.KeyedDefaultDict(self._unknown_item)
            self._game_store: typing.Dict[str, typing.ChainMap[int, str]] = collections.defaultdict(
                lambda: collections.ChainMap(self._archipelago_lookup, Utils.KeyedDefaultDict(self._unknown_item)))
            self.warned: bool = False

        # noinspection PyTypeChecker
        def __getitem__(self, key: str) -> typing.Mapping[int, str]:
            # TODO: In a future version (0.6.0?) this should be simplified by removing implicit id lookups support.
            if isinstance(key, int):
                if not self.warned:
                    # Use warnings instead of logger to avoid deprecation message from appearing on user side.
                    self.warned = True
                    warnings.warn(f"Implicit name lookup by id only is deprecated and only supported to maintain "
                                  f"backwards compatibility for now. If multiple games share the same id for a "
                                  f"{self.lookup_type}, name could be incorrect. Please use "
                                  f"`{self.lookup_type}_names.lookup_in_game()` or "
                                  f"`{self.lookup_type}_names.lookup_in_slot()` instead.")
                return self._flat_store[key]  # type: ignore

            return self._game_store[key]

        def __len__(self) -> int:
            return len(self._game_store)

        def __iter__(self) -> typing.Iterator[str]:
            return iter(self._game_store)

        def __repr__(self) -> str:
            return self._game_store.__repr__()

        def lookup_in_game(self, code: int, game_name: typing.Optional[str] = None) -> str:
            """Returns the name for an item/location id in the context of a specific game or own game if `game` is
            omitted.
            """
            if game_name is None:
                game_name = self.ctx.game
                assert game_name is not None, f"Attempted to lookup {self.lookup_type} with no game name available."

            return self._game_store[game_name][code]

        def lookup_in_slot(self, code: int, slot: typing.Optional[int] = None) -> str:
            """Returns the name for an item/location id in the context of a specific slot or own slot if `slot` is
            omitted.

            Use of `lookup_in_slot` should not be used when not connected to a server. If looking in own game, set
            `ctx.game` and use `lookup_in_game` method instead.
            """
            if slot is None:
                slot = self.ctx.slot
                assert slot is not None, f"Attempted to lookup {self.lookup_type} with no slot info available."

            return self.lookup_in_game(code, self.ctx.slot_info[slot].game)

        def update_game(self, game: str, name_to_id_lookup_table: typing.Dict[str, int]) -> None:
            """Overrides existing lookup tables for a particular game."""
            id_to_name_lookup_table = Utils.KeyedDefaultDict(self._unknown_item)
            id_to_name_lookup_table.update({code: name for name, code in name_to_id_lookup_table.items()})
            self._game_store[game] = collections.ChainMap(self._archipelago_lookup, id_to_name_lookup_table)
            self._flat_store.update(id_to_name_lookup_table)  # Only needed for legacy lookup method.
            if game == "Archipelago":
                # Keep track of the Archipelago data package separately so if it gets updated in a custom datapackage,
                # it updates in all chain maps automatically.
                self._archipelago_lookup.clear()
                self._archipelago_lookup.update(id_to_name_lookup_table)

    # defaults
    starting_reconnect_delay: int = 5
    current_reconnect_delay: int = starting_reconnect_delay
    command_processor: typing.Type[CommandProcessor] = ClientCommandProcessor
    ui: typing.Optional["kvui.GameManager"] = None
    ui_task: typing.Optional["asyncio.Task[None]"] = None
    input_task: typing.Optional["asyncio.Task[None]"] = None
    keep_alive_task: typing.Optional["asyncio.Task[None]"] = None
    server_task: typing.Optional["asyncio.Task[None]"] = None
    autoreconnect_task: typing.Optional["asyncio.Task[None]"] = None
    disconnected_intentionally: bool = False
    server: typing.Optional[Endpoint] = None
    server_version: Version = Version(0, 0, 0)
    generator_version: Version = Version(0, 0, 0)
    current_energy_link_value: typing.Optional[int] = None  # to display in UI, gets set by server
    max_size: int = 16 * 1024 * 1024  # 16 MB of max incoming packet size

    last_death_link: float = time.time()  # last send/received death link on AP layer
    death_link: float = time.time()
    death_link_lockout: float = time.time()
    activate_death: bool = False
    goal_type: int = None
    bcz_emblems: int = 0
    # remaining type info
    slot_info: typing.Dict[int, NetworkSlot]
    server_address: typing.Optional[str]
    password: typing.Optional[str]
    hint_cost: typing.Optional[int]
    hint_points: typing.Optional[int]
    player_names: typing.Dict[int, str]

    finished_game: bool
    ready: bool
    team: typing.Optional[int]
    slot: typing.Optional[int]
    auth: typing.Optional[str]
    seed_name: typing.Optional[str]

    # locations
    locations_checked: typing.Set[int]  # local state
    locations_scouted: typing.Set[int]
    items_received: typing.List[NetworkItem]
    missing_locations: typing.Set[int]  # server state
    checked_locations: typing.Set[int]  # server state
    server_locations: typing.Set[int]  # all locations the server knows of, missing_location | checked_locations
    locations_info: typing.Dict[int, NetworkItem]

    # data storage
    stored_data: typing.Dict[str, typing.Any]
    stored_data_notification_keys: typing.Set[str]

    # internals
    # current message box through kvui
    _messagebox: typing.Optional["kvui.MessageBox"] = None
    # message box reporting a loss of connection
    _messagebox_connection_loss: typing.Optional["kvui.MessageBox"] = None

    def __init__(self, server_address: typing.Optional[str] = None, password: typing.Optional[str] = None) -> None:
        # server state
        self.server_address = server_address
        self.username = None
        self.password = password
        self.hint_cost = None
        self.slot_info = {}
        self.permissions = {
            "release": "disabled",
            "collect": "disabled",
            "remaining": "disabled",
        }

        # own state
        self.finished_game = False
        self.ready = False
        self.team = None
        self.slot = None
        self.auth = None
        self.seed_name = None

        self.locations_checked = set()  # local state
        self.locations_scouted = set()
        self.items_received = []
        self.missing_locations = set()  # server state
        self.checked_locations = set()  # server state
        self.server_locations = set()  # all locations the server knows of, missing_location | checked_locations
        self.locations_info = {}

        self.stored_data = {}
        self.stored_data_notification_keys = set()

        self.input_queue = asyncio.Queue()
        self.input_requests = 0

        # game state
        self.player_names = {0: "Archipelago"}
        self.exit_event = asyncio.Event()
        self.watcher_event = asyncio.Event()

        self.item_names = self.NameLookupDict(self, "item")
        self.location_names = self.NameLookupDict(self, "location")
        self.versions = {}
        self.checksums = {}
        self.texttransfer = []


        self.jsontotextparser = JSONtoTextParser(self)
        self.rawjsontotextparser = RawJSONtoTextParser(self)
        self.update_data_package(network_data_package)

        # execution
        self.keep_alive_task = asyncio.create_task(keep_alive(self), name="Bouncy")

    @property
    def suggested_address(self) -> str:
        if self.server_address:
            return self.server_address
        return Utils.persistent_load().get("client", {}).get("last_server_address", "")

    @functools.cached_property
    def raw_text_parser(self) -> RawJSONtoTextParser:
        return RawJSONtoTextParser(self)

    @property
    def total_locations(self) -> typing.Optional[int]:
        """Will return None until connected."""
        if self.checked_locations or self.missing_locations:
            return len(self.checked_locations | self.missing_locations)

    async def connection_closed(self):
        if self.server and self.server.socket is not None:
            await self.server.socket.close()
        self.reset_server_state()

    def reset_server_state(self):
        self.auth = None
        self.slot = None
        self.team = None
        self.items_received = []
        self.locations_info = {}
        self.server_version = Version(0, 0, 0)
        self.generator_version = Version(0, 0, 0)
        self.server = None
        self.server_task = None
        self.hint_cost = None
        self.permissions = {
            "release": "disabled",
            "collect": "disabled",
            "remaining": "disabled",
        }

    async def disconnect(self, allow_autoreconnect: bool = False):
        if not allow_autoreconnect:
            self.disconnected_intentionally = True
            if self.cancel_autoreconnect():
                logger.info("Cancelled auto-reconnect.")
        # if self.server and not self.server.socket.closed:
        #    await self.server.socket.close()
        if self.server_task is not None:
            await self.server_task
        # self.ui.update_hints()

    async def send_msgs(self, msgs: typing.List[typing.Any]) -> None:
        """ `msgs` JSON serializable """
        # if not self.server or not self.server.socket.open or self.server.socket.closed:
        #    return
        await self.server.socket.send(encode(msgs))

    def consume_players_package(self, package: typing.List[tuple]):
        self.player_names = {slot: name for team, slot, name, orig_name in package if self.team == team}
        self.player_names[0] = "Archipelago"

    def event_invalid_slot(self):
        raise Exception('Invalid Slot; please verify that you have connected to the correct world.')

    def event_invalid_game(self):
        raise Exception('Invalid Game; please verify that you connected with the right game to the correct world.')

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            logger.info('Enter the password required to join this game:')
            self.password = await self.console_input()
            return self.password

    async def get_username(self):
        if not self.auth:
            self.auth = self.username
            if not self.auth:
                logger.info('Enter slot name:')
                self.auth = await self.console_input()

    async def send_connect(self, **kwargs: typing.Any) -> None:
        """
        Send a `Connect` packet to log in to the server,
        additional keyword args can override any value in the connection packet
        """
        payload = {
            'cmd': 'Connect',
            'password': self.password, 'name': self.auth, 'version': Utils.version_tuple,
            'tags': self.tags, 'items_handling': self.items_handling,
            'uuid': Utils.get_unique_identifier(), 'game': self.game, "slot_data": self.want_slot_data,
        }

        if kwargs:
            payload.update(kwargs)
        await self.send_msgs([payload])
        await self.send_msgs([{"cmd": "Get", "keys": ["_read_race_mode"]}])

    async def check_locations(self, locations: typing.Collection[int]) -> set[int]:
        """Send new location checks to the server. Returns the set of actually new locations that were sent."""
        locations = set(locations) & self.missing_locations
        if locations:
            await self.send_msgs([{"cmd": 'LocationChecks', "locations": tuple(locations)}])
        return locations

    async def console_input(self) -> str:
        if self.ui:
            self.ui.focus_textinput()
        self.input_requests += 1
        return await self.input_queue.get()

    async def connect(self, address: typing.Optional[str] = None) -> None:
        """ disconnect any previous connection, and open new connection to the server """
        await self.disconnect()
        self.server_task = asyncio.create_task(server_loop(self, address), name="server loop")

    def cancel_autoreconnect(self) -> bool:
        if self.autoreconnect_task:
            self.autoreconnect_task.cancel()
            self.autoreconnect_task = None
            return True
        return False

    def slot_concerns_self(self, slot) -> bool:
        """Helper function to abstract player groups, should be used instead of checking slot == self.slot directly."""
        if slot == self.slot:
            return True
        if slot in self.slot_info:
            return self.slot in self.slot_info[slot].group_members
        return False

    def is_echoed_chat(self, print_json_packet: dict) -> bool:
        """Helper function for filtering out messages sent by self."""
        return print_json_packet.get("type", "") == "Chat" \
            and print_json_packet.get("team", None) == self.team \
            and print_json_packet.get("slot", None) == self.slot

    def is_uninteresting_item_send(self, print_json_packet: dict) -> bool:
        """Helper function for filtering out ItemSend prints that do not concern the local player."""
        return print_json_packet.get("type", "") == "ItemSend" \
            and not self.slot_concerns_self(print_json_packet["receiving"]) \
            and not self.slot_concerns_self(print_json_packet["item"].player)

    def on_print(self, args: dict):
        logger.info(args["text"])

    def on_print_json(self, args: dict):
        if self.ui:
            # send copy to UI
            self.ui.print_json(copy.deepcopy(args["data"]))
            print(args["data"])
            self.texttransfer.append(copy.deepcopy(args["data"]))
        logging.getLogger("FileLog").info(self.rawjsontotextparser(copy.deepcopy(args["data"])),
                                          extra={"NoStream": True})
        logging.getLogger("StreamLog").info(self.jsontotextparser(copy.deepcopy(args["data"])),
                                            extra={"NoFile": True})

    def on_package(self, cmd: str, args: dict):
        """For custom package handling in subclasses."""
        pass

    def on_user_say(self, text: str) -> typing.Optional[str]:
        """Gets called before sending a Say to the server from the user.
        Returned text is sent, or sending is aborted if None is returned."""
        return text

    def on_ui_command(self, text: str) -> None:
        """Gets called by kivy when the user executes a command starting with `/` or `!`.
        The command processor is still called; this is just intended for command echoing."""
        self.ui.print_json([{"text": text, "type": "color", "color": "orange"}])
        print([{"text": text, "type": "color", "color": "orange"}])

    def update_permissions(self, permissions: typing.Dict[str, int]):
        """Internal method to parse and save server permissions from RoomInfo"""
        for permission_name, permission_flag in permissions.items():
            try:
                flag = Permission(permission_flag)
                logger.info(f"{permission_name.capitalize()} permission: {flag.name}")
                self.permissions[permission_name] = flag.name
            except Exception as e:  # safeguard against permissions that may be implemented in the future
                logger.exception(e)

    async def shutdown(self):
        self.server_address = ""
        self.username = None
        self.password = None
        self.cancel_autoreconnect()
        if self.server and not self.server.socket.closed:
            await self.server.socket.close()
        if self.server_task:
            await self.server_task

        while self.input_requests > 0:
            self.input_queue.put_nowait(None)
            self.input_requests -= 1
        self.keep_alive_task.cancel()
        if self.ui_task:
            await self.ui_task
        if self.input_task:
            self.input_task.cancel()

    # Hints
    def update_hint(self, location: int, finding_player: int, status: typing.Optional[HintStatus]) -> None:
        msg = {"cmd": "UpdateHint", "location": location, "player": finding_player}
        if status is not None:
            msg["status"] = status
        async_start(self.send_msgs([msg]), name="update_hint")

    # DataPackage
    async def prepare_data_package(self, relevant_games: typing.Set[str],
                                   remote_date_package_versions: typing.Dict[str, int],
                                   remote_data_package_checksums: typing.Dict[str, str]):
        """Validate that all data is present for the current multiworld.
        Download, assimilate and cache missing data from the server."""
        # by documentation any game can use Archipelago locations/items -> always relevant
        relevant_games.add("Archipelago")

        needed_updates: typing.Set[str] = set()
        for game in relevant_games:
            if game not in remote_date_package_versions and game not in remote_data_package_checksums:
                continue

            remote_version: int = remote_date_package_versions.get(game, 0)
            remote_checksum: typing.Optional[str] = remote_data_package_checksums.get(game)

            if remote_version == 0 and not remote_checksum:  # custom data package and no checksum for this game
                needed_updates.add(game)
                continue

            cached_version: int = self.versions.get(game, 0)
            cached_checksum: typing.Optional[str] = self.checksums.get(game)
            # no action required if cached version is new enough
            if (not remote_checksum and (remote_version > cached_version or remote_version == 0)) \
                    or remote_checksum != cached_checksum:
                local_version: int = network_data_package["games"].get(game, {}).get("version", 0)
                local_checksum: typing.Optional[str] = network_data_package["games"].get(game, {}).get("checksum")
                if ((remote_checksum or remote_version <= local_version and remote_version != 0)
                        and remote_checksum == local_checksum):
                    self.update_game(network_data_package["games"][game], game)
                else:
                    cached_game = Utils.load_data_package_for_checksum(game, remote_checksum)
                    cache_version: int = cached_game.get("version", 0)
                    cache_checksum: typing.Optional[str] = cached_game.get("checksum")
                    # download remote version if cache is not new enough
                    if (not remote_checksum and (remote_version > cache_version or remote_version == 0)) \
                            or remote_checksum != cache_checksum:
                        needed_updates.add(game)
                    else:
                        self.update_game(cached_game, game)
        if needed_updates:
            await self.send_msgs([{"cmd": "GetDataPackage", "games": [game_name]} for game_name in needed_updates])

    def update_game(self, game_package: dict, game: str):
        self.item_names.update_game(game, game_package["item_name_to_id"])
        self.location_names.update_game(game, game_package["location_name_to_id"])
        self.versions[game] = game_package.get("version", 0)
        self.checksums[game] = game_package.get("checksum")

    def update_data_package(self, data_package: dict):
        for game, game_data in data_package["games"].items():
            self.update_game(game_data, game)

    def consume_network_data_package(self, data_package: dict):
        self.update_data_package(data_package)
        current_cache = Utils.persistent_load().get("datapackage", {}).get("games", {})
        current_cache.update(data_package["games"])
        Utils.persistent_store("datapackage", "games", current_cache)
        logger.info(f"Got new ID/Name DataPackage for {', '.join(data_package['games'])}")
        for game, game_data in data_package["games"].items():
            Utils.store_data_package_for_checksum(game, game_data)

    # data storage

    def set_notify(self, *keys: str) -> None:
        """Subscribe to be notified of changes to selected data storage keys.

        The values can be accessed via the "stored_data" attribute of this context, which is a dictionary mapping the
        names of the data storage keys to the latest values received from the server.
        """
        if new_keys := (set(keys) - self.stored_data_notification_keys):
            self.stored_data_notification_keys.update(new_keys)
            async_start(self.send_msgs([{"cmd": "Get",
                                         "keys": list(new_keys)},
                                        {"cmd": "SetNotify",
                                         "keys": list(new_keys)}]))

    # DeathLink hooks

    def on_deathlink(self, data: typing.Dict[str, typing.Any]) -> None:
        """Gets dispatched when a new DeathLink is triggered by another linked player."""
        self.last_death_link = max(data["time"], self.last_death_link)
        text = data.get("cause", "")
        self.activate_death = True
        if text:
            logger.info(f"DeathLink: {text}")
        else:
            logger.info(f"DeathLink: Received from {data['source']}")

    async def send_death(self, death_text: str = ""):
        """Helper function to send a deathlink using death_text as the unique death cause string."""
        if self.server and self.server.socket:
            logger.info("DeathLink: Sending death to your friends...")
            self.last_death_link = time.time()
            await self.send_msgs([{
                "cmd": "Bounce", "tags": ["DeathLink"],
                "data": {
                    "time": self.last_death_link,
                    "source": self.player_names[self.slot],
                    "cause": death_text
                }
            }])

    async def update_death_link(self, death_link: bool):
        """Helper function to set Death Link connection tag on/off and update the connection if already connected."""
        old_tags = self.tags.copy()
        if death_link:
            self.tags.add("DeathLink")
        else:
            self.tags -= {"DeathLink"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])

    def gui_error(self, title: str, text: typing.Union[Exception, str]) -> typing.Optional["kvui.MessageBox"]:
        """Displays an error messagebox in the loaded Kivy UI. Override if using a different UI framework"""
        if not self.ui:
            return None
        title = title or "Error"
        from kvui import MessageBox
        if self._messagebox:
            self._messagebox.dismiss()
        # make "Multiple exceptions" look nice
        text = str(text).replace('[Errno', '\n[Errno').strip()
        # split long messages into title and text
        parts = title.split('. ', 1)
        if len(parts) == 1:
            parts = title.split(', ', 1)
        if len(parts) > 1:
            text = parts[1] + '\n\n' + text
            title = parts[0]
        # display error
        self._messagebox = MessageBox(title, text, error=True)
        self._messagebox.open()
        return self._messagebox

    def handle_connection_loss(self, msg: str) -> None:
        """Helper for logging and displaying a loss of connection. Must be called from an except block."""
        exc_info = sys.exc_info()
        logger.exception(msg, exc_info=exc_info, extra={'compact_gui': True})
        self._messagebox_connection_loss = self.gui_error(msg, exc_info[1])

    def make_gui(self) -> "type[kvui.GameManager]":
        """
        To return the Kivy `App` class needed for `run_gui` so it can be overridden before being built

        Common changes are changing `base_title` to update the window title of the client and
        updating `logging_pairs` to automatically make new tabs that can be filled with their respective logger.

        ex. `logging_pairs.append(("Foo", "Bar"))`
        will add a "Bar" tab which follows the logger returned from `logging.getLogger("Foo")`
        """
        from kvui import GameManager

        class TextManager(GameManager):
            base_title = "Sonic Robo Blast 2 Client"

        return TextManager

    def run_gui(self):
        """Import kivy UI system from make_gui() and start running it as self.ui_task."""
        ui_class = self.make_gui()
        self.ui = ui_class(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")
        # self.save_watcher = asyncio.create_task(SaveFileWatcher(), name="SW")

    def run_cli(self):
        if sys.stdin:
            if sys.stdin.fileno() != 0:
                from multiprocessing import parent_process
                if parent_process():
                    return  # ignore MultiProcessing pipe

            # steam overlay breaks when starting console_loop
            if 'gameoverlayrenderer' in os.environ.get('LD_PRELOAD', ''):
                logger.info("Skipping terminal input, due to conflicting Steam Overlay detected. Please use GUI only.")
            else:
                self.input_task = asyncio.create_task(console_loop(self), name="Input")


async def SaveFileWatcher():
    while True:
        print("watching save file...")


async def keep_alive(ctx: CommonContext, seconds_between_checks=100):
    """some ISPs/network configurations drop TCP connections if no payload is sent (ignore TCP-keep-alive)
     so we send a payload to prevent drop and if we were dropped anyway this will cause an auto-reconnect."""
    seconds_elapsed = 0
    while not ctx.exit_event.is_set():
        await asyncio.sleep(1)  # short sleep to not block program shutdown
        if ctx.server and ctx.slot:
            seconds_elapsed += 1
            if seconds_elapsed > seconds_between_checks:
                await ctx.send_msgs([{"cmd": "Bounce", "slots": [ctx.slot]}])
                seconds_elapsed = 0


async def server_loop(ctx: CommonContext, address: typing.Optional[str] = None) -> None:
    if ctx.server and ctx.server.socket:
        logger.error('Already connected')
        return

    if address is None:  # set through CLI or APBP
        address = ctx.server_address

    # Wait for the user to provide a multiworld server address
    if not address:
        logger.info('Please connect to an Archipelago server.')
        return

    ctx.cancel_autoreconnect()
    if ctx._messagebox_connection_loss:
        ctx._messagebox_connection_loss.dismiss()
        ctx._messagebox_connection_loss = None

    address = f"ws://{address}" if "://" not in address \
        else address.replace("archipelago://", "ws://")

    server_url = urllib.parse.urlparse(address)
    if server_url.username:
        ctx.username = server_url.username
    if server_url.password:
        ctx.password = server_url.password

    def reconnect_hint() -> str:
        return ", type /connect to reconnect" if ctx.server_address else ""

    logger.info(f'Connecting to Archipelago server at {address}')
    try:
        port = server_url.port or 38281  # raises ValueError if invalid
        socket = await websockets.connect(address, port=port, ping_timeout=None, ping_interval=None,
                                          ssl=get_ssl_context() if address.startswith("wss://") else None,
                                          max_size=ctx.max_size)
        if ctx.ui is not None:
            ctx.ui.update_address_bar(server_url.netloc)
        ctx.server = Endpoint(socket)
        logger.info('Connected')
        ctx.server_address = address
        ctx.current_reconnect_delay = ctx.starting_reconnect_delay
        ctx.disconnected_intentionally = False
        async for data in ctx.server.socket:
            for msg in decode(data):
                await process_server_cmd(ctx, msg)
        logger.warning(f"Disconnected from multiworld server{reconnect_hint()}")
    except websockets.InvalidMessage:
        # probably encrypted
        if address.startswith("ws://"):
            # try wss
            await server_loop(ctx, "ws" + address[1:])
        else:
            ctx.handle_connection_loss(f"Lost connection to the multiworld server due to InvalidMessage"
                                       f"{reconnect_hint()}")
    except ConnectionRefusedError:
        ctx.handle_connection_loss("Connection refused by the server. "
                                   "May not be running Archipelago on that address or port.")
    except websockets.InvalidURI:
        ctx.handle_connection_loss("Failed to connect to the multiworld server (invalid URI)")
    except OSError:
        ctx.handle_connection_loss("Failed to connect to the multiworld server")
    except Exception:
        ctx.handle_connection_loss(f"Lost connection to the multiworld server{reconnect_hint()}")
    finally:
        await ctx.connection_closed()
        if ctx.server_address and ctx.username and not ctx.disconnected_intentionally:
            logger.info(f"... automatically reconnecting in {ctx.current_reconnect_delay} seconds")
            assert ctx.autoreconnect_task is None
            ctx.autoreconnect_task = asyncio.create_task(server_autoreconnect(ctx), name="server auto reconnect")
        ctx.current_reconnect_delay *= 2


async def server_autoreconnect(ctx: CommonContext):
    await asyncio.sleep(ctx.current_reconnect_delay)
    if ctx.server_address and ctx.server_task is None:
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")


async def process_server_cmd(ctx: CommonContext, args: dict):
    try:
        cmd = args["cmd"]
    except:
        logger.exception(f"Could not get command from {args}")
        raise

    if cmd == 'RoomInfo':
        if ctx.seed_name and ctx.seed_name != args["seed_name"]:
            msg = "The server is running a different multiworld than your client is. (invalid seed_name)"
            logger.info(msg, extra={'compact_gui': True})
            ctx.gui_error('Error', msg)
        else:
            logger.info('--------------------------------')
            logger.info('Room Information:')
            logger.info('--------------------------------')
            version = args["version"]
            ctx.server_version = Version(*version)

            if "generator_version" in args:
                ctx.generator_version = Version(*args["generator_version"])
                logger.info(f'Server protocol version: {ctx.server_version.as_simple_string()}, '
                            f'generator version: {ctx.generator_version.as_simple_string()}, '
                            f'tags: {", ".join(args["tags"])}')
            else:
                logger.info(f'Server protocol version: {ctx.server_version.as_simple_string()}, '
                            f'tags: {", ".join(args["tags"])}')
            if args['password']:
                logger.info('Password required')
            ctx.update_permissions(args.get("permissions", {}))
            logger.info(
                f"A !hint costs {args['hint_cost']}% of your total location count as points"
                f" and you get {args['location_check_points']}"
                f" for each location checked. Use !hint for more information.")
            ctx.hint_cost = int(args['hint_cost'])
            ctx.check_points = int(args['location_check_points'])

            if "players" in args:  # TODO remove when servers sending this are outdated
                players = args.get("players", [])
                if len(players) < 1:
                    logger.info('No player connected')
                else:
                    players.sort()
                    current_team = -1
                    logger.info('Connected Players:')
                    for network_player in players:
                        if network_player.team != current_team:
                            logger.info(f'  Team #{network_player.team + 1}')
                            current_team = network_player.team
                        logger.info('    %s (Player %d)' % (network_player.alias, network_player.slot))

            # update data package
            data_package_versions = args.get("datapackage_versions", {})
            data_package_checksums = args.get("datapackage_checksums", {})
            await ctx.prepare_data_package(set(args["games"]), data_package_versions, data_package_checksums)

            await ctx.server_auth(args['password'])

    elif cmd == 'DataPackage':
        ctx.consume_network_data_package(args['data'])

    elif cmd == 'ConnectionRefused':
        errors = args["errors"]
        if 'InvalidSlot' in errors:
            ctx.disconnected_intentionally = True
            ctx.event_invalid_slot()
        elif 'InvalidGame' in errors:
            ctx.disconnected_intentionally = True
            ctx.event_invalid_game()
        elif 'IncompatibleVersion' in errors:
            ctx.disconnected_intentionally = True
            raise Exception('Server reported your client version as incompatible. '
                            'This probably means you have to update.')
        elif 'InvalidItemsHandling' in errors:
            raise Exception('The item handling flags requested by the client are not supported')
        # last to check, recoverable problem
        elif 'InvalidPassword' in errors:
            logger.error('Invalid password')
            ctx.password = None
            await ctx.server_auth(True)
        elif errors:
            raise Exception("Unknown connection errors: " + str(errors))
        else:
            raise Exception('Connection refused by the multiworld host, no reason provided')

    elif cmd == 'Connected':
        ctx.username = ctx.auth
        ctx.team = args["team"]
        ctx.slot = args["slot"]
        # int keys get lost in JSON transfer
        ctx.slot_info = {0: NetworkSlot("Archipelago", "Archipelago", SlotType.player)}
        ctx.slot_info.update({int(pid): data for pid, data in args["slot_info"].items()})
        ctx.hint_points = args.get("hint_points", 0)
        ctx.consume_players_package(args["players"])
        ctx.stored_data_notification_keys.add(f"_read_hints_{ctx.team}_{ctx.slot}")
        ctx.goal_type = args["slot_data"]["CompletionType"]
        ctx.bcz_emblems = args["slot_data"]["BlackCoreEmblems"]
        if args["slot_data"]["DeathLink"] != 0:
            ctx.death_link = True
            ctx.tags.add("DeathLink")
        else:
            ctx.death_link = False

        msgs = []
        if ctx.locations_checked:
            msgs.append({"cmd": "LocationChecks",
                         "locations": list(ctx.locations_checked)})
        if ctx.locations_scouted:
            msgs.append({"cmd": "LocationScouts",
                         "locations": list(ctx.locations_scouted)})
        if ctx.stored_data_notification_keys:
            msgs.append({"cmd": "Get",
                         "keys": list(ctx.stored_data_notification_keys)})
            msgs.append({"cmd": "SetNotify",
                         "keys": list(ctx.stored_data_notification_keys)})
        if msgs:
            await ctx.send_msgs(msgs)
        if ctx.finished_game:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

        # Get the server side view of missing as of time of connecting.
        # This list is used to only send to the server what is reported as ACTUALLY Missing.
        # This also serves to allow an easy visual of what locations were already checked previously
        # when /missing is used for the client side view of what is missing.
        ctx.missing_locations = set(args["missing_locations"])
        ctx.checked_locations = set(args["checked_locations"])
        ctx.server_locations = ctx.missing_locations | ctx.checked_locations

        server_url = urllib.parse.urlparse(ctx.server_address)
        Utils.persistent_store("client", "last_server_address", server_url.netloc)

    elif cmd == 'ReceivedItems':

        start_index = args["index"]

        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        if start_index == len(ctx.items_received):
            for item in args['items']:
                ctx.items_received.append(NetworkItem(*item))
                str_itemname = ctx.item_names.lookup_in_game(item.item)
                str_senderloc = ctx.location_names.lookup_in_slot(item.location, item.player)
                str_sendername = ctx.slot_info[item.player].name

                #str_final = str_sendername+" sent "+str_itemname+" to "+ctx.slot_info[ctx.slot].name+" ("+str_senderloc+")\n"
                #if str_sendername == ctx.slot_info[ctx.slot].name:
                #    str_final = ctx.slot_info[ctx.slot].name+" found their "+str_itemname+" ("+str_senderloc+")\n"
                #ctx.texttransfer.append(str_final)
                #do something like ctx.texttransfer.append(str_final) and in file_watcher, write to all the files
        ctx.watcher_event.set()

    elif cmd == 'LocationInfo':
        for item in [NetworkItem(*item) for item in args['locations']]:
            ctx.locations_info[item.location] = item
        ctx.watcher_event.set()

    elif cmd == "RoomUpdate":
        if "players" in args:
            ctx.consume_players_package(args["players"])
        if "hint_points" in args:
            ctx.hint_points = args['hint_points']
        if "checked_locations" in args:
            checked = set(args["checked_locations"])
            ctx.checked_locations |= checked
            ctx.missing_locations -= checked
        if "permissions" in args:
            ctx.update_permissions(args["permissions"])

    elif cmd == 'Print':
        ctx.on_print(args)

    elif cmd == 'PrintJSON':
        ctx.on_print_json(args)

    elif cmd == 'InvalidPacket':
        logger.warning(f"Invalid Packet of {args['type']}: {args['text']}")


    elif cmd == "Bounced":
        tags = args.get("tags", [])
        # we can skip checking "DeathLink" in ctx.tags, as otherwise we wouldn't have been send this
        if "DeathLink" in tags and ctx.last_death_link != args["data"]["time"]:
            ctx.on_deathlink(args["data"])

    elif cmd == "Retrieved":
        ctx.stored_data.update(args["keys"])
        if ctx.ui and f"_read_hints_{ctx.team}_{ctx.slot}" in args["keys"]:
            ctx.ui.update_hints()

    elif cmd == "SetReply":
        ctx.stored_data[args["key"]] = args["value"]
        if ctx.ui and f"_read_hints_{ctx.team}_{ctx.slot}" == args["key"]:
            ctx.ui.update_hints()
        elif args["key"].startswith("EnergyLink"):
            ctx.current_energy_link_value = args["value"]
            if ctx.ui:
                ctx.ui.set_new_energy_link_value()
    else:
        logger.debug(f"unknown command {cmd}")

    ctx.on_package(cmd, args)


async def console_loop(ctx: CommonContext):
    commandprocessor = ctx.command_processor(ctx)
    queue = asyncio.Queue()
    stream_input(sys.stdin, queue)
    while not ctx.exit_event.is_set():
        try:
            input_text = await queue.get()
            queue.task_done()

            if ctx.input_requests > 0:
                ctx.input_requests -= 1
                ctx.input_queue.put_nowait(input_text)
                continue

            if input_text:
                commandprocessor(input_text)
        except Exception as e:
            logger.exception(e)


def get_base_parser(description: typing.Optional[str] = None):
    """Base argument parser to be reused for components subclassing off of CommonClient"""
    import argparse
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--connect', default=None, help='Address of the multiworld host.')
    parser.add_argument('--password', default=None, help='Password of the multiworld host.')
    if sys.stdout:  # If terminal output exists, offer gui-less mode
        parser.add_argument('--nogui', default=False, action='store_true', help="Turns off Client GUI.")
    return parser


def handle_url_arg(args: "argparse.Namespace",
                   parser: "typing.Optional[argparse.ArgumentParser]" = None) -> "argparse.Namespace":
    """
    Parse the url arg "archipelago://name:pass@host:port" from launcher into correct launch args for CommonClient
    If alternate data is required the urlparse response is saved back to args.url if valid
    """
    if not args.url:
        return args

    url = urllib.parse.urlparse(args.url)
    if url.scheme != "archipelago":
        if not parser:
            parser = get_base_parser()
        parser.error(f"bad url, found {args.url}, expected url in form of archipelago://archipelago.gg:38281")
        return args

    args.url = url
    args.connect = url.netloc
    if url.username:
        args.name = urllib.parse.unquote(url.username)
    if url.password:
        args.password = urllib.parse.unquote(url.password)

    return args


def run_as_textclient(*args):
    class TextContext(CommonContext):
        # Text Mode to use !hint and such with games that have no text entry
        tags = CommonContext.tags
        game = "Sonic Robo Blast 2"  # empty matches any game since 0.3.2
        items_handling = 0b111  # receive all items for /received
        want_slot_data = True  # Can't use game specific slot_data

        async def server_auth(self, password_requested: bool = False):
            if password_requested and not self.password:
                await super(TextContext, self).server_auth(password_requested)
            await self.get_username()
            await self.send_connect(game="Sonic Robo Blast 2")

        def on_package(self, cmd: str, args: dict):
            if cmd == "Connected":
                self.game = self.slot_info[self.slot].game

        async def disconnect(self, allow_autoreconnect: bool = False):
            self.game = ""
            await super().disconnect(allow_autoreconnect)

    async def main(args):
        ctx = TextContext(args.connect, args.password)
        ctx.auth = args.name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        loop = asyncio.get_running_loop()
        file_path = filedialog.askdirectory(title="Select SRB2 root folder")
        loop.create_task(file_watcher(ctx, file_path), name="save data watcher")
        loop.create_task(item_handler(ctx, file_path), name="incoming item handler")
        # why the fuck does it work now

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Gameless Archipelago Client, for text interfacing.")
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args(args)

    args = handle_url_arg(args, parser=parser)

    # use colorama to display colored text highlighting on windows
    colorama.init()

    asyncio.run(main(args))
    print("got to the funny place")
    colorama.deinit()


async def item_handler(ctx, file_path):
    file_path2 = file_path + "/apgamedat1.ssg"

    f = open(file_path + "/luafiles/APTranslator.dat", 'w+b')
    f.close()
    # set up new save file here
    # dont need to zero anything out because the first write will overwrite everything wrong

    locs_received = []
    final_write = [0, 0, 0, 0]
    sent_shields = [0, 0, 0, 0, 0, 0, 0, 0]

    while True:
        while ctx.total_locations is None:
            await asyncio.sleep(1)
            continue
        try:
            f = open(file_path + "/luafiles/APTranslator.dat", 'r+b')
        except PermissionError:
            await asyncio.sleep(1)
            continue


        if len(ctx.texttransfer) > 0:
            h = open(file_path + "/luafiles/APTextTransfer.txt", 'w+b')#i love character 81 not fucking existing so i cant use the python string stuf :))))))
            for jsons in ctx.texttransfer:
                for strings in jsons:
                    try:
                        type = strings["type"]
                        if type == "player_id":
                            if int(strings["text"]) == ctx.slot:
                                h.write(0x81.to_bytes(1, byteorder="little"))
                            else:
                                h.write(0x82.to_bytes(1, byteorder="little"))
                            h.write((ctx.slot_info[int(strings["text"])].name).encode("ascii"))
                        elif type == "item_id":
                            if int(strings["flags"])==0:#filler
                                h.write(0x88.to_bytes(1, byteorder="little"))
                            if int(strings["flags"])==1:#important
                                h.write(0x89.to_bytes(1, byteorder="little"))
                            if int(strings["flags"])==2:#useful
                                h.write(0x84.to_bytes(1, byteorder="little"))
                            if int(strings["flags"])==3:#no clue
                                h.write(0x8F.to_bytes(1, byteorder="little"))
                            if int(strings["flags"])==4:#trap
                                h.write(0x87.to_bytes(1, byteorder="little"))
                            h.write((ctx.item_names.lookup_in_game(int(strings["text"]), ctx.slot_info[int(strings["player"])].game)).encode("ascii"))#int(strings["player"])))

                        elif type == "location_id":
                            h.write(0x83.to_bytes(1, byteorder="little"))
                            h.write((ctx.location_names.lookup_in_slot(int(strings["text"]), int(strings["player"]))).encode("ascii"))

                    except KeyError:
                        h.write(0x80.to_bytes(1, byteorder="little"))
                        h.write((strings["text"].encode("ascii"))) #stupid
                h.write(0x0A.to_bytes(1, byteorder="little"))
            ctx.texttransfer = []
            f.seek(0x18)
            f.write(0x01.to_bytes(1, byteorder="little"))#let srb2 know to read the texttransfer file
            h.close()




        traps = 0
        emeralds = 0
        emblemhints = 0
        emblems = 0
        startrings = 0
        soundtest = 0
        f.seek(0x12)
        num_traps = int.from_bytes(f.read(2), 'little')

        # read characters until null terminator in g
        # compare string/number to token list
        # if found, send respective check
        # repeat until end of file
        # clear file g

        for i in ctx.items_received:
            id = i[0]
            if id == 2:
                emeralds += 1
                continue
            if id == 1:
                emblems += 1
                continue
            if id == 3:
                emblemhints += 1
            if id == 80:
                soundtest = 1
            if id == 74:
                startrings += 1
            if id == 4 or id == 5 or id == 6 or id == 7 or id == 8 or id == 9 or id == 70 or id == 71 or id == 72 or id == 73 or id == 75 or id == 76 or id == 77 or id == 78 or id == 79:
                traps += 1
                if traps == num_traps + 1:

                    f.seek(0x02)
                    if id == 4:  # 1up
                        f.write(0x01.to_bytes(2, byteorder="little"))
                    if id == 6:  # pity shield
                        f.write(0x02.to_bytes(2, byteorder="little"))
                    if id == 5:  # gravity boots
                        f.write(0x03.to_bytes(2, byteorder="little"))
                    if id == 7:  # replay tutorial
                        f.write(0x04.to_bytes(2, byteorder="little"))
                    if id == 8:  # ring loss
                        f.write(0x05.to_bytes(2, byteorder="little"))
                    if id == 9:  # drop inputs
                        f.write(0x07.to_bytes(2, byteorder="little"))
                    if id == 70:  # & knuckles
                        f.write(0x06.to_bytes(2, byteorder="little"))
                    if id == 71:  # 50 rings
                        f.write(0x08.to_bytes(2, byteorder="little"))
                    if id == 72:  # 20 rings
                        f.write(0x09.to_bytes(2, byteorder="little"))
                    if id == 73:  # 10 rings
                        f.write(0x0A.to_bytes(2, byteorder="little"))
                    if id == 75:  # slippery floors
                        f.write(0x0B.to_bytes(2, byteorder="little"))
                    if id == 76:  # 1000 points
                        f.write(0x0C.to_bytes(2, byteorder="little"))
                    if id == 77:  # sonic forces
                        f.write(0x0D.to_bytes(2, byteorder="little"))
                    if id == 78:  # temp invincibility
                        f.write(0x0E.to_bytes(2, byteorder="little"))
                    if id == 79:  # temp speed shoes
                        f.write(0x0F.to_bytes(2, byteorder="little"))

                    f.seek(0x12)
                    f.write((num_traps + 1).to_bytes(2, byteorder="little"))

                continue
                # in the future it would be efficient to always hold a list of sent items so the file doesnt
            if id in locs_received:  # have to be read every second
                continue

            if id == 10:  # greenflower
                final_write[0] = final_write[0] + 1
            if id == 11:  # techno hill
                final_write[0] = final_write[0] + 2
            if id == 12:  # deep sea
                final_write[0] = final_write[0] + 4
            if id == 13:  # castle eggman
                final_write[0] = final_write[0] + 8
            if id == 14:  # arid canyon
                final_write[0] = final_write[0] + 16
            if id == 15:  # red volcano
                final_write[0] = final_write[0] + 32
            if id == 16:  # egg rock
                final_write[0] = final_write[0] + 64
            if id == 17 and ctx.bcz_emblems == 0:  # black core
                final_write[0] = final_write[0] + 128
            if id == 18:  # frozen hillside
                final_write[1] = final_write[1] + 8
            if id == 19:  # pipe towers
                final_write[1] = final_write[1] + 16
            if id == 20:  # forest fortress
                final_write[1] = final_write[1] + 32
            if id == 21:  # final demo
                final_write[1] = final_write[1] + 64
            if id == 22:  # haunted heights
                final_write[1] = final_write[1] + 1
            if id == 23:  # aerial garden
                final_write[1] = final_write[1] + 2
            if id == 24:  # azure temple
                final_write[1] = final_write[1] + 4
            if id == 50:  # tails
                final_write[1] = final_write[1] + 128
            if id == 51:  # knuckles
                final_write[2] = final_write[2] + 1
            if id == 53:  # fang
                final_write[2] = final_write[2] + 2
            if id == 52:  # amy
                final_write[2] = final_write[2] + 4
            if id == 54:  # metal sonic
                final_write[2] = final_write[2] + 8
            if id == 25:  # floral fields
                final_write[2] = final_write[2] + 16
            if id == 26:  # toxic plateau
                final_write[2] = final_write[2] + 32
            if id == 27:  # flooded cove
                final_write[2] = final_write[2] + 64
            if id == 28:  # cavern fortress
                final_write[2] = final_write[2] + 128
            if id == 29:  # dusty wasteland
                final_write[3] = final_write[3] + 1
            if id == 30:  # magma caves
                final_write[3] = final_write[3] + 2
            if id == 31:  # egg satellite
                final_write[3] = final_write[3] + 4
            if id == 32:  # black hole
                final_write[3] = final_write[3] + 8
            if id == 33:  # christmas chime
                final_write[3] = final_write[3] + 16
            if id == 34:  # dream hill
                final_write[3] = final_write[3] + 32
            if id == 35:  # alpine praradise
                final_write[3] = final_write[3] + 64
            if id == 56:  # whirlwind
                sent_shields[0] = 1
            if id == 57:  # armageddon
                sent_shields[1] = sent_shields[1]+1
            if id == 100: #paraloop
                sent_shields[1] = sent_shields[1] + 2
            if id == 101: #night helper
                sent_shields[1] = sent_shields[1] + 4
            if id == 102: #link freeze
                sent_shields[1] = sent_shields[1] + 8
            if id == 103: #extra time
                sent_shields[1] = sent_shields[1] + 16
            if id == 104: #drill refill
                sent_shields[1] = sent_shields[1] + 32

            if id == 58:  # elemental
                sent_shields[2] = 1
            if id == 59:  # attraction
                sent_shields[3] = 1
            if id == 60:  # force
                sent_shields[4] = 1
            if id == 61:  # flame
                sent_shields[5] = 1
            if id == 62:  # bubble
                sent_shields[6] = 1
            if id == 56:  # lightning
                sent_shields[7] = 1


            locs_received.append(id)
        if (ctx.bcz_emblems > 0 and emblems >= ctx.bcz_emblems) and 17 not in locs_received:
            locs_received.append(17)
            final_write[0] = final_write[0] + 128
        # this would be so much better if i made a list of everything and then wrote it to the file all at once
        f.seek(0x14)
        if emblemhints >= 2:
            emblemhints = 3 #bits 1 and 2 set
        if soundtest!= 0:
            emblemhints += 4 #sound test bullshit
        f.write(emblemhints.to_bytes(1, byteorder="little"))  # this sucks
        if emeralds > 7:
            emeralds = 7
        f.seek(0x0F)

        if emeralds == 0:
            f.write(0x00.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 1:
            f.write(0x01.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 2:
            f.write(0x03.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 3:
            f.write(0x07.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 4:
            f.write(0x0F.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 5:
            f.write(0x1F.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 6:
            f.write(0x3F.to_bytes(2, byteorder="little"))  # this sucks
        if emeralds == 7:
            f.write(0x7F.to_bytes(2, byteorder="little"))  # this sucks


        f.seek(0x03)
        f.write(bytes(sent_shields))
        for i in range(len(final_write)):
            if final_write[i] > 255:
                final_write[i] = 255
        f.seek(0x0B)
        f.write(bytes(final_write))  # TODO change to only write on startup, file close, or new item received
        f.seek(0x15)
        f.write(emblems.to_bytes(1, byteorder="little"))
        f.seek(0x16)
        f.write(ctx.bcz_emblems.to_bytes(1, byteorder="little"))
        f.seek(0x17)
        f.write(startrings.to_bytes(1, byteorder="little"))

        try:
            g = open(file_path2, 'r+b')
            g.seek(0x10)  # always select No save to go back to the ap hub
            g.write(0x7D.to_bytes(2, byteorder="little"))  # or find a console command that does that
            g.close()
        except:
            print("save file 1 not found, create it to more easily return to the multiworld hub")

        # todo handle deathlink traps and 1ups
        f.seek(0x01)
        is_dead = f.read(1)
        if ctx.death_link == True:
            if ctx.death_link_lockout + 4 <= time.time():

                if ctx.activate_death == True:
                    f.seek(0x00)  # received deathlink
                    f.write(0x01.to_bytes(1, byteorder="little"))
                    ctx.death_link_lockout = time.time()
                    print("kill yourself")
                    ctx.activate_death = False

                elif is_dead != b'\x00':  # outgoing deathlink
                    f.seek(0x01)
                    f.write(0x00.to_bytes(1, byteorder="little"))
                    message = [ctx.player_names[ctx.slot] + " wasn't able to retry in time"]

                    await ctx.send_death(message)
                    ctx.death_link_lockout = time.time()
                    print("killed myself")

            else:
                ctx.activate_death = False
                print("in lockout")
                # write 0s to both slots if conditions havent been met
                f.seek(0x00)
                f.write(0x00.to_bytes(2, byteorder="little"))
        # print("wrote new file data")
        f.close()
        await asyncio.sleep(1)


async def file_watcher(ctx, file_path):
    locs_to_send = set()
    num_sent = 0
    locs_sent = set()
    file_path2 = file_path + "/apgamedat.dat"

    while ctx.total_locations is None:
        await asyncio.sleep(1)
        continue

    await ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": ctx.tags}])
    # wait to connect



    try:  # once connected verify apgamedat exists

        if not os.path.isfile(file_path2):
            raise FileNotFoundError  # stupid code
        f = open(file_path2, 'r+b')
        checkma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0,0,0,0,0,0]
        for i in ctx.checked_locations:
            if i < 240:
                i = i - 1
                r1 = math.floor(i / 8)
                r2 = i % 8

                # divide then floor to get byte number
                # modulo to get byte value to set
                if r2 == 0:
                    checkma[r1] += 1
                if r2 == 1:
                    checkma[r1] += 2
                if r2 == 2:
                    checkma[r1] += 4
                if r2 == 3:
                    checkma[r1] += 8
                if r2 == 4:
                    checkma[r1] += 16
                if r2 == 5:
                    checkma[r1] += 32
                if r2 == 6:
                    checkma[r1] += 64
                if r2 == 7:
                    checkma[r1] += 128
        f.seek(0x0C)
        for i in range(0x50):
            f.write(0x01.to_bytes(1, byteorder="little")) #set level visited flags
        f.seek(0x450)
        f.write(0x00.to_bytes(0x1000, byteorder="little"))
        f.seek(0x417)
        f.write(bytes(checkma))


        f.close()
    except FileNotFoundError:

        print("apgamedat.dat does not exist, let SRB2 make a new one...")
    except PermissionError:
        print("could not overwrite old save data (lack of permission). Try closing the file in HXD you dumbass")

    cfg = open(file_path + "/AUTOEXEC.CFG", "w")
    cfg.write("addfile addons/SL_ArchipelagoSRB2_v120.pk3")
    cfg.close()
    os.chdir(file_path)
    try:
        os.startfile("srb2win.exe")
        await asyncio.sleep(10)
    except:
        logger.info(
            'Could not open srb2win.exe. If you are using Linux, you must open the game and load the addon manually')
    # look into subprocess.Popen, if used correctly, i might be able to acess srb2's console output for commands and
    # use COM_BufInsertText(server, "command") to type in console
    # recieved notifications

    cfg = open(file_path + "/AUTOEXEC.CFG", "w")
    cfg.write("")
    cfg.close()
    # if not do nothing (srb2 will create an empty gamedat on launch)
    # if it does, get checked locations from the server, and overwrite corresponding bits in apgamedat

    # create AUTOEXEC.CFG with the text "addfile addons/ArchipelagoSRB2.pk3"
    # launch srb2
    # clear AUTOEXEC.CFG so people dont get confused when they cant uninstall the ap mod
    while not os.path.isfile(file_path2):
        await asyncio.sleep(1)  # wait for srb2 to make new apgamedat if it doesnt exist
    previous = os.stat(file_path2).st_mtime
    token_numbers = ["1111149056392167424", "1205520896132120576",
                     "2429916160140509184",
                     "2-134217728-658505728",
                     "2-360185856-495452160",
                     "4979369984-525336576",
                     "41241513984-335544320",
                     "554525952-457179136",
                     "5-1048576000-398458880",
                     "741313894458720256",
                     "7763363328442499072",
                     "7125829120645922816",
                     "7838860800929038336",
                     "767528294458720256",
                     "81522532352-880803840",
                     "8964689920541065216",
                     "8635437056-434110464",
                     "8579862528461373440",
                     "1016777216-880803840",
                     "10352321536-434110464",
                     "10752877568264241152",
                     "11-587202560-1132462080",
                     "11362807296-650117120",
                     "11-318767104-1040187392",
                     "11-738197504-213909504",
                     "11452984832115343360",
                     "13-263192576-510132224",
                     "13-805306368-415236096",
                     "13184549376-75497472",
                     "148388608-1247805440",
                     "14514850816-429391872",
                     "14589299712-1384120320",
                     "161562378240243269632",
                     "16232783872557842432",
                     "163019898881172307968",
                     "16-158007296-949813248",
                     "22312475648-427819008",
                     "22-878706688-677380096",
                     "2325165824633339904",
                     "23664797184679477248",
                     "23-742391808266338304",
                     "33-1742733312-1530920960",
                     "33-662700032-1296039936",
                     "33-585629696-1988624384",
                     "331482686464-1557135360",
                     "331577058304-1828716544",
                     "331665138688-243269632",
                     "331694498816-494927872",
                     "331811939328754974720",
                     "331728053248436207616",
                     "3316714301441484783616",
                     "411069547520-618659840",
                     "41-576716800-681574400",
                     "41-576716800-694157312",
                     "41-589299712-694157312",
                     "41-589299712-681574400",
                     "411614807041367343104"
                     ]
    oneupids = ["1:354418688199229440",
                "1:692060160146800640",
                "1:77594624381681664",
                "2:-31457280-293601280",
                "2:188743680-406847488",
                "2:-195035136-306184192",
                "2:12320768-22740992",
                "2:-7759462433554432",
                "2:216006656434110464",
                "2:-463470592-635437056",
                "2:47185920-676331520",
                "2:-260046848314572800",
                "4:364904448-220200960",
                "4:-255852544-801112064",
                "4:197132288-599785472",
                "4:-62914560-794820608",
                "4:1069547520-620756992",
                "4:1321205760-517996544",
                "4:717225984-759169024",
                "4:943718400-406847488",
                "4:195035136287309824",
                "5:-1149239296134217728",
                "5:0146800640",
                "5:-861929472522190848",
                "5:-205520896-29360128",
                "5:115343360358612992",
                "5:-1218445312-268435456",
                "5:-759169024-312475648",
                "5:-134217728-515899392",
                "5:367001600-731906048",
                "5:54525952-402653184",
                "5:-1048576000-423624704",
                "5:270532608-14680064",
                "7:197132288222298112",
                "7:192937984343932928",
                "7:721420288373293056",
                "7:566231040207618048",
                "7:65011712058720256",
                "7:13421772847185920",
                "7:102341017658720256",
                "7:-216006656444596224",
                "7:333447168778043392",
                "7:713031680364904448",
                "7:1310720000991952896",
                "7:20971520297795584",
                "7:2034237441017118720",
                "7:2160066561017118720",
                "7:1152385024-363331584",
                "7:1166016512796917760",
                "7:4194304801112064",
                "7:914358272-138412032",
                "7:675282944-48234496",
                "8:989855744401604608",
                "8:1759510528759169024",
                "8:989855744395313152",
                "8:1262485504-385875968",
                "8:1249902592-708837376",
                "8:635437056-218103808",
                "8:568328192849346560",
                "8:1035993088184549376",
                "8:169449881616777216",
                "8:1245708288612368384",
                "8:378535936675282944",
                "8:6270484481113587712",
                "8:127926272-143654912",
                "8:111149056169869312",
                "8:989855744398458880",
                "10:-530579456-564133888",
                "10:-8912896-645922816",
                "10:73400320-423624704",
                "10:677380096398458880",
                "10:-264241152-729808896",
                "10:33554432012582912",
                "10:-122683392-403701760",
                "10:192937984446693376",
                "10:497025024-169869312",
                "10:218103808281018368",
                "11:0-1426063360",
                "11:-234881024-964689920",
                "11:138412032-20971520",
                "11:0-444596224",
                "11:201326592-1056964608",
                "11:-301989888121634816",
                "11:-446693376-1098907648",
                "11:-201326592-1367343104",
                "11:545259520436207616",
                "11:568328192-975175680",
                "11:-86402662454525952",
                "11:-318767104-889192448",
                "11:-452984832125829120",
                "11:81369497650331648",
                "13:-587202566291456",
                "13:-171966464-1027604480",
                "13:348127232-358612992",
                "13:130023424-46137344",
                "13:-432013312-189792256",
                "13:339738624-289406976",
                "13:184549376-65011712",
                "13:178257920-1025507328",
                "13:-339738624977272832",
                "13:-73400320065011712",
                "14:-664797184-304087040",
                "14:322961408-1396703232",
                "14:-228589568-1356857344",
                "14:479199232-421527552",
                "14:440401920-1495269376",
                "14:254803968-1077936128",
                "14:-142606336-780140544",
                "14:10485760-706740224",
                "14:146800640-1012924416",
                "14:8388608-1029701632",
                "14:-479526912-814809088",
                "14:-933232640-415236096",
                "14:-464519168-905969664",
                "14:180355072-640679936",
                "14:-231735296220200960",
                "14:-327155712-507510784",
                "14:199229440-1507852288",
                "14:-92274688-981467136",
                "16:-565182464-536870912",
                "16:1541668864276824064",
                "16:1717567488457179136",
                "16:836239360549978112",
                "16:677380096-253755392",
                "16:142606336727711744",
                "16:-264241152-1077936128",
                "16:476053504-385875968",
                "16:494927872782237696",
                "22:-4194304-710934528",
                "22:-339738624-738197504",
                "22:455081984-692060160",
                "22:402653184-138412032",
                "22:-719323136-478150656",
                "22:-392167424-144703488",
                "22:-436207616-184549376",
                "22:-490733568-515899392",
                "23:-3271557121140850688",
                "23:-3313500161140850688",
                "23:-340787200413138944",
                "23:-104857600576716800",
                "23:-603979776811597824",
                "23:3418357761358954496",
                "23:-7822376961000341504",
                "23:-436207616530579456",
                "23:7298088961012924416",
                "23:1509949441635778560",
                "23:-788529152461373440",
                "23:-843055104461373440",
                "23:662700032683671552",
                "23:16777216499122176",
                "25:-795869184-218103808",
                "25:-678428672-186646528",
                "30:436207616-303038464",
                "30:-192937984-1256194048",
                "31:-1032847363604480",
                "31:-14155776334036992",
                "31:458752000427294720",
                "31:753401856-334036992",
                "31:50488934440370176",
                "31:573046784-245891072",
                "32:-83886080-503316480",
                "32:67108864-427819008",
                "32:595591168838860800",
                "32:381681664548405248",
                "32:966787072699400192",
                "33:-1784676352-1310720000",
                "33:-610271232-1344274432",
                "33:-398458880-1740636160",
                "33:603979776-1686110208",
                "33:1933574144-654311424",
                "33:1379926016-419430400",
                "33:1237319680989855744",
                "33:1803550720494927872",
                "33:1816133632482344960",
                "33:1602224128809500672",
                "33:13233029121673527296",
                "33:18475909121749024768",
                "33:-5966397441069547520",
                "33:325058561862270976",
                "33:5567938561761607680",
                "40:210763776277872640",
                "40:889192448824180736",
                "40:922746881186988032",
                "40:-4069130241028259840",
                "40:-2621440001186988032",
                "40:281018368802160640",
                "40:398458880778043392",
                "40:-807403520734003200",
                "40:-719323136369098752",
                "40:-5054136321205862400",
                "40:658505728635437056",
                "40:5012193281583349760",
                "40:7759462401134559232",
                "40:-1971322881357905920",
                "40:117440512174063616",
                "40:540934144780533760",
                "40:574619648947912704",
                "41:-912261120335544320",
                "41:-476053504-882900992",
                "41:-524288000-364904448",
                "41:660602880-610271232",
                "41:329252864924844032",
                "41:-62914560641728512",
                "41:-276824064708837376",
                "41:-83886080-1306525696",
                "41:-83886080-1119879168",
                "41:-952107008-369098752",
                "41:-578813952822083584",
                "41:-578813952813694976",
                "41:-587202560813694976",
                "41:-587202560822083584",
                "41:-89128960056623104",
                "41:-583008256-532676608",
                "41:-627048448232783872",
                "41:-538968064232783872",
                "41:1065353216-618659840",
                "41:648019968-1201668096",
                "41:513802240-931135488",
                "41:467664896-931135488",
                "41:1283457024-645922816",
                "41:905969664-968884224",
                "41:358612992924844032",
                "41:199229440-23068672",
                "41:3439329281352663040",
                "41:343932928809500672",
                "41:335544320591396864",
                "41:-77594624-694157312",
                "41:1908408321394606080",
                "41:2243952641218445312",
                "42:119537664564133888",
                "42:-2097152438304768",
                "42:121634816652214272",
                "42:33554432918552576",
                "42:-148897792843055104",
                "42:-211812352924844032",
                "42:94371840962592768",
                "42:-165675008478150656",
                "42:-1950351361172307968",
                "42:-2747269121398800384",
                "42:-2747269121394606080",
                "42:-2747269121402994688",
                "42:-796917761476395008",
                "42:272629760811597824",
                "42:2390753281684013056",
                "42:-69206016270532608",
                "42:-1803550721306525696",
                "42:2390753281696595968"]
    # todo find a not stupid way of differentiating objects - currently the format is "[Map#][object.z] "
    # probably do "[Map#][object.x][object.y] " and if theres objects on top of each other i guess i can go fuck myself

    while True:
        # run the console command to get recieved items
        try:
            g = open(file_path + "/luafiles/APTokens.txt", 'r+')
            for lines in g:
                lines = lines.strip()
                if lines is None:
                    break
                for i in token_numbers:
                    if lines == i:
                        locs_to_send.add(token_numbers.index(i) + 240)
                        break
                for i in oneupids:
                    if lines == i:
                        locs_to_send.add(oneupids.index(i) + 300)
                        break

            g.truncate(0)
            g.close()
        except FileNotFoundError:
            print("APTokens.txt not found, collect an emerald token to create it")

        current = os.stat(file_path2).st_mtime
        if current != previous:

            previous = current
            with open(file_path2, 'rb') as f:
                f.seek(0x417)  # start of the emblem save file
                for i in range(0, 0x1E):
                    byte = int.from_bytes(f.read(1), 'little')
                    # convert each check into corresponding location number
                    for j in range(8):
                        bit = (byte >> j) & 1
                        if bit == 1:
                            locs_to_send.add(8 * i + j + 1)
                            if (8 * i + j + 1) == 128 and ctx.goal_type == 0:
                                ctx.finished_game = True
                                await ctx.send_msgs([{
                                    "cmd": "StatusUpdate",
                                    "status": ClientStatus.CLIENT_GOAL
                                }])

                f.seek(0x457)
                byte = int.from_bytes(f.read(1), 'little')
                if byte != 0 and ctx.goal_type == 1:
                    ctx.finished_game = True
                    locs_to_send.add(238)
                    await ctx.send_msgs([{
                        "cmd": "StatusUpdate",
                        "status": ClientStatus.CLIENT_GOAL
                    }])


            f.close()
            # Compare locs_to_send to locations already sent
        if len(locs_to_send) > num_sent:
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])
            print("sending new checks")
            num_sent = len(locs_to_send)
        await asyncio.sleep(1)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    # t = threading.Thread(target=file_watcher)
    # t.daemon = True
    # t.start()
    run_as_textclient(*sys.argv[1:])
