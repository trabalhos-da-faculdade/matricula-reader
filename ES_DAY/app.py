# imports
import methods

methods.welcomeScreen()
p = True
while p:
    matricula = input('MATRICULA: ')
    if(len(matricula) < 8):
        print("MATRICULA INVÁLIDA! TENTE NOVAMENTE")
        continue
    else:
        matricula = matricula[0:8]
    print("\n")
    print("--------------------------------------------------------------------------------------")
    print('MATRICULA DO ALUNO: ',matricula)
    print("\n")
    check = input('CONFIRMAR MATRICULA: \n[ENTER]Confirmar  [t/T]Tentar novamente [f/F]Concluir: ')
    print("--------------------------------------------------------------------------------------")
    if(check == 'ENTER' or check == ""):
        print('MATRICULA CONFIRMADA!')
        methods.writeOnFile(matricula)
    elif(check == 't' or check == 'T'):
        continue
    elif(check == 'f' or check == 'F'):
        print('CONFIRMAÇÃO COM ES-DAY CONCLUIDO!')
        p = False
    else:
        print('Comando Não confirmado, tente novamente!')
        continue





