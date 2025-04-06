from Models.Funcionario import Funcionario

class Freelancer(Funcionario):
    def __init__(self, codigo, nome, diasTrabalhados, valordia):
        super().__init__(codigo, nome)
        self._diasTrabalhados = diasTrabalhados  
        self._valordia = valordia  

    def get_diasTrabalhados(self):
        return self._diasTrabalhados

    def set_diasTrabalhados(self, diasTrabalhados):
        self._diasTrabalhados = diasTrabalhados

    def get_valordia(self):
        return self._valordia

    def set_valordia(self, valordia):
        self._valordia = valordia

    def calcularSalario(self):
        return self._valordia * self._diasTrabalhados