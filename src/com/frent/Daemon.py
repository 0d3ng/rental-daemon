'''
Created on Mar 6, 2018

@author: nopri
'''

from com.frent.Queries import Queries
from com.frent.LogUtil import LogUtil
import logging

class Daemon:
    '''
    class to handling transaction
    '''

    logger = logging.getLogger('Daemon')

    def __init__(self):
        '''
        Constructor
        '''
            
if __name__ == '__main__':
    LogUtil.setup_logging()
    d = Daemon()
    d.logger.info("Starting application")
    q = Queries()
    #Get time limit after transaction
    setting = q.getSetting("time_limit")
    if setting is None:
        d.logger.info("No time_limit Found")
    else:
        #check transaction limit base on limit time(hour)
        limit = int(setting['setting_value'])*3600
        d.logger.info(setting)
        result = q.checkTransactonTimeOut(limit)
        if result is None:
            d.logger.info("No Data")
        else:
            d.logger.info(result)
            for res in result:
                trx_id = res['trxpinjam_id']
                status = q.insertCancel(trx_id)
                if status:
                    d.logger.info("Success")
                else:
                    d.logger.info("Fail")
