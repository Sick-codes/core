"""Constants used by Photos.network core."""
MAJOR_VERSION = 0
MINOR_VERSION = 1
PATCH_VERSION = 0
__short_version__ = f"{MAJOR_VERSION}.{MINOR_VERSION}"
__version__ = f"{__short_version__}.{PATCH_VERSION}"
REQUIRED_PYTHON_VER = (3, 7, 1)

# The exit code to send to request a restart
RESTART_EXIT_CODE = 100

DEVICE_DEFAULT_NAME = "Unnamed Device"

URL_API = "/api/"

CONF_ACCESS_TOKEN = "access_token"
CONF_ADDRESS = "address"
CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
CORE_VERSION = __version__
