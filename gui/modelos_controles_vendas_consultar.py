import flet as ft

class TextoPadrao:
    def __init__(self, texto: str, container_largura: int, container_altura: int,
                 tamanho_texto: int = 15, cor_texto: str = ft.colors.PINK_ACCENT_700,
                 peso: bool = False, destacar_container: bool = False):
        self._texto = texto
        self._tamanho_texto = tamanho_texto
        self._cor_texto = cor_texto
        self._peso = peso
        self._container_largura = container_largura
        self._container_altura = container_altura
        self._destacar_container = destacar_container
        self.item, self.item_container = self._item_texto_padrao()

    def _item_texto_padrao(self):
        item = ft.Text(
            value=self._texto,
            size=self._tamanho_texto,
            color=self._cor_texto,
            weight=ft.FontWeight.BOLD if self._peso else None
        )

        item_container = ft.Container(
            height=self._container_altura,
            width=self._container_largura,
            bgcolor='blue' if self._destacar_container else None,
            content=item
        )

        return item, item_container


class CaixaDeTextoPadraoCONSULTA:
    def __init__(self, label: str, icone_prefixo:str, altura: int = 45, largura: int = 150, tamanho_texto: int = 12,
                 tamanho_label: int = 12, cor_padrao: str = ft.colors.PINK_ACCENT_700):
        self._label = label
        self._icone_prefixo = icone_prefixo
        self._altura = altura
        self._largura = largura
        self._tamanho_texto = tamanho_texto
        self._tamanho_label = tamanho_label
        self._cor_padrao = cor_padrao
        self.item, self.item_container = self._item_caixa_de_texto_conuslta()

    def _item_caixa_de_texto_conuslta(self):
        item = ft.TextField(
            width=self._largura,
            height=self._altura,
            label=self._label,
            label_style=ft.TextStyle(
                size=self._tamanho_label,
                weight=ft.FontWeight.BOLD,
                color=self._cor_padrao
            ),
            text_style=ft.TextStyle(
                size=self._tamanho_texto,
                color=self._cor_padrao,
                weight=ft.FontWeight.BOLD
            ),
            border_color=self._cor_padrao,
            border_radius=5,
            prefix_icon=self._icone_prefixo,
            prefix_style=ft.TextStyle(
                color=self._cor_padrao
            )
        )

        item_container = ft.Container(
            content=item,
            width=self._largura,
            height=self._altura
        )

        return item, item_container


class CaixaDeEscolhaPadraoCONSULTA:
    def __init__(self, label: str, icone_prefixo:str, altura: int = 45, largura: int = 150, tamanho_texto: int = 12,
                 tamanho_label: int = 12, cor_padrao: str = ft.colors.PINK_ACCENT_700):
        self._label = label
        self._icone_prefixo = icone_prefixo
        self._altura = altura
        self._largura = largura
        self._tamanho_texto = tamanho_texto
        self._tamanho_label = tamanho_label
        self._cor_padrao = cor_padrao
        self.opcoes_dropdow = []
        self.item, self.item_container = self._item_caixa_de_texto_conuslta()

    def _item_caixa_de_texto_conuslta(self):
        item = ft.Dropdown(
            width=self._largura,
            height=self._altura,
            label=self._label,
            label_style=ft.TextStyle(
                size=self._tamanho_label,
                weight=ft.FontWeight.BOLD,
                color=self._cor_padrao
            ),
            text_style=ft.TextStyle(
                size=self._tamanho_texto,
                color=self._cor_padrao,
                weight=ft.FontWeight.BOLD
            ),
            border_color=self._cor_padrao,
            border_radius=5,
            prefix_icon=self._icone_prefixo,
            prefix_style=ft.TextStyle(
                color=self._cor_padrao
            ),
            options=self.opcoes_dropdow
        )

        item_container = ft.Container(
            content=item,
            width=self._largura,
            height=self._altura
        )

        return item, item_container


