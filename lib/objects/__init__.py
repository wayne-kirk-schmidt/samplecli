import os
import glob
import sys
sys.dont_write_bytecode = True
currentdir = os.path.dirname(os.path.abspath(__file__))
targets = ['py']
filelist = [fn for fn in os.listdir(currentdir) if not os.path.basename(fn).startswith('__')]
filelist = [os.path.splitext(x)[0] for x in filelist]
__all__ = filelist  
