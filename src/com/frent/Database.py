'''
Created on Mar 6, 2018

@author: nopri
'''
import pymysql
import logging

class Database:
    '''
    class database to handling connection
    '''

    logger = logging.getLogger('Database')

    __host = '127.0.0.1'
    __user = 'root'
    __password = ''
    __db = 'e_rental'
    __connection = None
    __cursor = None

    def __init__(self):
        '''
        Constructor
        '''
        try:
            self.__connection = pymysql.connect(host=self.__host, user=self.__user, password=self.__password, db=self.__db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            self.__cursor = self.__connection.cursor();
            self.logger.info('Connection success')
        except Exception as e:
            self.logger.error(e)
    
    def __del__(self):
        try:
            if self.__connection is None:
                self.logger.info('cannot close because connection NULL')
                pass
            else:
                self.__connection.close()
        except Exception as e:
            self.logger.error(e)   

    def __commit(self):
        '''
        commit transaction
        ''' 
        try:
            self.__connection.commit()
            return True
        except Exception as e:
            self.logger.error(e)
        return False

    def roolback(self):
        '''
        roolback transaction
        '''
        try:
            self.__connection.rollback()
            return True
        except Exception as e:
            self.logger.error(e)
        return False            

    def setAutoCommit(self, autoCommit):
        '''
        to set autocommit
        @param autocommit: True if autocommit true, False if autocommit false
        @type bool: True and False
        '''
        try:
            self.__connection.autocommit(autoCommit)
            return True
        except Exception as e:
            self.logger.error(e)
        return False
            
    def execute(self, query):
        '''
        to execute query(insert, update, delete)
        @param query: query to database
        @type string: string value
        '''
        try:
            self.__cursor.execute(query)
            return True
        except Exception as e:
            self.logger.error(e)   
        return False
        
    def executeParams(self, query, params):
        '''
        to execute insert query using data parameters
        @param query: query to database
        @param params: data to query 
        @type string: string value
        '''
        try:
            self.__cursor.execute(query, params)
            self.__commit()
            return True
        except Exception as e:
            self.logger.error(e)   
        return False 
        
    def executeSelectAny(self, query,param):
        '''
        to execute query select
        @param query: query to database
        @type string: string value
        @return: results of data
        '''
        try:
            self.__cursor.execute(query,param)
            result = self.__cursor.fetchall()
            return result
        except Exception as e:
            self.logger.error(e)   
        return None
        
    def executeSelectAll(self, query):
        '''
        to execute query select
        @type string: string value
        @return: results of data
        '''
        try:
            self.__cursor.execute(query)
            result = self.__cursor.fetchall()
            return result
        except Exception as e:
            self.logger.error(e)   
        return None
        
    def executeSelectOne(self, query,param):
        '''
        to execute query select
        @param query: query to database
        @type string: string value
        @return: result one of data
        '''
        try:
            self.__cursor.execute(query,param)
            result = self.__cursor.fetchone()
            return result
        except Exception as e:
            self.logger.error(e)   
        return None
        
# db = Database()
if __name__ == '__main__':
    db = Database()
#     db.execute('SELECT NOW()')
    
    
