# ------------------------------------------ PATHS
PRJ_DIR := $(realpath .)

# ------------------------------ add folder docs file path here
# ------------------------------ add folder scripts file path here
DIR_SCRIPTS			:= $(PRJ_DIR)/scripts
# ------------------------------ add folder src file path here
DIR_SRC				:= $(PRJ_DIR)/src
# ------------------------------ add folder results file path here

# ------------------------------------------ VARIABLES


# ------------------------------------------ TARGETS
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

VERBOSE		= 0
DEBUG		= 0

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
	-excel $(EXCEL) -csv $(CSV) -html $(HTML) -json $(JSON) \
	-d $(DEBUG) -v $(VERBOSE)
	@ echo ------------------------------------ DONE ----------------------------------
	@ echo " "

cleanvenv:
	@ echo ------------------- Deleting Python Virtual Environment/s ------------------
	@ echo " "
	@ rm -rf .pyvenv
	@ echo ------------------------------------ DONE ----------------------------------

cleanxlsx:
	@ echo -------------------------- Deleting all XLSX files -------------------------
	@ echo " "
	@ rm -rf *.xlsx
	@ echo ------------------------------------ DONE ----------------------------------

cleanlogs:
	@ echo -------------------------- Deleting all log files --------------------------
	@ echo " "
	@ rm -rf *.log
	@ echo ------------------------------------ DONE ----------------------------------

cleandumpfiles: cleanxlsx cleanlogs

deepclean:
	clear
	@ echo ------------------------- Deep Cleaning Environment ------------------------
	@ echo " "
	@ make cleanvenv 
	@ make cleanxlsx
	@ make cleanlogs
	@ echo ------------------------------------ DONE ----------------------------------
	@ echo " "