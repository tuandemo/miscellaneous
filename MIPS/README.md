# Fundamental Instructions
## Arithmetic
```
add dReg, sReg, tReg           # Add (with Overflow)
addi dReg, sReg, Imm           # Add immediate (with Overflow)
addu dReg, sReg, tReg          # Add unsigned (no Overflow)
addiu dReg, sReg, Imm          # Add immediate unsigned (no Overflow)

sub dReg, sReg, tReg           # Add (with Overflow)
subu dReg, sReg, tReg          # Add unsigned (no Overflow)

mult sReg, tReg                # Multiply
div sReg, tReg                 # Divide

mfhi dReg                      # Move from HI
mflo dReg                      # Move from LO

```
## Data Transfer
```
lw dReg, offset(sReg)          # Load word
lh dReg, offset(sReg)          # Load half
lhu dReg, offset(sReg)         # Load half unsigned
lb dReg, offset(sReg)          # Load byte
lbu dReg, offset(sReg)         # Load byte unsigned
lui dReg, Imm                  # Load upper immediate
la dReg, Labl                  # Load from Label

sw dReg, offset(sReg)          # Store word
sh dReg, offset(sReg)          # Store half
sb dReg, offset(sReg)          # Store byte
```
## Logical
```
and dReg, sReg, tReg           # Bitwise AND
or dReg, sReg, tReg            # Bitwise OR
nor dReg, sReg, tReg           # Bitwise NOR
andi dReg, sReg, Imm           # Bitwise AND immediate
ori dReg, sReg, Imm            # Bitwise OR immediate
nori dReg, sReg, Imm           # Bitwise NOR immediate

sll dReg, sReg, Imm            # Shift Left logical
srl dReg, sReg, Imm            # Shift Right logical
```


## References
* [Programmed Instroduction to MIPS Assembly Language](https://chortle.ccsu.edu/AssemblyTutorial/)
* [MIPS Instruction Reference](http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html)
