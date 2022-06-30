from tabulate import tabulate
from csv import writer
import pandas as pd
import logging
import enum
import os

# ===========================================================================================
# ======================================= Begin Class =======================================
# ===========================================================================================

class coverageExtractor:
    # ----------------------------------------------------------------- Variables
    def __init__(self):
        # public vars
        self.htmlFilePath   = str()
        self.htmlFileName   = str()
        self.xlsxFileName   = str()
        self.txtFilePath    = str()
        self.txtFileName    = str()
        # protected vars
        self._covTablesDF = str()
        self._isolatedDfObj = pd.DataFrame
        self._updatePath = str()
        self._signalPath = str()
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
        # print(tabulate(dataFrame,headers='keys',tablefmt='github'))
        print(dataFrame)
    
    
    # print and save data to Excel sheet
    def writeCovtoXlsx(self):
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
    
    
    # print and save data to txt doc
    def writeCovtoTxt(self):
        #  create folder if it doesnt exist
        self.txtFilePath = 'CovRpt_' + self.htmlFileName.replace('.html','')
        if os.path.exists(self.txtFilePath) is False:
            os.mkdir(self.txtFilePath)
        # write to file
        for index, item in enumerate(self._covTablesDF):
            # create file name
            tempFileName = 'CovRpt_' + self.htmlFileName.replace('.html','') + 'Table_' + str(index) + '.txt'
            pwd = os.getcwd()
            tempFilePath = os.path.join(pwd+'/',self.txtFilePath+'/',tempFileName)
            # create empty file
            open(tempFilePath,'w').close()
            # save to txt
            tempTable = pd.DataFrame(item)
            tempTable.to_csv(tempFilePath,index=False,header=True,sep=' ',mode='w')
    
    
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
    
    
    def getSignalPath(self):
        # print(self._covTablesDF[1])
        # get path name from cov table 1
        self._signalPath = self._covTablesDF[1].loc[0]['NAME']
        logging.info('Current Signal Path: {}'.format(self._signalPath))
        # self._updatePath = input('Update Signal Path (Press Y/N): ')
        # if self._updatePath is 'y' or self._updatePath is 'Y':
        #     self._signalPath = input('New Signal Path: ')
        #     logging.info('Updated Signal Path: {}'.format(self._signalPath))
    
    
    def addColCovTable(self):
        # insert col 0
        self._isolatedDfObj.insert(0,"IP","")
        # insert col 1
        self._isolatedDfObj.insert(1,"Signal Path",self._signalPath)
        # rename col 2
        self._isolatedDfObj.rename(columns={"Name":"Signal Name"},inplace=True)
        # insert col 3
        self._isolatedDfObj.insert(3,"Bits Index Not Covered","")
        # insert col 9
        self._isolatedDfObj["Should be Excluded (Y/N)"] = ""
        # insert col 10
        self._isolatedDfObj["Test Name"] = ""
        # insert col 11
        self._isolatedDfObj["Test Description"] = ""
        # insert col 12
        self._isolatedDfObj["Reason for Exclusion"] = ""
        # insert col 13
        self._isolatedDfObj["Reference"] = ""
        # insert col 14
        self._isolatedDfObj["Comments"] = ""
    
    
    def writeTabletoXlsx(self):
        # set filename
        fileName = 'updated_' + self.htmlFileName.replace('.html','.xlsx')
        # save table to excel
        writer = pd.ExcelWriter(fileName,engine='xlsxwriter')
        writer.save()
        excelFileData = pd.ExcelWriter(fileName,mode='a',if_sheet_exists='replace',engine='openpyxl')
        self._isolatedDfObj.to_excel(excelFileData,index=False)
        excelFileData.save()
    
    
    def writeTabletoCsv(self):
        fileName = 'updated_' + self.htmlFileName.replace('.html','.csv')
        self._isolatedDfObj.to_csv(fileName,index=False)
    
    
    def writeTabletoHtml(self):
        fileName = 'updated_' + self.htmlFileName
        self._isolatedDfObj.to_html(fileName)
    
    
    def writeTabletoJson(self):
        fileName = 'updated_' + self.htmlFileName.replace('.html','.json')
        self._isolatedDfObj.to_json(fileName,orient='index',indent=4)
    
    
    def writeTabletoTxt(self,tbfmt):
        fileName = 'updated_' + self.htmlFileName.replace('.html','.txt')
        myTable = tabulate(self._isolatedDfObj,headers='keys',tablefmt=tbfmt,colalign="right")
        with open(fileName,'w') as f:
            f.write(myTable)

# ===========================================================================================
# ======================================== End Class ========================================
# ===========================================================================================