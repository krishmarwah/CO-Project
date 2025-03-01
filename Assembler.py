import sys
import math
def dec_to_bin(n,x):
    k=abs(int(n));
    if(int(n)>=0):
        s=""
        c=0
        while(k!=0):
            c=c+1
            t=k%2
            s=str(t)+s;
            k=k//2   
        s="0"*(x-c)+s
        return s
    else:
        k=(2**x)-k
        s="";
        c=0
        while(k!=0):
            c=c+1
            t=k%2
            s=str(t)+s;
            k=k//2  
        s="1"*(x-c)+s
        return s


def Ins_R_Type(line):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    output+=funct7[div[0]]
    output+=regs[rs[2]]
    output+=regs[rs[1]]
    output+=funct3[div[0]]
    output+=regs[rs[0]]
    output+=opcode[div[0]]
    return output

def Ins_I_Type(line):
    output=""
    div=line.split(" ")
    if (div[0]=='lw'):
        output=""
        div=line.split(",")
        rs2 = div[0].split()[1]  
        rest = div[1].split("(")
        rs1 = rest[1].split(")")[0] 
        imm = rest[0]
        k=dec_to_bin(imm,12)
        output+=k[0:12]+regs[rs1]+funct3[div[0].split()[0]]+regs[rs2]+opcode[div[0].split()[0]]
        return output
    rs=div[1].split(",")
    imv=dec_to_bin(int(rs[2]),12)
    output+=imv
    output+=regs[rs[1]]
    output+=funct3[div[0]]
    output+=regs[rs[0]]
    output+=opcode[div[0]]
    return output

def Ins_S_Type(line):
    output=""
    div=line.split(",")
    rs2 = div[0].split()[1]  
    rest = div[1].split("(")
    rs1 = rest[1].split(")")[0] 
    imm = rest[0]
    k=dec_to_bin(imm,12)
    output+=k[0:7]+regs[rs2]+regs[rs1]+funct3[div[0].split()[0]]+k[7:12]+opcode[div[0].split()[0]]
    return output
    
    
def Ins_B_Type(line,c):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    im=rs[2]
    if(im.isdigit()):
        im=dec_to_bin(int(im),13)
        output+=im[0]+im[2:8]
        output+=regs[rs[1]]
        output+=regs[rs[0]]
        output+=funct3[div[0]]
        output+=im[8:12]+im[1]
        output+=opcode[div[0]]
        return output
    elif (im in labels):
        k=labels[im]-c+4
        im=dec_to_bin(k,13)
        output+=im[0]+im[2:8]
        output+=regs[rs[1]]
        output+=regs[rs[0]]
        output+=funct3[div[0]]
        output+=im[8:12]+im[1]
        output+=opcode[div[0]]
        return output



def Ins_U_Type(line):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    im=dec_to_bin(rs[1],32)
    output+=im[0:20]
    output+=regs[rs[0]]
    output+=opcode[div[0]]
    return output

def Ins_J_Type(line,c):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    im=rs[1]
    if(im.isdigit()):
        im=dec_to_bin(int(rs[1]),21)
        imr=im[0]+im[10:20]+im[9]+im[1:9]
        output+=imr
        output+=regs[rs[0]]
        output+=opcode[div[0]]
        return output
    elif (im in labels):
        k=labels[im]-c+4
        im=dec_to_bin(k,21)
        imr=im[0]+im[10:20]+im[9]+im[1:9]
        output+=imr
        output+=regs[rs[0]]
        output+=opcode[div[0]]
        return output
def bonus_instruction(line):
    output=""
    d=line.split()
    if(d[0]=="mul"):
        output+="0"*7
        p=d[1].split(',')
        rd=p[0]
        rs1=p[1]
        rs2=p[2]
        output+=regs[rs2]
        output+=regs[rs1]
        output+="0"*3
        output+=regs[rd]
        output+=opcode[d[0]]
    elif (d[0]=="rst" or d[0]=="halt"):
        output+="0"*25
        output+=opcode[d[0]]
    elif (d[0]=="rvrs"):
        output+="0"*12
        p=d[1].split(',')
        rd=p[0]
        rs=p[1]
        output+=regs[rs]
        output+="0"*3
        output+=regs[rd]
        output+=opcode[d[0]]
    return output    
