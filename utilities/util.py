
import pytest
import logging


class Logger:

    def generate_logs(self, level, message):
        """ 
            Levels\n
            1 = Critical\n
            2 = Error\n
            3 = Warning\n
            4 = Info\n
            5 = Debug\n
        """

        logging.basicConfig(filename="mylogs.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                    )

        logging.basicConfig(filename='mylogs.log')
        logging.getLogger().setLevel(logging.INFO)


