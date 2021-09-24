import logging
import random
import time

import snowflake.connector

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    print('dq5-lambda-1 Lambda invoked')
    if random.random() < 0.5:
        rowsLoaded = random.randrange(1, 21)
        con = snowflake.connector.connect(
            user='k',
            password='Y9h3#Ejg#MgU75(C',
            account='zq85670.ap-southeast-2',
            warehouse='COMPUTE_WH',
            database='DQ5_DB_1',
            schema='SYSADMIN',
        )
        try:
            con.cursor().execute("INSERT INTO DQ5_DESTINATION_TABLE_1 VALUES('test')")
            con.commit()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            con.close()
        time.sleep(rowsLoaded)
        logger.info({'rowsLoaded': rowsLoaded})
        logger.info('dq5-lambda-1 Lambda ran successfully')
    else:
        logger.error('dq5-lambda-1 Lambda failed')