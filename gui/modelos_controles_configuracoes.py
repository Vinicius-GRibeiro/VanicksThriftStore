import flet as ft


class Abas:
    def __init__(self, pagina: ft.Page, conteudo_tab_1: ft.Container, conteudo_tab_2: ft.Container,
                 conteudo_tab_3: ft.Container, conteudo_tab_4: ft.Container, conteudo_tab_5: ft.Container):
        self.conteudo_tab_1 = conteudo_tab_1
        self.conteudo_tab_2 = conteudo_tab_2
        self.conteudo_tab_3 = conteudo_tab_3
        self.conteudo_tab_4 = conteudo_tab_4
        self.conteudo_tab_5 = conteudo_tab_5
        self.tabs, self.tabs_container = self._retornar_tabs()

    def _retornar_tabs(self):
        tabs = ft.Tabs(
            indicator_tab_size=False,
            selected_index=0,
            divider_color='transparent',
            tabs=[
                ft.Tab(content=self.conteudo_tab_1),
                ft.Tab(content=self.conteudo_tab_2),
                ft.Tab(content=self.conteudo_tab_3),
                ft.Tab(content=self.conteudo_tab_4),
                ft.Tab(content=self.conteudo_tab_5)
            ]
        )

        tabs_container = ft.Container(
            width=800,
            height=600,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        width=800,
                        height=600,
                        content=ft.Stack(
                            controls=[
                                tabs,
                                ft.Container(  # Cabeçalho da página de vendas
                                    bgcolor=ft.colors.PINK_500,
                                    width=800,
                                    height=50,
                                    alignment=ft.alignment.center,
                                    border_radius=20,
                                    border=ft.border.only(
                                        top=ft.BorderSide(5, ft.colors.PINK_ACCENT_700),
                                        right=ft.BorderSide(5, ft.colors.PINK_ACCENT_700)
                                    ),
                                    content=ft.Text(
                                        value='CONFIGURAÇÕES',
                                        text_align=ft.TextAlign.CENTER,
                                        size=25,
                                        weight=ft.FontWeight.BOLD,
                                        color='white'
                                    )
                                ),
                            ]
                        )
                    )
                ]
            )
        )

        return tabs, tabs_container


class BotaoParaOSubMenu:
    def __init__(self, pagina: ft.Page, icone: str, texto: str, tamanho_icone: int, tamanho_texto: int, tabs: Abas):
        self._pagina = pagina
        self._icone = icone
        self._texto = texto
        self._tamanho_icone = tamanho_icone
        self._tamanho_texto = tamanho_texto
        self._tabs = tabs
        self.item_container = self._item_botao()

    def _item_botao(self):
        botao = ft.IconButton(
            on_click=lambda _: self._ao_clicar_no_botao(),
            icon=self._icone,
            icon_size=self._tamanho_icone,
            icon_color=ft.colors.WHITE
        )

        item_container = ft.Container(
            on_click=lambda _: self._ao_clicar_no_botao(),
            on_hover=lambda e: self._destacar_botao(e),
            width=100,
            height=100,
            border_radius=20,
            content=ft.Column(
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    botao,
                    ft.Text(
                        value=self._texto,
                        size=self._tamanho_texto,
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD
                    ),

                ]
            )
        )

        return item_container

    def _ao_clicar_no_botao(self):
        match self._texto:
            case 'Conta':
                self._tabs.tabs.selected_index = 0
            case 'Geral':
                self._tabs.tabs.selected_index = 1
            case 'Relatórios':
                self._tabs.tabs.selected_index = 2
            case 'Usuários':
                self._tabs.tabs.selected_index = 3
            case 'DEV':
                self._tabs.tabs.selected_index = 4
        self._pagina.update()

    def _destacar_botao(self, e):
        if e.data == 'true':
            e.control.bgcolor = ft.colors.with_opacity(0.3, ft.colors.WHITE)
            e.control.update()
            e.control.content.controls[0].icon_color = ft.colors.WHITE
            e.control.content.controls[1].color = ft.colors.WHITE
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = ft.colors.WHITE
            e.control.content.controls[1].color = ft.colors.WHITE
            e.control.content.update()


class CaixaDeTextoBordaUnica:
    def __init__(self, pagina: ft.Page, label: str, largura_caixa: int, largura_container: int, altura_caixa: int,
                 altura_container: int,
                 texto_dica: str = None, destacar: bool = False):
        self._pagina = pagina
        self._label = label
        self._texto_dica = texto_dica
        self._largura_caixa = largura_caixa
        self._largura_container = largura_container
        self._altura_caixa = altura_caixa
        self._altura_container = altura_container
        self._destacar = destacar
        self.item, self.item_container = self._item_caixa()

    def _item_caixa(self):
        item = ft.TextField(
            label=self._label,
            border=ft.InputBorder('underline'),
            border_color=ft.colors.PINK_ACCENT_700,
            focused_border_color=ft.colors.PINK_ACCENT_700,
            content_padding=ft.padding.only(bottom=10),
            hint_text=self._texto_dica,
            width=self._largura_caixa,
            height=self._altura_caixa,
            label_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                weight=ft.FontWeight.BOLD,
                size=20
            ),
            text_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=20
            )
        )

        item_container = ft.Container(
            bgcolor='blue' if self._destacar else None,
            content=item,
            width=self._largura_container,
            height=self._altura_container,
        )

        return item, item_container
