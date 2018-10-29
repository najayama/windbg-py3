c_structure = """    WORD   ControlWord;
    WORD   StatusWord;
    BYTE  TagWord;
    BYTE  Reserved1;
    WORD   ErrorOpcode;
    DWORD ErrorOffset;
    WORD   ErrorSelector;
    WORD   Reserved2;
    DWORD DataOffset;
    WORD   DataSelector;
    WORD   Reserved3;
    DWORD MxCsr;
    DWORD MxCsr_Mask;
    M128A FloatRegisters[8];"""

ctypelist = c_structure.split("\n")

result_str = ""

for i in ctypelist:
    tmplist = []
    for j in i.split(" "):
        
        if j:
            tmplist.append(j)
            
    result_str  += '("' + tmplist[1][0:-1]+ '", '+ tmplist[0] + "),\n"
        
        
print(result_str)


            
            
