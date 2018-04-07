#Talvez comparar as hashes seja mais facil \(T-T)/

print("Bem vindo a solução de diff de banners =D")
print("Este programa indica arquivos com conteudo duplicado")
print("Insira o numero do ultimo banner : ",end='')
fim = int(input())

dup = []

for i in range(fim+1):
    try:
        with open("banner_"+str(i)+".txt",'r') as f:
            sup = f.read()
        for j in range(i+1, fim+1):
            if not j in dup:
                try:
                    print("Checando "+str(i)+" -> "+str(j)+" : ",end='')
                    with open("banner_"+str(j)+".txt",'r') as f:
                        dow = f.read()
                    if sup == dow:
                        dup.append(j)
                        print("dup")
                    else:
                        print("diff")
                except:
                    print("Erro ao abrir banner "+str(j))

    except:
        print("Erro ao abrir o banner "+str(i))

if len(dup) > 0:
    print("Sem duplicatas")
else:
    print("Escrevendo arquivos que possuem duplicação no dup.txt")

with open("dup.txt",'w') as f:
    for i in dup:
        f.write(str(i)+'\n')

