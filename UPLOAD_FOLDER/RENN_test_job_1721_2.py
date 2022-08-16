'''
easypy RENN_test_job_1721_2.py -testbed renn_testbed_9300_stack.yaml
'''

import os,sys
import logging
import argparse
from ats.easypy import run
from ats.datastructures.logic import And, Or, Not
from ats.topology import loader

testbed = loader.load('renn_testbed_9300_stack.yaml')

def main():
    ''' '''

    testscript='RENN_main1_1721.py'

    run(testscript=testscript,datafile = 'RENN_test_job_1721_datafile.yaml')
