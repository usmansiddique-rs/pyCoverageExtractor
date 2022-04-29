from tabulate import tabulate
import pandas as pd
import logging
import os
import re
os.system('clear')

# ===========================================================================================
# ======================================= Begin Class =======================================
# ===========================================================================================

class coverageExtractor:
    # ----------------------------------------------------------------- Variables
    # public vars
    htmlFilePath = str()
    htmlFileName = str()
    # protected vars
    _covTablesDF = str()
    # private vars
    
    # ----------------------------------------------------------------- Functions
    def __init__(self):
        # public vars
        self.htmlFilePath = ''
        self.htmlFileName = ''
        # protected vars
        self._covTablesDF = ''
        # private vars
        
        
        logging.basicConfig(level=logging.DEBUG, filename='coverageExtractor.log',
                            format='%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(lineno)d | %(message)s')
    
    
    # read coverage HTML file
    def readHTML(self):
        self._covTablesDF = pd.read_html(self.htmlFilePath,header=[0])
        logging.info('Total tables in HTML doc = ' + str(len(self._covTablesDF)))
        for i in range(len(self._covTablesDF)):
            logging.info('Table[' + str(i) + '] col ' + str(self._covTablesDF[i].columns))
    
    
    # print a table from excel or html file
    def displayDF(self,dataFrame):
        print(tabulate(dataFrame,headers='keys',tablefmt='github'))


# ===========================================================================================
# ======================================== End Class ========================================
# ===========================================================================================