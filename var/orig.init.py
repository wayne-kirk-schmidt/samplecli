import sys
sys.dont_write_bytecode = True
import os
folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for dirpath, dirs, files in os.walk(folder):
    sys.path.append(os.path.abspath(dirpath))
import lib
