###This is test to create new process to debug.

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import my_debugger
debugger = my_debugger.debugger()


debugger.load("C:\\WINDOWS\\System32\\calc.exe")