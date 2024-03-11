#Assembler

This program serves as an assembler. It reads assembly programs from a text file as input and generates binary machine code or error notifications as output. The assembler ensures that the input assembly code follows the specified format and rules, handling various instruction types, labels, and error cases.

### Features

1. **Conversion of Assembly to Binary**:
   - Converts assembly instructions into 32-bit binary machine code.
   - Handles R-type, I-type, S-type, B-type, U-type, and J-type instructions.

2. **Assembler Functionality**:
   - Reads assembly program from input text file.
   - Generates binary output if the code is error-free.
   - Detects and reports errors with line numbers if encountered.
   - Supports labels for jump and branch instructions, calculating relative offsets.

3. **Error Handling**:
   - Detects illegal instructions, register names, and immediate values.
   - Ensures the presence of a virtual halt instruction at the end of the program.

4. **Memory Size and Addressing**:
   - Defines the memory sizes and ranges for program memory, stack memory, and data memory.
   - Ensures proper memory allocation and addressing within the specified ranges.

### Supported Instruction Encoding

- **R-type Instructions**: add, sub, xor, or, and, sll, srl, sra, slt, sltu
- **I-type Instructions**: addi, xori, ori, andi, slli, srli, srai, slti, sltiu, lb, lh, lw, lbu, lhu, jalr, ecall, ebreak
- **S-type Instructions**: sb, sh, sw
- **B-type Instructions**: beq, bne, blt, bge, bltu, bgeu
- **U-type Instructions**: lui, auipc
- **J-type Instructions**: jal

### Additional Notes

- The assembler ensures compatibility with the ISA and ABI conventions.
- The output binary file contains 32-bit binary numbers represented in ASCII.
- The program terminates with the Virtual Halt instruction (`beq zero, zero, 0x00000000`).
- The assembler supports custom-defined instructions: mul, rst, halt, and rvrs, as a bonus feature.

### Usage

1. **Input File Format**: Provide a text file containing the assembly program, following the specified format.
2. **Output**: The assembler generates a text file with binary machine code or error notifications.
