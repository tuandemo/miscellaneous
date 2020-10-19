## Macro in MIPS
_Macro.asm_
```
.data
NewLine: .asciiz "\n"
Space:   .asciiz " "
Tab:     .asciiz "\t" 


.text .globl MACRO
MACRO:
	.macro Print(%str)
		la $a0, %str
		li $v0, 4
		syscall
	.end_macro
	.macro rPrint(%sReg)
		move $a0, %sReg
		li $v0, 4
		syscall
	.end_macro
	.macro Read(%dReg, %buffer, %len)
		la $a0, %buffer
		li $a1, %len
		li $v0, 8
		syscall
		move %dReg, $a0
	.end_macro
	.macro iPrint(%int)
		la $a0, %int
		li $v0, 1
		syscall
	.end_macro
	.macro If(%cond, %label1, %label2)
		bne %cond, $0, %label2
		j %label1
	.end_macro
	.macro Exit()
		li $v0, 10
		syscall
	.end_macro

```


_Test.asm_
```
.data
WhatIsYourName: .asciiz "What is your name?"
Hello: .asciiz "Hello"
name: .space 21 # '\0' included

.text
.include "Macro.asm"
main:
	Print(WhatIsYourName)
	Print(NewLine)
	Read($t0, name, 21)
	Print(Hello)
	Print(Space)
	rPrint($t0)
	Print(NewLine)
	Exit()

```