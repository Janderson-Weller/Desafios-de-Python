class Salario:
    def __init__(self, salario, h_extra, faltas): #salario, hora extra
        self.SALARIO = salario
        self.H_EXTRA = h_extra
        self.FALTAS = faltas

    def feriado(self, feriados):
        if feriados == 'S' or 's':
            return True
        elif feriados == 'N' or 'n':
            return False
        else:
            print("Informação inválida")

    def extra(self):
        vl_hora = 4.5 #valor de uma hora extra em dia normal 50%
        vl_total_h  =  self.H_EXTRA * vl_hora #valor total das horas
        return vl_total_h
