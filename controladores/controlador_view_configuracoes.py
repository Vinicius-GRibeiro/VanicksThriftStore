import flet as ft
import gui.view_configuracoes as vc
from dotenv import load_dotenv
import os

load_dotenv()


def resetar_aba_conta(pagina: ft.Page, view: vc.ViewConfiguracoes = None, caixas_de_texto: [ft.Control] = None):
    caixas_texto = view.contas_controles if view is not None else caixas_de_texto
    chaves = ['USER_ID', 'USER_NOME', 'USER_LOGIN', 'USER_EMAIL',
              'USER_TELEFONE', 'USER_NIVEL_ACESSO']
    for index, caixa in enumerate(caixas_texto):
        caixa.value = os.getenv(chaves[index])

    pagina.update()
