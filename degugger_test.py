import my_debugger
import sys
debugger = my_debugger.debugger()


###load test
#debugger.load("C:\\WINDOWS\\System32\\calc.exe")

###attach test
pid = input("Enter the PID of the process to attach to.: ")

debugger.attach(int(pid))



###Software breakpoints test. set breakporint to address of pritnf and run process.
printf_address = debugger.func_resolve("msvcrt.dll", "printf")
if printf_address is None:
    sys.exit()

print("[*] Address of printf: 0x{:08x}".format(printf_address))
debugger.bp_set_sw(printf_address)






debugger.run()




###Read Thread Context test.
#thread_list = debugger.enumurate_threads()
#print(thread_list)


#for thread in thread_list:

       #thread_context = debugger.get_thread_context(thread)
       
       #if thread_context.Rbp >= thread_context.Rsp:
              #print("[*] Dumping registers for thread ID: 0x%08x" % thread)
              #print("[**] EIP: 0x%x" % thread_context.Rip)
              #print("[**] ESP: 0x%x" % thread_context.Rsp)
              #print("[**] EBP: 0x%x" % thread_context.Rbp)
              #print("[**] EAX: 0x%x" % thread_context.Rax)
              #print("[**] EBX: 0x%x" % thread_context.Rbx)
              #print("[**] ECX: 0x%x" % thread_context.Rcx)
              #print("[**] EDX: 0x%x" % thread_context.Rdx)
              #print("[*] END DUMP")
          
              

    
debugger.detach()



