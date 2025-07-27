import logging

class LogMaker:
    @staticmethod
    def create_log():
        logging.basicConfig(filename=".\\logs\\nopcommerce.log",
                            format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                            datefmt = '%Y-%m-%d %H:%M:%S',
                            force=True
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger