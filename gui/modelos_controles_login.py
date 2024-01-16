import flet as ft
import data.data_model as sgbd
import controladores.utils as util
from flet.security import decrypt
from dotenv import load_dotenv
import os

db = sgbd.SGBD()
load_dotenv()


class BotaoTextoLogin:
    def __init__(self, pagina: ft.Page, texto: str, do_tipo_login: bool = False,
                 usuario: ft.TextField = None, senha: ft.TextField = None):
        self._pagina = pagina
        self._texto = texto
        self._do_tipo_login = do_tipo_login
        self._usuario = usuario
        self._senha = senha
        self.item, self.item_container = self._item_botao()

    def _item_botao(self) -> tuple:
        if self._do_tipo_login:
            estilo = ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: ft.colors.PINK_ACCENT_700,
                    ft.MaterialState.DEFAULT: ft.colors.WHITE,
                },

                bgcolor={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.DEFAULT: ft.colors.PINK_ACCENT_700,
                },
                shape=ft.RoundedRectangleBorder(radius=10),
                animation_duration=500,
            )
        else:
            estilo = ft.ButtonStyle(
                color=ft.colors.WHITE,
                overlay_color='transparent'
            )

        item = ft.TextButton(
            text=self._texto,
            style=estilo,
            scale=2 if self._do_tipo_login else None,
            on_click=lambda e: self._ao_clicar_no_botao()
        )

        item_container = ft.Container(
            content=item
        )

        return item, item_container

    def _ao_clicar_no_botao(self):
        if self._do_tipo_login:
            usuario = self._usuario.value
            senha = self._senha.value
            dados_usuario = db.recuperar_registros(tabela='usuario', condicao=f"login_usuario = '{usuario}'")

            senha_hash = dados_usuario[0][3] if dados_usuario else []

            self._usuario.error_style = ft.TextStyle(color=ft.colors.PINK_500, weight=ft.FontWeight.BOLD)
            self._senha.error_style = ft.TextStyle(color=ft.colors.PINK_500, weight=ft.FontWeight.BOLD)

            self._usuario.error_text = 'insira o usuário' if usuario == '' else None
            self._senha.error_text = 'insira a senha' if senha == '' else None

            if usuario == '' or senha == '':
                self._pagina.update()
                return None

            if not senha_hash:
                util.mostrar_notificacao(page=self._pagina, mensagem='Opa! Usuário não encontrado, verifique novamente.'
                                                                     ' Caso você tenha algum problema, entre em contato'
                                                                     ' com o desenvolvedor', tipo='erro', emoji='🤔')
                self._senha.value = ''
                self._pagina.update()
                return None

            if senha == decrypt(senha_hash, os.getenv('CHAVE_DE_CODIFICACAO')):  # TYPE: IGNORE
                self._usuario.value = ''
                self._senha.value = ''

                os.environ["USER_ID"] = str(dados_usuario[0][0])
                os.environ["USER_NOME"] = str(dados_usuario[0][1])
                os.environ["USER_LOGIN"] = str(dados_usuario[0][2])
                os.environ["USER_SENHA_HASH"] = str(dados_usuario[0][3])
                os.environ["USER_EMAIL"] = str(dados_usuario[0][4])
                os.environ["USER_TELEFONE"] = str(dados_usuario[0][5])
                os.environ["USER_NIVEL_ACESSO"] = str(dados_usuario[0][6])

                self._pagina.go('/inicio')
                return True

            util.mostrar_notificacao(page=self._pagina, mensagem='Ops! A senha inserida está incorreta',
                                     tipo='erro', emoji='🤔')
            self._senha.value = ''
            self._pagina.update()
        else:
            pass


class CaixaDeFormularioLogin:
    def __init__(self, pagina: ft.Page, texto: str, altura_container: int, largura_container: int, cor_prefixo: str,
                 largura_caixa: int, altura_caixa: int, texto_de_prefixo: str, maiusculas: bool = False,
                 campo_de_senha: bool = False, autofoco: bool = False, pad_esquerda: int = 80, pad_direita: int = 80):
        self._pagina = pagina
        self._e_campo_de_senha = campo_de_senha
        self._autofoco = autofoco
        self._texto = texto
        self._altura_container = altura_container
        self._largura_container = largura_container
        self._pad_esquerda = pad_esquerda
        self._pad_direita = pad_direita
        self._largura_caixa = largura_caixa
        self._altura_caixa = altura_caixa
        self._texto_de_prefixo = texto_de_prefixo
        self._maiusculas = maiusculas
        self._cor_prefixo = cor_prefixo
        self.item, self.item_container = self._item_caixa()

    def _item_caixa(self) -> tuple:
        item = ft.TextField(
            password=self._e_campo_de_senha,
            can_reveal_password=True if self._e_campo_de_senha else None,
            autofocus=self._autofoco,
            width=self._largura_caixa,
            height=self._altura_caixa,
            border_color=ft.colors.PINK_ACCENT_700,
            border_width=2,
            border_radius=10,
            focused_border_width=3,
            focused_border_color=ft.colors.PINK_500,
            hint_text=self._texto,
            hint_style=ft.TextStyle(color=ft.colors.GREY_600),
            text_style=ft.TextStyle(color=ft.colors.PINK_50, size=20),
            prefix_text=self._texto_de_prefixo,
            prefix_style=ft.TextStyle(color=self._cor_prefixo, size=20),
            capitalization=ft.TextCapitalization.CHARACTERS if self._maiusculas else None,
            shift_enter=True,
        )

        item_container = ft.Container(
            expand=True,
            content=item,
            width=self._largura_container,
            height=self._altura_container,
        )

        return item, item_container