regs={"zero":"00000","ra":"00001","sp":"00010","gp":"00011",
      "tp":"00100","t0":"00101","t1":"00110","t2":"00111","s0":"01000",
      "fp":"01000","s1":"01001","a0":"01010","a1":"01011",
      "a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000",
      "a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101",
      "s6":"10110","s7":"10111","s8":"11000","s9":"11001","s10":"11010",
      "s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"}
opcode={"add":"0110011","sub":"0110011","xor":"0110011","or":"0110011",
        "and":"0110011","sll":"0110011","srl":"0110011","sra":"0110011",
        "slt":"0110011","sltu":"0110011",
        "addi":"0010011","xori":"0010011","ori":"0010011","andi":"0010011",
        "slli":"0010011","srli":"0010011","srai":"0010011","slti":"0010011",
        "sltiu":"0010011",
        "lb":"0000011","lh":"0000011","lw":"0000011","lbu":"0000011",
        "lhu":"0000011",
        "sb":"0100011","sh":"0100011","sw":"0100011",
        "beq":"1100011","bne":"1100011","blt":"1100011","bge":"1100011",
        "bltu":"1100011","bgeu":"1100011",
        "jal":"1101111","jalr":"1100111","lui":"0110111","auipc":"0010111",
        "ecall":"1110011","ebreak":"1110011","mul":"1111111","rst":"1111110","halt":"1111101","rvrs":"1111100"}
funct3={"add":"000","sub":"000","xor":"100","or":"110",
        "and":"111","sll":"001","srl":"101","sra":"101",
        "slt":"010","sltu":"011",
        "addi":"000","xori":"100","ori":"110","andi":"111",
        "slli":"001","srli":"101","srai":"101","slti":"011",
        "sltiu":"011",
        "lb":"000","lh":"001","lw":"010","lbu":"100",
        "lhu":"101",
        "sb":"000","sh":"001","sw":"010",
        "beq":"000","bne":"001","blt":"100","bge":"101",
        "bltu":"110","bgeu":"111",
        "jalr":"000",
        "ecall":"000","ebreak":"000"}
funct7={"add":"0000000","sub":"0100000","sll":"0000000","slt":"0000000",
        "slt":"0000000","sltu":"0000000",
        "srl":"0000000","xor":"0000000","or":"0000000","and":"0000000",
        }
R=["add","sub","xor","or","and","sll","srl","sra","slt","sltu"]
I=["addi","xori","ori","andi","slli","srli","srai","slti","sltiu","lb","lh",
   "lw","lbu","lhu","jalr","ecall","ereak"]
S=["sb","sh","sw"]
B=["beq","bne","blt","bge","bltu","bgeu"]
J=["jal"]
U=["lui","auipc"]

fname=sys.argv[1]
fread=open(fname,"r")
input_lines=fread.readlines()
output_lines=[]
for i in range(len(input_lines)):
    input_lines[i]=input_lines[i].strip()
labels = {}
pq=[]
current_address=0
for i in range(len(input_lines)):
    if ":" in input_lines[i]:
        label = input_lines[i].split(":")[0]
        if label in labels:
            pq.append("Error: Duplicate label '" + label + "' on line " + str(i+1))
        else:
             if current_address != 0:
                current_address+=4
                labels[label] = current_address
             else:
                labels[label] = current_address
    else:
        if input_lines[i]=="":
            continue
        current_address += 4
for i in range(len(input_lines)):
    if ":" in input_lines[i]:
        input_lines[i]=input_lines[i].split(":")[1].strip()
