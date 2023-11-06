soma= 0
qtalunos= 0

while True:
    nota= float(input("Digite a nota do aluno:"))
    if nota == 999:
      break
    else:
      qtalunos +=1
      soma= soma + nota
print (f"A média geral da turma é de {soma/qtalunos:.2f}")