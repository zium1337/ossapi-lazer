import logging
# we need to explicitly set a handler for the logging module to be happy
handler = logging.StreamHandler()
logging.getLogger("ossapi").addHandler(handler)
from importlib import metadata

from ossapi.ossapi import (OssapiV1, ReplayUnavailableException,
    InvalidKeyException, APIException)
from ossapi.ossapiv2 import Ossapi, Grant, Scope, Domain
from ossapi.models import (Beatmap, BeatmapCompact, BeatmapUserScore,
    ForumTopicAndPosts, Search, CommentBundle, Cursor, Score,
    BeatmapsetSearchResult, ModdingHistoryEventsBundle, User, Rankings,
    BeatmapScores, KudosuHistory, Beatmapset, BeatmapPlaycount, Spotlight,
    Spotlights, WikiPage, _Event, Event, BeatmapsetDiscussionPosts, Build,
    ChangelogListing, MultiplayerScores,
    BeatmapsetDiscussionVotes, CreatePMResponse, BeatmapsetDiscussions,
    UserCompact, BeatmapsetCompact, ForumPoll, Room, RoomPlaylistItem,
    RoomPlaylistItemMod, RoomLeaderboardScore, RoomLeaderboardUserScore,
    RoomLeaderboard, Match, Matches, MatchResponse, ScoreMatchInfo, MatchGame,
    MatchEventDetail, MatchEvent, ScoringType, TeamType, StatisticsVariant)
from ossapi.enums import (GameMode, ScoreType, RankingFilter, RankingType,
    UserBeatmapType, BeatmapDiscussionPostSort, UserLookupKey,
    BeatmapsetEventType, CommentableType, CommentSort, ForumTopicSort,
    SearchMode, MultiplayerScoresSort, BeatmapsetDiscussionVote,
    BeatmapsetDiscussionVoteSort, BeatmapsetStatus, MessageType,
    BeatmapsetSearchCategory, BeatmapsetSearchMode,
    BeatmapsetSearchExplicitContent, BeatmapsetSearchLanguage,
    BeatmapsetSearchGenre, NewsPostKey, BeatmapsetSearchSort, RoomType,
    RoomCategory, RoomSearchType, MatchEventType, Variant)
from ossapi.mod import Mod
from ossapi.replay import Replay
from ossapi.encoder import ModelEncoder, serialize_model
from ossapi.ossapiv2_async import OssapiAsync

from oauthlib.oauth2 import AccessDeniedError, TokenExpiredError
from oauthlib.oauth2.rfc6749.errors import InsufficientScopeError

__version__ = metadata.version(__package__)

__all__ = [
    # OssapiV1
    "OssapiV1", "ReplayUnavailableException", "InvalidKeyException",
    "APIException",
    # OssapiV2 core
    "Ossapi", "OssapiAsync", "Grant", "Scope", "Domain",
    # OssapiV2 models
    "Beatmap", "BeatmapCompact", "BeatmapUserScore", "ForumTopicAndPosts",
    "Search", "CommentBundle", "Cursor", "Score", "BeatmapsetSearchResult",
    "ModdingHistoryEventsBundle", "User", "Rankings", "BeatmapScores",
    "KudosuHistory", "Beatmapset", "BeatmapPlaycount", "Spotlight",
    "Spotlights", "WikiPage", "_Event", "Event", "BeatmapsetDiscussionPosts",
    "Build", "ChangelogListing", "MultiplayerScores",
    "BeatmapsetDiscussionVotes", "CreatePMResponse",
    "BeatmapsetDiscussions", "UserCompact", "BeatmapsetCompact", "ForumPoll",
    "Room", "RoomPlaylistItem", "RoomPlaylistItemMod", "RoomLeaderboardScore",
    "RoomLeaderboardUserScore", "RoomLeaderboard", "Match", "Matches",
    "MatchResponse", "ScoreMatchInfo", "MatchGame", "MatchEventDetail",
    "MatchEvent", "StatisticsVariant",
    # OssapiV2 enums
    "GameMode", "ScoreType", "RankingFilter", "RankingType",
    "UserBeatmapType", "BeatmapDiscussionPostSort", "UserLookupKey",
    "BeatmapsetEventType", "CommentableType", "CommentSort", "ForumTopicSort",
    "SearchMode", "MultiplayerScoresSort", "BeatmapsetDiscussionVote",
    "BeatmapsetDiscussionVoteSort", "BeatmapsetStatus", "MessageType",
    "BeatmapsetSearchCategory", "BeatmapsetSearchMode",
    "BeatmapsetSearchExplicitContent", "BeatmapsetSearchLanguage",
    "BeatmapsetSearchGenre", "NewsPostKey", "BeatmapsetSearchSort", "RoomType",
    "RoomCategory", "RoomSearchType", "MatchEventType", "ScoringType",
    "TeamType", "Variant",
    # OssapiV2 exceptions
    "AccessDeniedError", "TokenExpiredError", "InsufficientScopeError",
    # misc
    "Mod", "Replay", "__version__", "ModelEncoder",
    "serialize_model"
]
