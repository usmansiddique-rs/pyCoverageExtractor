# ------------------------------------------ PATHS
PRJ_DIR := $(realpath .)

# ------------------------------ add folder docs file path here
# ------------------------------ add folder scripts file path here
DIR_SCRIPTS			:= $(PRJ_DIR)/scripts
# ------------------------------ add folder src file path here
# ------------------------------ add folder results file path here

# ------------------------------------------ VARIABLES


# ------------------------------------------ TARGETS

setupvenv:
	clear
	@ echo -------------------- Creating Python Virtual Environment -------------------
	@ echo " "
	@ bash ${DIR_SCRIPTS}/setup_pyvenv.sh
	@ echo ------------------------------------ DONE ----------------------------------
	@ echo " "