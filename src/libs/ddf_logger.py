##This file is for logging settings.

import logging
#from RETS_Manager.settings import DEV

LOG_FILENAME='ddf_client.log'

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(filename)- 15s:%(lineno)-4s %(funcName)-30s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%S')


logging.basicConfig(format='%(asctime)s.%(msecs)03d %(filename)- 15s:%(lineno)-4s %(funcName)-30s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)