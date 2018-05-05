'''
Created on Mar 7, 2018

@author: nopri
'''
from com.frent.Database import Database
from com.frent.NumberGenerator import NumberGenerator
import datetime
import logging


class Queries(Database):
    '''
    class to provide query database
    '''

    logger = logging.getLogger('Queries')

    def __init__(self):
        '''
        Constructor
        '''
        super(Queries, self).__init__()
        
    def checkCancel(self, transaksi_id):
        '''
        function to check cancel transaction
        @param transaksi id: 
        @return: true = found, false not found
        '''
        sql = """SELECT cancel_id FROM trx_cancel WHERE cancel_pinjamid=%s"""
        result = self.executeSelectOne(sql, transaksi_id)
        if result is not None:
            return True
        else:
            return False
        
    def checkReturn(self, transaksi_id):
        '''
        function to check return transaction
        @param transaksi id: 
        @return: true = found, false not found
        '''
        sql = """SELECT kembali_id FROM trx_kembali WHERE kembali_pinjamid=%s"""
        result = self.executeSelectOne(sql, transaksi_id)
        if result is not None:
            return True
        else:
            return False
    
    def checkConfirmation(self, transaksi_id):
        '''
        function to check confirmation transaction
        @param transaksi id: 
        @return: true = found, false not found
        '''
        sql = """SELECT confirmation_id FROM trx_confirmation WHERE confirmation_pinjamid=%s"""
        result = self.executeSelectOne(sql, transaksi_id)
        if result is not None:
            return True
        else:
            return False
    
    def insertCancel(self, transaksi_id):
        '''
        function to insert transaction cancel
        @param transaksi id: 
        @return: true = found, false not found
        '''
        sql = """INSERT INTO trx_cancel (cancel_id,cancel_pinjamid,cancel_date,cancel_user,cancel_telp,cancel_reason) 
            VALUES(%s,%s,%s,%s,%s,%s)"""
        return self.executeParams(sql, (NumberGenerator.Genreate8(), transaksi_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'System', '-', 'Timeout'))

    def checkTransactonTimeOut(self,limit):
        '''
        function to get all transaction timeout
        @return: collection of id transaction
        '''
        sql = """SELECT trxpinjam_id FROM trx_pinjam 
                    WHERE cancel_id IS NULL
                    AND TIMESTAMPDIFF(SECOND,trxpinjam_date,CURRENT_TIMESTAMP) >%s"""
        return self.executeSelectAny(sql,limit)
    
    def getSetting(self,name):
        '''
        function to get parameters setting
        @return: collection of id transaction
        '''
        sql = """SELECT setting_nama,setting_value FROM web_setting
                    WHERE setting_nama=%s"""
        return self.executeSelectOne(sql, name);

        
q = Queries()
# q.setup_logging()
q.logger.info('Check.')
# print(q.checkCancel('PRDUIWD8'))
# print(q.checkConfirmation('PRDUIWD8'))
# print(q.checkReturn('T7P42EP0x'))
# print(NumberGenerator.Genreate8())
