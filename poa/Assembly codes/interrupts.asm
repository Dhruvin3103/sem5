DATA SEGMENT 
    MSG DB "Enter any Character : $"
    DATA ENDS
CODE SEGMENT
    START:
    MOV AX,DATA
    MOV DS,AX
    LEA DX,MSG
    MOV AH,09H 
    INT 21H
    MOV AH,01h
    INT 21H
    MOV DL,AL
    MOV AH,02h
    INT 21H
    
    MOV AH,4CH
    INT 21H
    CODE ENDS
END START
