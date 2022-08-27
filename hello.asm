	section .data
message: db    "Hello, momo", 0Ah, 00h
	global _main
	section .text
_main:
	mov 	rax, 0x02000004		;syscall for write
	mov		rdi, 1				;file descriptor 1 is stdout
	mov		rsi, qword message	;get string address
	mov		rdx, 13				;number of bytes
	syscall						;execute syscall (write)
	mov		rax, 0x02000001		;syscall for exit
	mov 	rdi, 69				;exit code 69
	syscall						;execute syscall (exit) with 69
