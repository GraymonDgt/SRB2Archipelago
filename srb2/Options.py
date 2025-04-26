import typing
from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup


class TimeEmblems(DefaultOnToggle):
    """Enable record attack time emblems (27 Locations)"""
    display_name = "Time Emblems"
class RingEmblems(DefaultOnToggle):
    """Enable record attack Ring emblems (20 Locations)"""
    display_name = "Ring Emblems"
class ScoreEmblems(DefaultOnToggle):
    """Enable record attack Score emblems (7 Locations)"""
    display_name = "Score Emblems"
class RankEmblems(DefaultOnToggle):
    """Enable NiGHTS A Rank emblems (12 Locations)"""
    display_name = "NiGHTS Rank Emblems"
class NTimeEmblems(DefaultOnToggle):
    """Enable NiGHTS Time emblems (12 Locations)"""
    display_name = "NiGHTS Time Emblems"


class RadarStart(Toggle):
    """Start with Emblem Hints + Radar, useful if you don't know where all the emblems are"""
    display_name = "Start with Emblem Radar"

class LogicDifficulty(Choice):
    """Difficulty of logic required to get items
    Normal - Tails/Knuckles required for difficult emblems, no badnik bouncing
    Hard - If it's possible, it's in logic
    Custom - Disables logic for custom character use"""
    option_normal = 0
    option_hard = 1
    option_custom = 2
    default = 0



class OneUpSanity(Toggle):
    """Enable 1UP Monitors as checks (247 Locations)"""
    display_name = "1UP-Sanity"




class BlackCoreEmblemCost(Range):
    """Percentage of emblems needed for black core zone to be unlocked
    Putting 0 will make Black Core Zone an item in the multiworld like the rest of the zones"""
    display_name = "Emblems for Black Core"
    range_start = 0
    range_end = 100
    default = 50

class EmblemNumber(Range):
    """Total Number of emblems
    (There are about 250 locations with all emblems turned on)"""
    display_name = "Total Emblems"
    range_start = 50
    range_end = 300
    default = 180


class CompletionType(Choice):
    """Set goal for Victory Condition
    Bad Ending Requires Beating Black Core Zone Act 3
    Good Ending Requires The 7 Chaos Emeralds"""

    display_name = "Completion Goal"
    option_Bad_Ending = 0
    option_Good_Ending = 1



srb2_options_groups = [
    OptionGroup("Emblem Toggles", [
        TimeEmblems,
        RingEmblems,
        ScoreEmblems,
        RankEmblems,
        NTimeEmblems,
        OneUpSanity,
    ]),
    OptionGroup("Meta Options", [
        LogicDifficulty,
        RadarStart,
        BlackCoreEmblemCost,
        EmblemNumber,
    ]),
]

@dataclass
class SRB2Options(PerGameCommonOptions):

    time_emblems: TimeEmblems
    ring_emblems: RingEmblems
    score_emblems: ScoreEmblems
    rank_emblems: RankEmblems
    ntime_emblems: NTimeEmblems
    difficulty: LogicDifficulty
    oneup_sanity: OneUpSanity
    radar_start: RadarStart
    num_emblems: EmblemNumber
    bcz_emblems:BlackCoreEmblemCost
    death_link: DeathLink
    completion_type: CompletionType
