#--coding:utf8;--
#qpy:3
#qpy:console
import subprocess
import sys
e = input("Arquivo ou programa? \n").lower()
if e == "programa":
    while a == True :
        print( "TAKSBAR" )
        a = input( "Entre com o nome do programa \n" )
        if a == "exit":
            a = False
        else:
            subprocess.run( a )
        continue
elif e == "arquivos":
    while s == True:
        s = input("nome do arquivo\n")
        if s == "exit":
            s = False
        else:
            s.open()
            s.read()
            s.close()
        continue
else:
    print("tchau")
    sys.exit()