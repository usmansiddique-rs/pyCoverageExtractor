from csv import writer
import enum
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
    def __init__(self):
        # public vars
        self.htmlFilePath = str()
        self.htmlFileName = str()
        self.xlsxFileName = str()
        # protected vars
        self._covTablesDF = str()
        self._isolatedDfObj = pd.DataFrame
        # private vars
    
    
    # ----------------------------------------------------------------- Functions
        logging.basicConfig(level=logging.DEBUG, filename='coverageExtractor.log',
                            format='%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(lineno)d | %(message)s')
    
    
    # read coverage HTML file
    def readHTML(self):
        self._covTablesDF = pd.read_html(self.htmlFilePath,header=[0])
        logging.info('Total tables in HTML doc = ' + str(len(self._covTablesDF)))
        for i in range(len(self._covTablesDF)):
            logging.info('Table "{}" columns: "{}"'.format(i,str(self._covTablesDF[i].columns)))
            # logging.info('Table[' + str(i) + '] col ' + str(self._covTablesDF[i].columns))
    
    
    # print a table from excel or html file
    def displayDF(self,dataFrame):
        print(tabulate(dataFrame,headers='keys',tablefmt='github'))
    
    
    # print and save data to Excel sheet
    def writeDFtoXlsx(self):
        # create file name
        self.xlsxFileName = 'CovRpt_' + self.htmlFileName.replace('.html','.xlsx')
        # create empty file
        writer = pd.ExcelWriter(self.xlsxFileName,engine='xlsxwriter')
        writer.save()
        for index, item in enumerate(self._covTablesDF):
            tempTable = pd.DataFrame(item)
            # writing to excel
            # excelFileData = pd.ExcelWriter(self.xlsxFileName,mode='a',if_sheet_exists='new')
            excelFileData = pd.ExcelWriter(self.xlsxFileName,mode='a',if_sheet_exists='replace',engine='openpyxl')
            # write dataframe to excel
            tempSheetName = 'Cov Table ' + str(index)
            tempTable.to_excel(excelFileData,sheet_name=tempSheetName,index=False)
            # save to excel
            excelFileData.save()
            logging.info('Added Table "{}" as Sheet "{}" in doc "{}"'.format(index,tempSheetName,self.xlsxFileName))
    
    
    def readCoverageTable(self,columnName,keyword):
        # iterate through all dataframes
        for index, table in enumerate(self._covTablesDF):
            # find table with specific column name
            if columnName in table:
                # self.displayDF(table)
                logging.info('FOUND column heading "{}" in "Cov Table {}"'.format(columnName,index))
                # append column names to new data frame
                logging.info('Table column headings "{}"'.format(table.columns))
                self._isolatedDfObj = pd.DataFrame(columns=table.columns)
                # find rows with specific column value (string)
                tempRow = table.loc[table[columnName] == keyword]
                # find rows with specific column value (array)
                # tempRow = table.loc[table[columnName].isin(keyword)]
                # append tempRow to new data frame
                self._isolatedDfObj = self._isolatedDfObj.append(tempRow)
                # print('/////////////////////////////////////////////////////////////////////////////')
                # self.displayDF(self._isolatedDfObj)


# ===========================================================================================
# ======================================== End Class ========================================
# ===========================================================================================