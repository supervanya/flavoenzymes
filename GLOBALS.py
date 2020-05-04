DEBUG = True
USE_CACHING = True
FILE_LOGGING_ENABLED = True

# less_verbose <---- 'none' | 'success' | 'error' | 'warning' | 'info' | 'debug' | 'silly' ----> more_verbose
VERBOSITY = (
    "info"  # set to 'none' to have almost no output, set to 'silly' for most verbosity
)

KEYWORDS = [
    "FAD",
    "FMN",
    "flavin",
    "flavoenzyme",
    "flavo enzyme",
    "flavo",
    "flavoprotein",
    "flavo protein",
]
# KEYWORDS = ["flavoenzyme"]  # TODO: very important, make sure this is removed!
