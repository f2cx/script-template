#!/usr/bin/env python3

import os
import click
import logging
import pendulum
import json

from dotty_dict import dotty
from pathlib import Path
from dotenv import dotenv_values

env = {
    **dotenv_values(".env"),
    **os.environ
}

#####################################################################################################
# Configuration
#####################################################################################################

LOGGER = logging.getLogger(__name__)

#####################################################################################################
# Helper Methods
#####################################################################################################

def load_config_file(file):
    return dotty(json.loads(Path(file).absolute().open().read()))

def configure_logger(verbose):
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z', level=log_level)

#####################################################################################################
# Main Methods
#####################################################################################################

@click.command()
@click.option('--config-file', type=click.Path(exists=True, file_okay=True, dir_okay=False), required=True)
@click.option('--verbose', is_flag=True)
def main(config_file, verbose):
    """Update the categories in Marketplace PIM based on FLAPIM categories."""

    configure_logger(verbose)
    config = load_config_file(config_file)
    
    name = config.get('main.name')
    ADMIN_EMAIL = env.get('ADMIN_EMAIL')

    timestamp = pendulum.now(tz='Europe/Berlin').format('YYYY-MM-DD HH:mm:ss')

    LOGGER.info(f"Environment Variable ADMIN_EMAIL: {ADMIN_EMAIL} (from .env, can be overwritten via export VAR)")
    LOGGER.debug("Verbose debug message...")
    LOGGER.info(f"Hello {name} on {timestamp}!")


#####################################################################################################
# Main
#####################################################################################################

if __name__ == "__main__":
    main()