class TabelaProdutosConsultar:
    def __init__(self, pagina: ft.Page, largura_tabela: int = 500, altura_cabecalho: int = 50,
                 altura_caixa_e_container: int = 500, largura_caixa_container: int = 450,
                 pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0):
        self._pagina = pagina
        self._altura_caixa_e_container = altura_caixa_e_container
        self._largura_caixa_e_container = largura_caixa_container
        self._largura_tabela = largura_tabela
        self._linhas_tabela: list[ft.DataRow] = []
        self._altura_cabecalho = altura_cabecalho
        self._pad_cima = pad_cima
        self._pad_baixo = pad_baixo
        self._pad_direita = pad_direita
        self._pad_esquerda = pad_esquerda
        self.item, self.item_container = self._item_tabela_produtos()

    def _item_tabela_produtos(self):
        item = ft.DataTable(
            width=self._largura_tabela,
            heading_row_height=self._altura_cabecalho,
            data_row_min_height=self._altura_cabecalho,
            data_row_max_height=self._altura_cabecalho,
            divider_thickness=1,
            horizontal_lines=ft.BorderSide(1, ft.colors.GREY_700),
            border=ft.Border(top=ft.BorderSide(2, ft.colors.PINK_ACCENT_700),
                             right=ft.BorderSide(2, ft.colors.PINK_ACCENT_700),
                             bottom=ft.BorderSide(2, ft.colors.PINK_ACCENT_700),
                             left=ft.BorderSide(2, ft.colors.PINK_ACCENT_700)),
            border_radius=ft.BorderRadius(bottom_left=30, bottom_right=30, top_left=0, top_right=0),
            heading_row_color=ft.colors.PINK_ACCENT_700,
            heading_text_style=ft.TextStyle(
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
            ),
            data_text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                size=12
            ),
            columns=[
                self._coluna_tabela_produtos(titulo_coluna='Data'),
                self._coluna_tabela_produtos(titulo_coluna='Total R$.'),
                self._coluna_tabela_produtos(titulo_coluna='Status'),
                self._coluna_tabela_produtos(titulo_coluna='Produtos'),
            ],
            rows=self._linhas_tabela
        )

        item_container = ft.Container(
            padding=ft.padding.only(
                top=self._pad_cima,
                bottom=self._pad_baixo,
                left=self._pad_esquerda,
                right=self._pad_direita
            ),
            width=self._largura_caixa_e_container,
            content=item,
            alignment=ft.alignment.top_center,
        )

        return item, item_container

    @staticmethod
    def _coluna_tabela_produtos(titulo_coluna: str) -> ft.DataColumn:
        return ft.DataColumn(
            label=ft.Text(value=titulo_coluna)
        )

    def adicionar_linha_tabela_produtos(self, dados: tuple):
        linha = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(value=dados[1])),
                ft.DataCell(ft.Text(value=dados[2])),
                ft.DataCell(ft.Text(value=dados[3])),
                ft.DataCell(ft.Text(value=dados[4])),
            ],
            on_select_changed=lambda e: self._ao_clicar_no_produto(dados=dados),
        )

        self._linhas_tabela.append(linha)
        self._pagina.update()

    def _ao_clicar_no_produto(self, dados):
        self._pagina.banner = self._banner(dados)
        self._pagina.banner.open = True
        self._pagina.update()

    def _banner(self, dados):
        return ft.Banner(
            bgcolor=ft.colors.PINK_50,
            leading=ft.Container(content=ft.Icon(name=ft.icons.RECEIPT_LONG_ROUNDED, size=100, color=ft.colors.PINK_ACCENT_700)),
            content=ft.Column(controls=[
                ft.Row(controls=[
                    ft.Text(value='Cód. da compra: ', size=20, color=ft.colors.PINK_ACCENT_700, weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[0], size=20, color=ft.colors.PINK_ACCENT_700),

                    ft.Container(bgcolor=ft.colors.PINK_ACCENT_700, width=1, height=25),

                    ft.Text(value='Data e hora: ', size=20, color=ft.colors.PINK_ACCENT_700,
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[1], size=20, color=ft.colors.PINK_ACCENT_700),

                    ft.Container(bgcolor=ft.colors.PINK_ACCENT_700, width=1, height=25),

                    ft.Text(value='Total: R$ ', size=20, color=ft.colors.PINK_ACCENT_700,
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[2], size=20, color=ft.colors.PINK_ACCENT_700),

                    ft.Container(bgcolor=ft.colors.PINK_ACCENT_700, width=1, height=25),

                    ft.Text(value='Status: ', size=20, color=ft.colors.PINK_ACCENT_700,
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[3], size=20, color=ft.colors.PINK_ACCENT_700),

                ]),

                ft.Container(height=2, width=1000, bgcolor=ft.colors.PINK_ACCENT_700),

                ft.Row(controls=[
                    # TODO: LISTA DE ITENS COMPRADOS
                ])
            ]),
            actions=[
                ft.TextButton(text='Fechar'),
                ft.TextButton(text='Cancelar compra'),
                ft.TextButton(text='Deletar dos registros'),
            ]
        )
