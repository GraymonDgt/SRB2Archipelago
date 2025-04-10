import typing
from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup


class TimeEmblems(DefaultOnToggle):
    """Enable record attack time emblems"""
    display_name = "Time Emblems"
class RingEmblems(DefaultOnToggle):
    """Enable record attack Ring emblems"""
    display_name = "Ring Emblems"
class ScoreEmblems(DefaultOnToggle):
    """Enable record attack Score emblems"""
    display_name = "Score Emblems"
class RankEmblems(DefaultOnToggle):
    """Enable NiGHTS A Rank emblems"""
    display_name = "NiGHTS Rank Emblems"
class NTimeEmblems(DefaultOnToggle):
    """Enable NiGHTS Time emblems"""
    display_name = "NiGHTS Time Emblems"

class BlackCoreEmblemCost(Range):
    """Amount of emblems needed for black core zone to be unlocked
    Putting 0 will make Black Core Zone an item in the multiworld like the rest of the zones"""
    display_name = "Emblems for Black Core"
    range_start = 0
    range_end = 120
    default = 80

class EmblemNumber(Range):
    """Total Number of emblems (DOESN'T WORK CURRENTLY)"""
    display_name = "Total Emblems"
    range_start = 120
    range_end = 200
    default = 200


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
    ]),
    OptionGroup("Meta Options", [
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
    num_emblems: EmblemNumber
    bcz_emblems:BlackCoreEmblemCost
    death_link: DeathLink
    completion_type: CompletionType
