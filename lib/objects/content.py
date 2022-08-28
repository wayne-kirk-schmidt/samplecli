import os
import sys
sys.dont_write_bytecode = True
targetname = os.path.splitext(os.path.basename(__file__))[0]
dirname = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
attribute = '%s::%s' % ( dirname.upper(), targetname )
def debug():
    print(attribute)
