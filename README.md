# pyCoverageExtractor
This repository allows you to read coverage reports (`.html`) and extract specific information from them in various formats including (`.csv`,`.xlsx`,`.json`,`.html`).

## How to Setup
Simply run the command `make setupvenv` to create a python virtual environment for your project. 
You only need to create the virtual environment once. Make sure to **activate** it before running your code and **deactivate** it once done.  
-   Activate vir env: `source .pyvenv/bin/activate`
-   Deactivate vir env: `deactivate`

To learn more about what are virtual environemnts click [here](https://realpython.com/python-virtual-environments-a-primer/).

## How to Run
-   To view all possible targets and what they do run `make help`.
-   To generate isolated port list from coverage report run the following command:
    ```bash
    make readcov \
    RHTML=file.html \       # path to .html coverage report file
    PRINTCOV=1/0 \          # print original coverage report in .xlsx format
    COLNAME=Toggle \        # Read value from this column (Default value = Toggle)
    KEYWORD=No \            # Extract this value (Default value = No)
    EXCEL=1/0 \             # Generate extracted values as .xlsx
    CSV=1/0 \               # Generate extracted values as .csv
    HTML=1/0 \              # Generate extracted values as .html (Default output)
    JSON=1/0 \              # Generate extracted values as .json
    VERBOSE=1/0 \           # Set/Unset verbosity mode        
    DEBUG=1/0               # Set/Unset debugging mode
    ``` 