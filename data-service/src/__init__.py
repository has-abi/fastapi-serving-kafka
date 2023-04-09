import logging
from logging.config import fileConfig

from pkg_resources import resource_filename

fileConfig(
    fname=resource_filename("src", "logger.cfg"),
    disable_existing_loggers=False,
    defaults={
        "data_service_level": "DEBUG",
        "data_service_formatter": "classic",
    },
)

logger = logging.getLogger("data_service")
