import imp
import pandas as pd
import logging
import argparse
import os
import re

os.system('clear')

# ===========================================================================================
# ======================================= Begin Class =======================================
# ===========================================================================================

class coverageExtractor:
    # ----------------------------------------------------------------- Variables
    # public vars
    # protected vars
    # private vars
    
    # ----------------------------------------------------------------- Functions
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, filename='ExclusionGenerator.log',
                    format='%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(lineno)d | %(message)s')
    
    


# ===========================================================================================
# ======================================== End Class ========================================
# ===========================================================================================