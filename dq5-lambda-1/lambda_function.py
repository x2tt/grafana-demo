import random
import logging
import time
import snowflake.connector

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    print('dq5-lambda-1 Lambda invoked')
    if random.random() < 0.5:
        rowsLoaded = random.randrange(1, 21)
        time.sleep(rowsLoaded)
        logger.info({ 'rowsLoaded': rowsLoaded })
        logger.info('dq5-lambda-1 Lambda ran successfully')
    else:
        logger.error('dq5-lambda-1 Lambda failed')
