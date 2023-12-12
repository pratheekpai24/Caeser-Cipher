import os
import sys
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
def cls():
    os.system('cls')
cls()
do = True
ew = "The encoded text = "
dw = "The decoded text = "
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def main(t,s):
    nap = []
    dap = []
    for i in t:
        if i not in alpha:
            nap.append(i)
            dap.append(i)
            continue
        a = alpha.index(i)
        nap.append(alpha[a+s]) #encodes the text
        dap.append(alpha[a-s]) #decodes the text
    if op == 'encode':
        print(ew,end="")
        for i in nap:
            print(i,end="")
    if op == 'decode':
        print(dw,end="")
        for i in dap:
            print(i,end="")
    jk = input("\nType 'yes' to try again and type 'no' to exit = \n").lower()
    if jk == 'no':
        sys.exit(0)
print(logo)
while do == True:
    op = input("Type 'encode' to encrpyt or type 'decode' to decrypt =\n").lower()
    text = input("Enter your message =\n").lower()
    shift = int(input("Type the shift number (1 - 26) =\n") )
    main(text,shift)




