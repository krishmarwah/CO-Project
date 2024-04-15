
def simulator(s):
    #R-Type
    #add
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
    elif s[-7:]=="0000011" and s[-14:-11]=="010":
        return LW
   #addi
    elif s[-7:]=="0010011" and s[-15:-12:-1]=="000":
        rd=s[20:25]
        op1=s[12:17]
        imm=s[0:12]
        regs[rd] = regs[op1] + twos_complement(imm)  
        
        
    #sltiu
    elif s[-7:]=="0010011" and s[-15:-12:-1]=="011":
        rd=s[20:25]
        op1=s[12:17]
        imm=s[0:12]
        if regs[op1]<int(imm,2):
            regs[rd]=1
    #jalr
    elif s[-7:]=="1100111" and s[-14:-11]=="000":
        rs=s[12:17]
        imm=int(s[:12])
        rd=s[20:25]
        regs[rd]=regs[]
    #S-Type
    #sw
    elif s[-7:]=="0100011" and s[-14:-11]=="010":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])

    #B-Type
    #beq
    elif s[-7:]=="1100011" and s[-14:-11]=="000":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])

    #bne
    elif s[-7:]=="1100011" and s[-14:-11]=="001":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])

    #blt
    elif s[-7:]=="1100011" and s[-14:-11]=="100":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])

    #bge
    elif s[-7:]=="1100011" and s[-14:-11]=="101":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])

    #bltu
    elif s[-7:]=="1100011" and s[-14:-11]=="110":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])
    
    #bgeu
    elif s[-7:]=="1100011" and s[-14:-11]=="111":
        rs1=s[12:17]
        rs2=s[7:12]
        imm=int(s[:7]+s[20:25])

    #U-Type
    #lui
    elif s[-7:]=="0110111":
        rd=s[20:25]
        imm=int(s[:20])
    
    #auipc
    elif s[-7:]=="0010111":
        rd=s[20:25]
        imm=int(s[:20])
    
    #J-Type
    #jal
    elif s[-7:]=="1101111":
        rd=s[20:25]
        imm=int(s[:20])
    




regs={"00000": 0, "00001": 0, "00010": 0, "00011": 0,
    "00100": 0, "00101": 0, "00110": 0, "00111": 0,
    "01000": 0, "01001": 0, "01010": 0, "01011": 0,
    "01100": 0, "01101": 0, "01110": 0, "01111": 0,
    "10000": 0, "10001": 0, "10010": 0, "10011": 0,
    "10100": 0, "10101": 0, "10110": 0, "10111": 0,
    "11000": 0, "11001": 0, "11010": 0, "11011": 0,
    "11100": 0, "11101": 0, "11110": 0, "11111": 0}
for i in regs:
    print(f"0b{format(regs[i],'032b')}" , end = " ")

