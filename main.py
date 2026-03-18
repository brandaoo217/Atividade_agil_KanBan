from processos import media, aprovacao

lista_nome = ["Nome:"]
lista_nota = ["Notas:"]
quantidade_nota = []
nota_total = 0

quan_alunos = int(input("Digite a quantidade de alunos: "))

for i in range (quan_alunos):

    lista_nota = []
    lista_nome = []
    nota_total = 0

    nome = str(input("Digite o nome do aluno: "))
    lista_nome.append(nome)

    notas = int(input("Digite a quantidade de notas: "))
    
    for y in range (notas): 
        notas1 = float(input("Digite as notas do aluno: "))
        if notas1 > 10:
            print ("Nota invalida, digite uma nota válida")
            continue 
        lista_nota.append(notas1)
        nota_total += notas1

    valordamedia = media(lista_nota)
    resultado_aprovacao = aprovacao(valordamedia)

    print(*lista_nome)
    print("------------------------------")
    print(*lista_nota)
    print("------------------------------")
    print("Soma das notas", nota_total)
    print("------------------------------")
    print("Media das notas: ", valordamedia)
    print("------------------------------")
    print("O boletim esta correto?: ", resultado_aprovacao)

    with open("result.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write("------------------------------\n")
        notas_texto = " ".join(map(str, lista_nota))
        arquivo.write(f"Notas: {notas_texto}\n")
        arquivo.write("------------------------------\n")
        arquivo.write(f"Soma das notas: {nota_total}\n")
        arquivo.write("------------------------------\n")
        arquivo.write(f"Media das notas: {valordamedia}\n")
        arquivo.write("------------------------------\n")
        arquivo.write(f"O boletim esta correto?: {resultado_aprovacao}\n")
        arquivo.write("\n")