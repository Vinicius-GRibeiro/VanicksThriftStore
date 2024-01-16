from dotenv import load_dotenv
from flet.security import encrypt, decrypt
import os
import flet as ft


class MinhaCaixaDeTexto:
    def __init__(self, max_length: int, aligment: QT.Aligment, text: str):  # Insira o restante dos atributos
        # Seus atributos. Aqui são só exemplos
        self._max_length = max_length
        self._aligment = aligment
        self._text = text
        ...

        #Atributo que possui o seu objeto QLineEdit
        self.minha_caixa_de_texto = self._criar_caixa_de_texto()

    def _criar_caixa_de_texto(self):
        # Aqui você chama o modelo que instancia o objeto QLineEdit, com os atributos
        # definidos lá em cima. Esse objeto é o retorno desse método, então o atributo
        # minha_caixa_de_texto vai possuir o objeto. Quando quiser usar, é só instanciar essa classe
        # MinhaCaixaDeTexto e chamar o atributo minha_caixa_de_texto dela.
        return '''
                Aqui você criar a sua caixa normalmente, como já cria com o QT. Essa função retornará
                esse objeto.
                Aqui você também define o textChanged para a chamada da função que deixa a letra
                maiúscula, o self._sua_funcao_que_deixa_a_letra_maiuscula().
                '''

    def _sua_funcao_que_deixa_a_letra_maiuscula(self):
        ...


minha_caixa = MinhaCaixaDeTexto('atributos')
