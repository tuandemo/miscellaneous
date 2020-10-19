## A Few MIPS Examples
### If-Else
`HowOldAreYou.asm`

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
`PasswordReading.asm`
```
.data
question:     .asciiz "How old are you?\n"
accepted:     .asciiz "You can watch this video now.\n"
not_accepted: .asciiz "You are not allowed to watch this video.\n"

.text
print_question:                        # 
	la $a0, question                   # a0 := Address of 'question'
	li $v0, 4                          # v0 := 4 (code for printing a string)
	syscall                            # 
read_user_input:                       # 
	li $v0, 5                          # v0 := 5 (code for reading an integer)
	syscall                            # 
	move $t0, $v0                      # t0 := v0
check_if_input_is_greater_than_18:     # 
	sgt $t0, $t0, 18                   # t0 := 1 if t0 > 18, else t0 := 0
	beq $t0, $0, else                  # go to label 'else' if t0 = 0
if_ok:                                 # 
	la $a0, accepted                   # a0 := Address of 'accepted'
	li $v0, 4                          # v0 := 4 (code for printing a string)
	syscall                            # 
	j exit                             # jump to label 'exit'
else:                                  # 
	la $a0, not_accepted               # a0 := Address of 'not_accepted'
	li $v0, 4                          # v0 := 4 (code for printing a string)
	syscall                            #
exit:                                  #
	li $v0, 10                         # v0 := 10 (code for exitting)
	syscall                            #

```