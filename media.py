notas = [7, 8, 6, 10, 5]

s = 0

for i in range(len(notas)):
    s = s + notas[i]

media = s / len(notas)

print("Média final:", media)
