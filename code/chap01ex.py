"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
               dat_file='2002FemResp.dat.gz',
               nrows=None):
    """ Reads 2002FemResp data.
    
    dct_file: string file name
    dat_file: string file name
    
    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df

def ValidatePregnum(resp):
    """ Validate Pregnum in the respondent file.
    
    resp: respondent DataFrame
    """
    
    # Read the pregnancy data frame
    preg = ReadFemPreg()
    
    # Create the dictionary
    pregmap = MakePregMap(preg)

        


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
