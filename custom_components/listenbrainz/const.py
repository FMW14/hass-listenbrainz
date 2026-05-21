"""Constants for listenbrainz."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "ListenBrainz"
DOMAIN = "listenbrainz"
CONF_API_URL = "api_url"
ATTRIBUTION = "Listening data from ListenBrainz.org"
