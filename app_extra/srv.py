class Colaborador:
    def __init__(self, colaborador, salario) -> None:
        self.colaborador = colaborador
        self.salario = salario
        self.setor = None

    def calcular_irpf(self):
        imposto = 0.0
        taxas = (0.0, 7.5, 15.0, 22.5, 27.5)
        valores = (0.0, 1903.98, 2826.65, 3751.06, 4664.68)
        baseCalculo = self.salario
        
        for i in range(4, -1, -1):
            if baseCalculo > valores[i]:
                imposto += (baseCalculo - valores[i])* taxas[i] / 100
                baseCalculo = valores[i]
        return imposto
    
    def alocacao(self, setor):
        self.setor = setor