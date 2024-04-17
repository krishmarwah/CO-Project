def sext(imm):
    size=len(imm)
    if imm[0] == '1':
        return '1'*(32-size) + imm
    else:
        return '0'*(32-size) + imm
def int_to_binary(n):
    if n == 0:
        return '0' * 32  # Special case: If n is 0, its binary representation is '000...000'
    elif n < 0:
        # If n is negative, convert it to its binary representation as if it were positive,
        # then remove the leading '-0b' from the result and pad it with leading zeros to make it 32 bits.
        return bin(n & 0xFFFFFFFF)[2:].zfill(32)  # 0xFFFFFFFF is used to ensure a 32-bit representation
    else:
        # Convert positive n to binary, remove the leading '0b', and pad it with leading zeros to make it 32 bits.
        return bin(n)[2:].zfill(32)

def twos_complement(binary_str):
    # Check if the number is negative
    if binary_str[0] == '1':
        # Perform two's complement by flipping the bits and adding 1
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        return -(int(inverted, 2) + 1)
    else:
        return int(binary_str, 2)


def simulator(s,PC):
    #R-Type
    #add
    ISB = False
    if (s[25:32]=='0110011' and s[17:20]=='000' and s[0:7]=='0000000'):
        regs[s[20:25]]=regs[s[7:12]]+regs[s[12:17]]
    #sub    
    elif (s[25:32]=='0110011' and s[17:20]=='000' and s[0:7]=='0100000'):
        regs[s[20:25]]=regs[s[12:17]] - regs[s[7:12]]
    #sll    
    elif (s[25:32]=='0110011' and s[17:20]=='001' and s[0:7]=='0000000'):
         l=regs[s[7:12]]
         regs[s[20:25]]=regs[s[12:17]] << l
    #slt     
    elif (s[25:32]=='0110011' and s[17:20]=='010' and s[0:7]=='0000000'):
         if(regs[s[12:17]] < regs[s[7:12]]):
             regs[s[20:25]]=1
    #sltu     
    elif (s[25:32]=='0110011' and s[17:20]=='011' and s[0:7]=='0000000'):
         regsue_rs1=regs[s[12:17]]
         regsue_rs2=regs[s[7:12]]
         if (regsue_rs1 < 0 and regsue_rs2 < 0) or (regsue_rs1 >= 0 and regsue_rs2 >= 0):
            if regsue_rs1 < regsue_rs2:
                regs[s[20:25]] = 1
            elif regsue_rs1 >= 0 and regsue_rs2 < 0:
                regs[s[20:25]] = 1
    #xor     
    elif (s[25:32]=='0110011' and s[17:20]=='100' and s[0:7]=='0000000'):
         regs[s[20:25]]=regs[s[7:12]] ^ regs[s[12:17]]  
    #srl     
    elif (s[25:32]=='0110011' and s[17:20]=='101' and s[0:7]=='0000000'):
        rd = s[20:25]
        rs1 = s[12:17]
        rs2 = s[7:12]
        f = regs[rs1] >> ((regs[rs2]) & 0b11111)
        regs[rd] = f
    #or    
    elif (s[25:32]=='0110011' and s[17:20]=='110' and s[0:7]=='0000000'):
        regs[s[20:25]]=regs[s[7:12]] | regs[s[12:17]]  
    #and    
    elif (s[25:32]=='0110011' and s[17:20]=='111' and s[0:7]=='0000000'):
        regs[s[20:25]]=regs[s[7:12]] & regs[s[12:17]]   
    #I-Type
    #lw
    elif s[-7:]=="0000011" and s[-15:-12]=="010":
        dest = s[-12:-7]
        op1 = regs[s[-20:-15]]
        imm = s[0:12]
        regs[dest] = memory_locations[address_specifier[(op1 + int(imm,2) - 65536)//4]]
   #addi
    elif s[-7:]=="0010011" and s[-15:-12]=="000":
        rd=s[20:25]
        op1=s[12:17]
        imm=s[0:12]
        regs[rd] = regs[op1] + twos_complement(imm)  
        
        
    #sltiu
    elif s[-7:]=="0010011" and s[-15:-12]=="011":
        rd=s[20:25]
        op1=s[12:17]
        imm=s[0:12]
        if regs[op1]<int(imm,2):
            regs[rd]=1
    #jalr
    elif s[-7:]=="1100111" and s[-15:-12]=="000":
        dest = regs[s[-12:-7]]
        imm = int(s[0:12],2)
        op1 = regs[s[12:17]]
        regs[dest] = PC + 4
        PC = regs[op1] + imm   
        PC = PC&0xFFFFFFFE
        ISB=True
    #S-Type
    #sw
    elif s[-7:]=="0100011" and s[-15:-12]=="010":
        imm = int(s[0:7]+s[20:25],2)
        print (imm)
        rs1 = regs[s[12:17]]
        memory_int = rs1 + imm
        rs2 = regs[s[7:12]]
        memory_locations[address_specifier[(memory_int-65536)//4]] = rs2

    #B-Type
    #beq
    elif s[-7:]=="1100011" and s[-15:-12]=="000":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
        if(regs[rs1]==regs[rs2]):
            ISB=True
            PC+=imm
    #bne
    elif s[-7:]=="1100011" and s[-15:-12]=="001":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
        if(regs[rs1]!=regs[rs2]):
            ISB=True
            PC+=imm
        

    #blt
    elif s[-7:]=="1100011" and s[-15:-12]=="100":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
        if(regs[rs1]<regs[rs2]):
            ISB=True
            PC+=imm
        

    #bge
    elif s[-7:]=="1100011" and s[-15:-12]=="101":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
        if(regs[rs1]>=regs[rs2]):
            ISB=True
            PC+=imm

    #bltu
    elif s[-7:]=="1100011" and s[-15:-12]=="110":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
        if(regs[rs1]<regs[rs2]):
            ISB=True
            PC+=imm
        
    
    #bgeu
    elif s[-7:]=="1100011" and s[-15:-12]=="111":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
        if(regs[rs1]>=regs[rs2]):
            ISB=True
            PC+=imm

    #U-Type
    #lui    
    elif s[-7:]=="0110111" :
        imm=(twos_complement(s[0:20])) << 12
        rd = s[-12:-7]
        regs[rd] = imm    
    
    #auipc
    elif s[-7:]=="0010111":
         rd = regs[s[-12:-7]]
         imm = (twos_complement(s[0:20])) << 12
         regs[rd] = imm + PC
    
    #J-Type
    #jal
    elif s[-7:]=="1101111":
        rd=s[20:25]
        imm=int(s[:20])
        ISB=True
    if not ISB:
        PC+=4


PC=0
program=open("program.txt",'r')
instructions={}
for i in program:
    instructions[PC]=i.strip()
    PC+=4
PC=0
print(instructions)
regs={"00000": 0, "00001": 0, "00010": 256, "00011": 0,
    "00100": 0, "00101": 0, "00110": 0, "00111": 0,
    "01000": 0, "01001": 0, "01010": 0, "01011": 0,
    "01100": 0, "01101": 0, "01110": 0, "01111": 0,
    "10000": 0, "10001": 0, "10010": 0, "10011": 0,
    "10100": 0, "10101": 0, "10110": 0, "10111": 0,
    "11000": 0, "11001": 0, "11010": 0, "11011": 0,
    "11100": 0, "11101": 0, "11110": 0, "11111": 0}
memory_locations = { "0x00010000" : 0 , "0x00010004" : 0 , "0x00010008" : 0 , "0x0001000c" : 0 , "0x00010010":0 ,"0x00010014":0,"0x00010018":0,"0x0001001c":0,"0x00010020":0,"0x00010024":0,"0x00010028":0,"0x0001002c":0,"0x00010030":0,"0x00010034":0,"0x00010038":0,"0x0001003c":0,"0x00010040":0,"0x00010044":0,"0x00010048":0,"0x0001004c":0,"0x00010050":0,"0x00010054":0,"0x00010058":0,"0x0001005c":0,"0x00010060":0,"0x00010064":0,"0x00010068":0,"0x0001006c":0,"0x00010070":0,"0x00010074":0,"0x00010078":0,"0x0001007c":0}
address_specifier = {  0 : "0x00010000" , 1 : "0x00010004" ,2:"0x00010008" ,3 : "0x0001000c"  ,4: "0x00010010" ,5:"0x00010014",6:"0x00010018", 7: "0x0001001c",8:"0x00010020",9 :"0x001010024",10:"0x00010028",11:"0x0001002c",12:"0x00010030",13:"0x00010034",14:"0x00010038",15:"0x0001003c",16:"0x00010040",17:"0x00010044",18:"0x00010048",19:"0x0001004c",20:"0x00010050",21:"0x00010054",22:"0x00010058",23:"0x0001005c",24:"0x00010060",25:"0x00010064",26:"0x00010068",27:"0x0001006c",28:"0x00010070",29:"0x00010074",30:"0x00010078",31:"0x0001007c"}
count = 0
outfile = open("output.txt","w")
for i in instructions:
    if instructions[i] == "00000000000000000000000001100011":
        outfile.write(f"0b{format(i,'032b')} ")
        for j in regs:
            outfile.write(f"0b{format(regs[j],'032b')} ")
        outfile.write("\n")
        break
    # m = int(input())
    simulator(instructions[i],i)
        # print(count)
    outfile.write(f"0b{format(i+4,'032b')} ")
    for j in regs:
        outfile.write(f"0b{format(regs[j],'032b')} ")
    outfile.write("\n")
for i in memory_locations:
    outfile.write(f"{i}:0b{format(memory_locations[i],'032b')}")
    outfile.write("\n")
    print(regs)
outfile.close()
print(memory_locations)
"""for i in regs:
    print(f"0b{format(regs[i],'032b')}" , end = " ")"""

