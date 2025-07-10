import logging

class log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\nopcommerce.log",
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )
        #diffrent methods in logger object
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
#adding a custom logger file in utilltes
