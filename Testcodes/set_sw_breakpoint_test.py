###This is testfile for setting breakpoint.
###!!! CHANGE SETTINGS before you use.
##    EXE_PATH: path to your debuggy.(for example, "C:\\python36\\python.exe")
##    CMD_PARAMS: command line parameter for 



import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import windbg3
debugger = windbg3.debugger()

#path to python executable (for example, "C:\\python36\\python.exe")
EXE_PATH = os.path.join(os.path.dirname(sys.path[1]), "python.exe")

#create process
CMD_PARAMS = os.path.join(os.path.dirname(__file__), "printf_loop.py")
debugger.load(EXE_PATH, "printf_loop.py")


#Set breakporint to address of printf and run process.
printf_address = debugger.func_resolve("msvcrt.dll", "printf")
if printf_address is None:
    sys.exit()

print("[*] Address of printf: {:016x}".format(printf_address))

#Read 8 bytes from printf_address
address_data = debugger.read_process_memory(printf_address, 8)
if not address_data:
    print("Can't read process memory at: {:016x}".format(printf_address))
    sys.exit()
    
print("{}".format(address_data))
    

if not debugger.bp_set_sw(printf_address):
    print("Can't set breakpoint....")
    sys.exit()

#Read 8 bytes from printf_address. (First bytes must be \xcc....)
address_data = debugger.read_process_memory(printf_address, 8)
print("{}".format(address_data))




debugger.run()
    
debugger.detach()



