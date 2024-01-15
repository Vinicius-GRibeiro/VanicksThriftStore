import flet as ft


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
            capitalization=ft.TextCapitalization.CHARACTERS if self._maiusculas else None
        )

        item_container = ft.Container(
            expand=True,
            content=item,
            width=self._largura_container,
            height=self._altura_container,
        )

        return item, item_container


class BotaoTextoLogin:
    def __init__(self, pagina: ft.Page, texto: str, do_tipo_login: bool = False):
        self._pagina = pagina
        self._texto = texto
        self._do_tipo_login = do_tipo_login
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
            self._pagina.go('/inicio')
        else:
            pass
