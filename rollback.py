#fiz esse script porque sou preguiçoso demais pra renomear
print("Digite o numero do ultimo arquivo : ",end='')
fim = int(input())
rollback = 0
for i in range(fim+1):
    try:
        with open("banner_"+str(i)+".txt",'r') as f:
            if not rollback == 0:
                with open("banner_"+str(i-rollback)+".txt",'w') as g:
                    g.write(f.read())

    except:
        rollback = rollback + 1

print("Rollback : "+str(rollback))
