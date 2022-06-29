# ------------------------------------------ PATHS
PRJ_DIR := $(realpath .)

# ------------------------------ add folder docs file path here
# ------------------------------ add folder scripts file path here
DIR_SCRIPTS			:= $(PRJ_DIR)/scripts
# ------------------------------ add folder src file path here
DIR_SRC				:= $(PRJ_DIR)/src
# ------------------------------ add folder results file path here

# ------------------------------------------ VARIABLES
# SHELL       := /bin/bash

# python script flags
RHTML		= 
PRINTCOV	= 0
COLNAME		= Toggle
KEYWORD		= No

EXCEL		= 0
CSV			= 0
HTML		= 1
JSON		= 0
TEXT		= 1

VERBOSE		= 0
DEBUG		= 0

# ------------------------------------------ TARGETS
default: help


setupvenv:
	clear
	@ echo -------------------- Creating Python Virtual Environment -------------------
	@ echo " "
	@ bash ${DIR_SCRIPTS}/setup_pyvenv.sh
	@ echo ------------------------------------ DONE ----------------------------------
	@ echo " "

readcov:
	clear
	@ echo " "
	@ echo ---------------------------- Coverage Extractor ----------------------------
	@ python3 $(DIR_SRC)/main.py \
	-rhtml $(RHTML) \
	--print_cov $(PRINTCOV) \
	--col_name $(COLNAME) --keyword $(KEYWORD) \
	-excel $(EXCEL) -csv $(CSV) -html $(HTML) -json $(JSON) -text $(TEXT) \
	-d $(DEBUG) -v $(VERBOSE)
	@ echo ------------------------------------ DONE ----------------------------------
	@ echo " "

cleanvenv:
	@ echo ------------------- Deleting Python Virtual Environment/s ------------------
	@ echo " "
	@ rm -rf .py* .venv*
	@ echo ------------------------------------ DONE ----------------------------------

cleanxlsx:
	@ echo -------------------------- Deleting all XLSX files -------------------------
	@ rm -rf *.xlsx
	@ echo ------------------------------------ DONE ----------------------------------

cleancsv:
	@ echo -------------------------- Deleting all CSV files --------------------------
	@ rm -rf *.csv
	@ echo ------------------------------------ DONE ----------------------------------

cleanhtml:
	@ echo -------------------------- Deleting all HTML files --------------------------
	@ rm -rf *.html
	@ echo ------------------------------------ DONE ----------------------------------

cleanjson:
	@ echo -------------------------- Deleting all json files --------------------------
	@ rm -rf *.json
	@ echo ------------------------------------ DONE ----------------------------------

cleantxt:
	@ echo -------------------------- Deleting all json files --------------------------
	@ rm -rf *.txt
	@ echo ------------------------------------ DONE ----------------------------------

cleanlogs:
	@ echo -------------------------- Deleting all log files --------------------------
	@ rm -rf *.log !(requirements.txt)
	@ echo ------------------------------------ DONE ----------------------------------

cleandumpfiles: cleanxlsx cleancsv cleanhtml cleanjson cleanlogs cleantxt

deepclean:
	clear
	@ echo ------------------------- Deep Cleaning Environment ------------------------
	@ echo " "
	@ make cleanvenv 
	@ make cleandumpfiles
	@ echo ------------------------------------ DONE ----------------------------------
	@ echo " "

help:
	clear
	@ echo " "
	@ echo ---------------------------- Targets in Makefile ---------------------------
	@ echo ----------------------------------------------------------------------------
	@ echo " "
	@ echo " setupvenv:		create a virtual environemnt with all necessary dependencies"
	@ echo " readcov:		generate a coverage report"
	@ echo " "
	@ echo " cleanvenv:		remove the virtual env"
	@ echo " cleanxlsx:		remove all .xlsx files"
	@ echo " cleancsv:		remove all .csv files"
	@ echo " cleanhtml:		remove all .html files"
	@ echo " cleanjson:		remove all .json files"
	@ echo " cleantxt:		remove all .txt files"
	@ echo " cleanlogs:		remove all .log files"
	@ echo " cleandumpfiles:	runs targets cleanxlsx cleancsv cleanhtml cleanjson cleanlogs"
	@ echo " "
	@ echo " deepclean:		delete everything (cleandumpfiles + cleanvenv)"
	@ echo " "
	@ echo " help:			humble people ask for help :)"
	@ echo ----------------------------------------------------------------------------
	@ echo " "
