###This is testfile for attach to process to debug.

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import windbg3
debugger = windbg3.debugger()


pid = input("Enter the PID of the process to attach to.: ")

#attach to process
debugger.attach(int(pid))

debugger.run()    
debugger.detach()



