import logging
from logging.config import fileConfig

from pkg_resources import resource_filename

fileConfig(
    fname=resource_filename("src", "logger.cfg"),
    disable_existing_loggers=False,
    defaults={
        "serving_service_level": "DEBUG",
        "serving_service_formatter": "classic",
    },
)

logger = logging.getLogger("serving_service")
