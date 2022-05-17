# from numpy import cov
import coverageExtactor
import argparse
import logging
import os
os.system('clear')


def main():
    # setup arguments
    parser = argparse.ArgumentParser(prog='coverage_extractor',
                                    usage='%(prog)s [options] path',
                                    description='Extract data from Synopsys Coverage Reports',
                                    epilog='Happy coding ! Eat, Sleep, Code, Repeat')
    # list of all possible args for coverage extractor
    parser.add_argument('-rhtml','--readhtml',
                        type=str,metavar='',required=True,help='provide PATH of HTML coverage file')
    parser.add_argument('--print_cov',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print original coverage report in XLSX')
    parser.add_argument('-col','--col_name',
                        type=str,metavar='',required=True,help='provide column heading to read')
    parser.add_argument('-key','--keyword',
                        type=str,metavar='',required=True,help='provide value of specific column')
    parser.add_argument('-excel',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print table as XLSX doc')
    parser.add_argument('-csv',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print table as CSV doc')
    parser.add_argument('-html',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print table as HTML doc')
    parser.add_argument('-json',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print table as JSON doc')
    parser.add_argument('-text',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print table as TXT doc')
    parser.add_argument('-v','--verbose',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print verbose')
    parser.add_argument('-d','--debug',
                        type=int,default=0,metavar='',required=False,nargs='?',help='print debugging')
    myargs = parser.parse_args()
    
    # create class object
    covext = coverageExtactor.coverageExtractor()
    # set URL and get HTML file name
    if myargs.readhtml:
        covext.htmlFilePath = myargs.readhtml
        covext.htmlFileName = os.path.basename(covext.htmlFilePath)
        logging.info('HTML Coverage File Dir:    ' + covext.htmlFilePath)
        logging.info('HTML Coverage File Name:   ' + covext.htmlFileName)
    # read tables from html file
    covext.readHTML()
    # display tables read from coverage report as prompt
    if myargs.verbose:
        for i in range(len(covext._covTablesDF)):
            print('================================= Coverage Table [{:2d}] ================================='.format(i))
            covext.displayDF(covext._covTablesDF[i])
            print('==========================================================================================')
            print('\n')
    # print original coverage report as excel doc
    if myargs.print_cov:
        covext.writeCovtoXlsx()
    # find specific signals via col name and values and save them in df
    if myargs.col_name and myargs.keyword:
        covext.readCoverageTable(columnName=myargs.col_name,keyword=myargs.keyword)
        # find the signal hierarchical path 
        covext.getSignalPath()
        # modify the isolated signal table
        covext.addColCovTable()
        # display the extracted signal table
        if myargs.debug:
            print('\nPrinting isolated rows from table\n')
            covext.displayDF(covext._isolatedDfObj)
        # print isolated signal table as excel
        if myargs.excel:
            covext.writeTabletoXlsx()
        # print isolated signal table as csv
        if myargs.csv:
            covext.writeTabletoCsv()
        # print isolated signal table as html
        if myargs.html:
            covext.writeTabletoHtml()
        # print isolated signal table as json
        if myargs.json:
            covext.writeTabletoJson()
        # print isolated signal table as txt
        if myargs.text:
            # possible formats: github, presto, 
            covext.writeTabletoTxt(tbfmt='presto')


if __name__ == '__main__':
    main()