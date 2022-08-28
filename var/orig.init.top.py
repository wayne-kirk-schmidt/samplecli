import os
import glob
import sys
sys.dont_write_bytecode = True

startdir = os.path.abspath(os.path.dirname(__file__))
startlib = os.path.join(startdir, 'lib')

startlibsubdirs = [f.path for f in os.scandir(startlib) if f.is_dir() ]    
targetliblist = ( startlib, startlibsubdirs )

for targetlib in targetliblist:
    sys.path.append(targetlib)

import lib