def find_errors(input_lines):
    errors = []
    for i in range(len(input_lines)):
        div = input_lines[i].split(" ")
        
        if div[0] in R:
            k = div[1].split(',')
            if k[0] not in regs.keys():
                errors.append("Error: Invalid register '" + k[0] + "' on line " + str(i+1))
            elif k[1] not in regs.keys():
                errors.append("Error: Invalid register '" + k[1] + "' on line " + str(i+1))
            elif k[2] not in regs.keys():
                errors.append("Error: Invalid register '" + k[2] + "' on line " + str(i+1))
        elif div[0] in I:
            k = div[1].split(',')
            if div[0] != 'lw':
                if k[0] not in regs.keys():
                    errors.append("Error: Invalid register '" + k[0] + "' on line " + str(i+1))
                elif k[1] not in regs.keys():
                    errors.append("Error: Invalid register '" + k[1] + "' on line " + str(i+1))
                elif int(k[2]) < -2**11 or int(k[2]) >= 2**11:
                    errors.append("Error: Immediate value " + k[2] + " out of range on line " + str(i+1))
            else:
                d = input_lines[i].split(",")
                rs2 = d[0].split()[1]
                rest = d[1].split("(")
                rs1 = rest[1].split(")")[0]
                imm = rest[0]
                if rs2 not in regs.keys():
                    errors.append("Error: Invalid register '" + rs2 + "' on line " + str(i+1))
                elif rs1 not in regs.keys():
                    errors.append("Error: Invalid register '" + rs1 + "' on line " + str(i+1))
                elif int(imm) < -2**11 or int(imm) >= 2**11:
                    errors.append("Error: Immediate value " + imm + " out of range on line " + str(i+1))
        elif div[0] in S:
            d = input_lines[i].split(",")
            rs2 = d[0].split()[1]
            rest = d[1].split("(")
            rs1 = rest[1].split(")")[0]
            imm = rest[0]
            if rs2 not in regs.keys():
                errors.append("Error: Invalid register '" + rs2 + "' on line " + str(i+1))
            elif rs1 not in regs.keys():
                errors.append("Error: Invalid register '" + rs1 + "' on line " + str(i+1))
            elif int(imm) < -2**11 or int(imm) >= 2**11:
                errors.append("Error: Immediate value " + imm + " out of range on line " + str(i+1))
        elif div[0] in B:
            k = div[1].split(',')
            if k[0] not in regs.keys():
                errors.append("Error: Invalid register '" + k[0] + "' on line " + str(i+1))
            elif k[1] not in regs.keys():
                errors.append("Error: Invalid register '" + k[1] + "' on line " + str(i+1))
            elif k[2].isdigit(): 
                imm = int(k[2])
                if imm < -4096 or imm >= 4096:
                    errors.append("Error: Immediate value " + str(imm) + " out of range on line " + str(i+1))
            elif k[2] not in labels:  
                errors.append("Error: Label '" + k[2] + "' not found on line " + str(i+1))
    
        elif div[0] in U :
            k = div[1].split(',')
            if k[0] not in regs.keys():
                errors.append("Error: Invalid register '" + k[0] + "' on line " + str(i+1))
            elif int(k[1]) < -2**31 or int(k[1]) >= 2**31:
                errors.append("Error: Immediate value " + k[1] + " out of range on line " + str(i+1))
        elif div[0] in J :
            k = div[1].split(',')
            if k[0] not in regs.keys():
                errors.append("Error: Invalid register '" + k[0] + "' on line " + str(i+1))
            elif int(k[1]) < -2**19 or int(k[1]) >= 2**19:
                errors.append("Error: Immediate value " + k[1] + " out of range on line " + str(i+1))        
        else:
            if div[0] not in labels:
                errors.append("Error: Invalid instruction '" + div[0] + "' on line " + str(i+1))        
    return errors

output_file=sys.argv[2]
fwrite=open(output_file,"w")
c=0
errors = find_errors(input_lines)
if errors:
    for error in errors:
        fwrite.write(error+'\n')
elif pq:
    for k in pq:
        fwrite.write(k+'\n')   
else:
    if input_lines[-1] != "beq zero,zero,0":
        fwrite.write("Error: 'virtual_halt' instruction is missing at the end of the program"+'\n')
    else:
        output_lines = []
        for line in input_lines:
            div = line.split(" ")
            if div[0] in R:
                c+=4
                output_lines .append( Ins_R_Type(line))
            elif div[0] in I:
                c+=4
                output_lines.append( Ins_I_Type(line))
            elif div[0] in S:
                c+=4
                output_lines.append( Ins_S_Type(line))
            elif div[0] in B:
                c+=4
                output_lines.append( Ins_B_Type(line,c))
            elif div[0] in U:
                c+=4
                output_lines.append( Ins_U_Type(line))
            elif div[0] in J:
                c+=4
                output_lines.append( Ins_J_Type(line,c))
        for i in range(len(output_lines)-1):
            fwrite.write(output_lines[i]+"\n")
        fwrite.write(output_lines[len(output_lines)-1])
