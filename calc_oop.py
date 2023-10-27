class Calc:
    def somar(self, a, b):
        print(f"A Soma e: {a+b}")        
    def subtracao(self, a, b):
         print(f"A Subtração e: {a-b}")
    def multiplicacao(self, a, b):
         print(f"A Multiplicação é: {a*b}")
    def divisao(self, a, b):
         print(f"A Divisão é: {a/b}")
    
    def exec_calc(self):
        print("=="*20)
        print(" ")
    
calculadora = Calc()

calculadora.somar(20,20)
calculadora.subtracao(20,20)
calculadora.multiplicacao(20,20)
calculadora.divisao(20,20)


