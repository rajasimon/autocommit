import argparse
import logging
import sys

logger = logging.getLogger(__name__)


class CommandLineInterface(object):
    
    @classmethod
    def entrypoint(cls):
        """
        Main entrypoint for external starts
        """
        cls().run()

    def run(self):
        """
        Starting git autocommit
        """
        # Setup logging
        logging.basicConfig(
            level={
                0: logging.WARN,
                1: logging.INFO,
                2: logging.DEBUG,
            }[2],
            format="%(asctime)-15s %(levelname)-8s %(message)s",
        )
        logger.info("Welcome to autocommit...")
