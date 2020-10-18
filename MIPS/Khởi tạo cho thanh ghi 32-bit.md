* `lui` - Load upper immediate
* `ori` - Bitwise or immediate

### Khởi tạo cho thanh ghi 32-bit
Thực hiện lần lượt các lệnh:
```
lui Reg, hImm
ori Reg, Reg, lImm
```
trong đó:
* `Reg` là thanh ghi cần nạp giá trị
* `hImm` là giá trị cần nạp vào nửa cao (16 bit đầu) của thanh ghi
* `lImm` là giá trị cần nạp vào nửa thấp (16 bit cuối) của thanh ghi

#### Ví dụ
Nạp vào thanh `$s0` giá trị 32-bit
`0010 0001 1010 0000 0100 0000 0011 1011 = 0x21A0403B`.

Nạp `0x21A0` vào nửa cao của `$s0`:
```
lui $s0, 0x21A0
```
Sau khi nạp, nửa cao của `$s0` chứa giá trị
`0010 0001 1010 0000 = 0x21A0`.

Nạp `0x403B` vào nửa thấp của `$s0`:
```
ori $s0, $s0, 0x403B
```
Sau khi nạp, nửa thấp của `$s0` chứa giá trị
`0100 0000 0011 1011 = 0x403B`
và `$s0` đã chứa giá trị 32-bit như yêu cầu.

