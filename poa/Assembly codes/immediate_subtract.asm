
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h


MOV AX,6H
MOV BX,9H
MOV CL,00h
SUB AX,BX
MOV DX,AX
JNC borrow
INC CL
NOT AX
ADD AX,0001h
MOV DX, AX
borrow:
MOV [1006h], CL
HLT

ret




