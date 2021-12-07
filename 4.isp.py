"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC


class IJanelaFecha(ABC):
    def fechar(self):
        raise NotImplementedError


class IJanelaTamanhoVariavel(ABC):
    def maximizar(self):
        pass

    def minimizar(self):
        pass


class IJanelaComMenu(ABC):
    def mostrar_menu(self):
        pass


class JanelaTamanhoFixo(IJanelaFecha, IJanelaComMenu):
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass


class JanelaSemMenu(IJanelaFecha, IJanelaTamanhoVariavel):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass


