import logging

class log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\nopcommerce.log",
            format='%(pastime)s:%(levelness)s:%(message)s',
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )