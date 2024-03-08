import math
def dec_to_bin(n,x):
    k=abs(int(n));
    if(int(n)>=0):
        s="";
        c=0
        while(k!=0):
            c=c+1
            t=k%2
            s=str(t)+s;
            k=k//2   
        s="0"*(x-c)+s
        return s
    else:
        p=int(math.log(k,2))+1
        k=(2**p)-k
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
    output+=opcode[div[0]]
    output+=regs[rs[0]]
    output+=funct3[div[0]]
    output+=regs[rs[1]]
    output+=regs[rs[2]]
    output+=funct7[div[0]]
    return output

def Ins_I_Type(line):
    output=""
    div=line.split(" ")
    if (div[0]=="lw"):
        d=line.split(",")
        rs2 = d[0].split()[1]  
        rest = d[1].split("(")
        rs1 = rest[1].split(")")[0] 
        imm = rest[0]
        k=dec_to_bin(imm,12)
        print(k,regs[rs1],funct3[div[0].split()[0]],regs[rs2],opcode[div[0].split()[0]])
        output+=k+regs[rs1]+funct3[div[0].split()[0]]+regs[rs2]+opcode[div[0].split()[0]]
        return output
    rs=div[1].split(",")
    output+=opcode[div[0]]
    output+=regs[rs[0]]
    output+=funct3[div[0]]
    output+=regs[rs[1]]
    imv=dec_to_bin(int(rs[2]),12)
    output+=imv
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
    
def Ins_B_Type(line):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    im=dec_to_bin(rs[2],12)
    output+=opcode[div[0]]
    output+=im[7:]
    output+=funct3[div[0]]
    output+=regs[rs[0]]
    output+=regs[rs[1]]
    output+=im[:7]
    return output
    
def Ins_U_Type(line):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    output+=opcode[div[0]]
    output+=regs[rs[0]]
    im=dec_to_bin(rs[1],20)
    output+=im
    return output
    
def Ins_J_Type(line):
    output=""
    div=line.split(" ")
    rs=div[1].split(",")
    output+=opcode[div[0]]
    output+=regs[rs[0]]
    im=dec_to_bin(int(rs[1]),20)
    output+=im
    return output

regs={"zero":"00000","ra":"00001","sp":"00010","gp":"00011",
      "tp":"00100","t0":"00101","t1":"00110","t2":"00111","s0":"01000",
      "fp":"01000","s1":"01001","a0":"01010","a1":"01011",
      "a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000",
      "a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101",
      "s6":"10110","s7":"10111","s8":"11000","s9":"11001","s10":"11010",
      "s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"}
output=""
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
        "jal":"1101111","jalr":"1101111","lui":"0110111","auipc":"0010111",
        "ecall":"1110011","ebreak":"1110011"}
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
set_Ins_Type=""

if set_Ins_Type=="R":
    Ins_R_Type(line)
elif set_Ins_Type=="I":
    Ins_I_Type(line)
elif set_Ins_Type=="S":
    Ins_S_Type(line)
elif set_Ins_Type=="B":
    Ins_B_Type(line)
elif set_Ins_Type=="U":
    Ins_U_Type(line)
elif set_Ins_Type=="J":
    Ins_J_Type(line)


    
