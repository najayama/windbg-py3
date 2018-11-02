###This is testfile for setting breakpoint.

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import windbg3
debugger = windbg3.debugger()


#attach to process
pid = input("Enter the PID of the process to attach to.: ")
debugger.attach(int(pid))



#Set breakporint to address of printf and run process.
printf_address = debugger.func_resolve("msvcrt.dll", "printf")
if printf_address is None:
    sys.exit()

print("[*] Address of printf: 0x{:08x}".format(printf_address))
debugger.bp_set_sw(printf_address)


debugger.run()
    
debugger.detach()



