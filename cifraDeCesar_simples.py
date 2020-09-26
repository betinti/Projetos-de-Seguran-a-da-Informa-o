caracter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

k = input("Digite a chave desejada para a criptografia: ")
C = input("Digite o texto a ser criptografado: ")

# Encontrar um determinado caracter na lista
def find(c):
    for i in range(len(caracter)):
        if c.lower() == caracter[i]:
            return i

# Encontrar um determinado index na lista
def get(n):
    if (n > len(caracter)):
        n = n - len(caracter)
    return caracter[n]

def cifrar():
    print("--- CIFRAR ---")
    chave = find(k[0])
    z = []
    for i in range(0,len(C)):
        z.append(get(find(C[i]) + int(chave)))
    T = ''.join(z)
    print(''.join(z)) ##concatena toda a lista novamente
    return T

T = cifrar()

def decifrar():
    print("--- DECIFRAR ---")
    chave = find(k[0])
    z = []
    for i in range(0, len(T)):
        z.append(get(find(T[i]) - int(chave)))
    print(''.join(z))  ##concatena toda a lista novamente
decifrar()
