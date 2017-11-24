def soma(num1, num2):
    return num1 + num2

def dec_mostra_soma(func):
    def nova_func(num1, num2):
        return "Resultado: " + str(func(num1, num2))
    return nova_func

resultado = dec_mostra_soma(soma)

print(resultado(2, 4))

#############

def dec_mostra_sub(func):
    def nova_func(num1, num2):
        return "Resultado: " + str(func(num1, num2))
    return nova_func

@dec_mostra_sub
def sub(num1, num2):
    return num1 - num2

print(sub(2, 1)) 