_[MIPS: lw (load word) instruction](https://stackoverflow.com/questions/31563768/)_

### Is `lw $s0, 8($0)` the same as `lw $s0, 0($v0)`?

The format of the `lw` instruction is as follows:
```
lw RegDest, Offset(RegSource)
```
where `RegDest` and `RegSource` are MIPS registers, and `Offset` is an immediate.

It means, load into register `RegDest` the word contained in the address resulting from adding the contents of register `RegSource` and the `Offset` specified. The resulting source address must be word-aligned (i.e. multiple of 4).

Therefore, `lw $s0, 8($0)` means to load in `$s0` the contents of the word located at address specified by `$0` plus `8`. As `$0` is register `$zero` which will always contain the constant zero, it will load the word located in absolute address `8` into `$s0`.

`lw $s0, 0($v0)` means to load in `$s0` the contents of the word located at the address specified by `$v0`. If `$v0` contains the value `8` then both instructions have the same effect. If `$v0` is not a multiple of 4, the instruction will generate an addressing trap.

Usually `lw` is a pseudoinstruction in the sense that the assembler may emmit more than one instruction to accomplish the instruction. The offset (displacement) has to be a 16-bit signed value. If your instruction has an immediate with more bits, the assembler will usually use a temporary register (`$at`) to hold the contents of the immediate and then emmit equivalent instructions to perform the intended behavior. You may see this in action using a dissassembler or a MIPS monitor (also inspecting the code with MARS simulator).
