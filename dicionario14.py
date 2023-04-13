students = {
    'joão': {
        'idade': 18,
        'cidade': 'São Paulo',
        'notas': [7.5, 8.0, 9.0]
    },
    'Maria': {
        'idade': 20,
        'cidade': 'Rio de Janeiro',
        'notas': [6.5, 7.0, 8.5]
    },
    'Pedro': {
        'idade': 19,
        'cidade': 'Belo Horizonte',
        'notas': [8.0, 8.5, 9.5]
    }
}

#Imprimir a idade de Joao
print("A idade de joao é: " +str(students['joão']['idade']))
#adicionar uma nova nota para maria
students['Maria']['notas'].append(9.0)
# imprimir todas as informações dos alunos
for student, info in students.items():
    print(student + ':')
    print('idade: ' + str(info['idade']))
    print('cidade: ' + info['cidade'])
    print('Notas: ' + str(info['notas']))
    print('Media: ' + str(sum(info['notas'])))
    print()
          
    
    
    