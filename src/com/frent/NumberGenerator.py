'''
Created on Mar 7, 2018

@author: nopri
'''
import random, string

class NumberGenerator:
    '''
    class provide function to genreate number
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def Genreate8():
        '''
        function to genreate 8 digit alfanumeric
        @return: string value
        '''
        x = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
        return x.upper()
            