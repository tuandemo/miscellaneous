## A Few MIPS Examples
### If-Else
_HowOldAreYou.asm_

```
.data
question:     .asciiz "How old are you?\n"
accepted:     .asciiz "You can watch this video now.\n"
not_accepted: .asciiz "You are not allowed to watch this video.\n"

.text
print_question:
	la $a0, question                   # a0 := Address of 'question'
	li $v0, 4                          # v0 := 4 (code for printing a string)
	syscall                            # 
read_user_input:
	li $v0, 5                          # v0 := 5 (code for reading an integer)
	syscall                            # 
	move $t0, $v0                      # t0 := v0
check_if_input_is_greater_than_18:
	sgt $t0, $t0, 18                   # t0 := 1 if t0 > 18, else t0 := 0
	beq $t0, $0, else                  # go to label 'else' if t0 = 0
if_ok:
	la $a0, accepted                   # a0 := Address of 'accepted'
	li $v0, 4                          # v0 := 4 (code for printing a string)
	syscall                            # 
	j exit                             # jump to label 'exit'
else:
	la $a0, not_accepted               # a0 := Address of 'not_accepted'
	li $v0, 4                          # v0 := 4 (code for printing a string)
	syscall                            #
exit:
	li $v0, 10                         # v0 := 10 (code for exitting)
	syscall                            #

```
### Do-While
_PasswordReading.asm_
```
.data
question: .asciiz "Enter your password (4 characters): "
if_wrong: .asciiz "\nWrong password. Please try again.\n"
if_right: .asciiz "\nWelcome! You logged in.\n"
true_pwd: .asciiz "Yeah"
password: .space  5 # include ending "\0"

.text
loop:
	li $v0, 4
	la $a0, question
	syscall                               # print question
	li $v0, 8
	la $a0, password
	la $a1, 5
	syscall                               # a0 := read password
	move $t0, $a0                         # t0 := a0
	la $t1, true_pwd                      # t1 := true_pwd
	compare_loop:
		lb $t2, ($t0)                 # t2 := &t0
		lb $t3, ($t1)                 # t3 := &t1
		bne $t2, $t3, not_equal       # if t2 != t3 goto not_equal
		beq $t2, $0, equal_end        # if t2 = 0 (= &'\0') goto equal
		addi $t0, $t0, 1              # t0 := t0 + 1 (get next char)
		addi $t1, $t1, 1              # t1 := t1 + 1 (get next char)
		j compare_loop                # continue compare_loop
		not_equal:
			li $v0, 4
			la $a0, if_wrong
			syscall               # print if_wrong
			j loop                # continue loop
		equal_end:
			li $v0, 4
			la $a0, if_right
			syscall               # print if_right
exit:
	li $v0, 10
	syscall                               # exit

```
## Jump/Jump-and-link/Jump-register
_SwapIntegers.asm_
```
.data
text1: .asciiz "Enter first number: "
text2: .asciiz "Enter second number: "
text3: .asciiz "After swapping: "
space: .asciiz ", "
endln: .asciiz "\n"

.text
main:
	jal input
	jal swap
	jal print
	j exit
input:
	la $a0, text1
	li $v0, 4
	syscall                # print text1
	li $v0, 5
	syscall                # v0 := read_int
	move $a1, $v0          # a1 := v0
	la $a0, text2
	li $v0, 4
	syscall                # print text2
	li $v0, 5
	syscall                # v0 := read_int
	move $a2, $v0          # a2 := v0
	jr $ra
swap:
	move $t1, $a1          # t1 := a1
	move $t2, $a2          # t2 := a2
	move $a2, $t1          # a2 := t1
	move $a1, $t2          # a1 := t2
	jr $ra
print:
	la $a0, text3
	li $v0, 4
	syscall                # print text3
	move $a0, $a1
	li $v0, 1
	syscall                # print a0 (= a1)
	la $a0, space
	li $v0, 4
	syscall                # print space
	move $a0, $a2
	li $v0, 1
	syscall                # print a0 (= a2)
	la $a0, endln
	li $v0, 4
	syscall                # print endln
exit:
	li $v0, 10
	syscall                # exit
```