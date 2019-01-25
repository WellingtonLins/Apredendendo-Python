class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


regis = Pessoa('Regis')    #regis e uma instancia de pessoa
print(regis)          
fabio = Pessoa('Fabio')    #fabio e outra instancia de pessoa
print(fabio)              