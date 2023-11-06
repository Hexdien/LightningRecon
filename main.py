

import requests
import inquirer

####### Variaveis de cores #######
green = "\033[0;32m"
END = "\033[0m"
red = "\033[0;31m"
##################################



##################################

def subdomains():
    subdm=["sl","admin","secreto","email","backup","interno"]
    alvo=input("Digite a url do alvo: ")
    for x in subdm:
        try:
            if alvo[len(alvo)-len(alvo)] == ".":
                target="https://" + x + alvo
                requisicao=requests.get(target)
                print(green+"Subdominio Encontrado | "+ target+END)
            elif alvo[len(alvo)-len(alvo)] != ".":
                target="https://" + x +"."+ alvo
                requisicao=requests.get(target)
                print(green+"Subdominio Encontrado | "+ target+END)
        except:
            print(red+x +"."+ alvo + " | Não existe!"  +END)

def directories():
    drt=["wp-admin","admin","robots.txt","login"]
    alvo=input("Digite a url do alvo: ")
    for x in drt:
        try:
            if alvo[len(alvo)-1] == "/":
                target="https://"+alvo+x
            elif alvo[len(alvo)-1] != "/":
                target="https://"+alvo + "/" + x

            requisicao=requests.get(target)
            sc=requisicao.status_code
            if sc >= 200 and sc <= 299:
                print(green + "Alvo encontrado: "+target + " | "+ str(sc) + END)
            elif sc == 404:
                print(red+"Alvo não encontrado: "+target + " | "+str(sc)+END)
            elif sc == 401 or 403:
                print(green+"Alvo não autorizado: "+target + " | "+ str(sc)+END)
        except:
                print(red+"Alvo Não existe  | " + target+END)

opt = [
        inquirer.List('opção',
                      message="Deseja fazer enumeração de Diretórios ou Subdominios?",
                      choices=['Subdominio','Diretório']
                      ),
        ]
print(
'''
 \033[1;30m    _, .--.
    (  / (  '-.
    .-=-.    ) -.
   /   (  .' .   \´
   \ ( ' ,_) ) \_/
    (_ , \033[1;36m/  \ \033[1;30m,_/
      '--\033[1;36m\   `\-\033[1;30m-`
          \033[1;36m_\  _\´
           `\ \´
            _\_\´
          `\ \´
            \ \´
           '`\.'.-.-'.-'.\´
           LIGHTNING RECON
     ''')

rspt = inquirer.prompt(opt)
if rspt['opção'] == "Subdominio":
    subdomains()
elif rspt['opção'] == "Diretório":
    directories()
else:
    print("Opção inválida!!")
