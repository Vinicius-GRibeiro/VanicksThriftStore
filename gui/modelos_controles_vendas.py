import flet as ft
import controladores.controlador_view_vendas as ctrl_vv
import data.data_model as sgbd
import controladores.utils as util

db = sgbd.SGBD()


class BotaoParaOSubMenu:
    def __init__(self, texto: str, icone: str, rota: str, pagina: ft.Page, tabs: ft.Tabs,
                 caixas_de_pesquisa=None, cod_data_hora=None, texto_cod=None, texto_timestamp=None,
                 valor_total=None, tabela_vendas_consulta=None, filtros_texto=None, filtros_escolha=None,
                 filtro_cancelados=None):
        self._texto = texto
        self._icone = icone
        self._rota = rota
        self._pagina = pagina
        self._tabs = tabs
        self._texto_cod = texto_cod
        self._texto_timestamp = texto_timestamp
        self._caixas_de_pesquisa = caixas_de_pesquisa
        self._cod_data_hora = cod_data_hora
        self._valor_total = valor_total
        self._tabela_vendas_consulta = tabela_vendas_consulta
        self._filtros_texto = filtros_texto
        self._filtros_escolha = filtros_escolha
        self._filtro_cancelados = filtro_cancelados
        self.botao = self._retornar_botao_com_container(texto_do_botao=self._texto, icone_do_botao=self._icone,
                                                        rota=self._rota)

    def _retornar_botao_com_container(self, texto_do_botao: str, icone_do_botao: str, rota: str) -> ft.Container:
        return ft.Container(
            padding=ft.padding.only(top=9),
            width=100,
            height=100,
            border_radius=20,
            on_click=lambda _: self._ao_clicar_no_botao(),
            on_hover=lambda e: self._destacar_botao(e),
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=9, right=9),
                        content=ft.IconButton(
                            icon=icone_do_botao,
                            expand=False,
                            icon_size=36,
                            icon_color=ft.colors.WHITE,
                            style=ft.ButtonStyle(
                                shape={
                                    '': ft.RoundedRectangleBorder(radius=14),
                                },
                                overlay_color={
                                    '': 'transparent',
                                }
                            ),
                        ),
                    ),

                    ft.Container(
                        content=ft.Text(
                            value=texto_do_botao,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=15,
                            opacity=1,
                            animate_opacity=200,
                        ),
                    )
                ]
            )
        )

    def _ao_clicar_no_botao(self):
        if self._rota == 'novo':
            self._tabs.selected_index = 0
            ctrl_vv.redefinir_view_vendas_novo(pagina=self._pagina, caixas_de_pesquisa=self._caixas_de_pesquisa,
                                               tabela=None, texto_cod_data_hora=self._cod_data_hora,
                                               texto_cod=self._texto_cod, texto_timestamp=self._texto_timestamp,
                                               valor_total=self._valor_total)

        elif self._rota == 'consultar':
            self._tabs.selected_index = 1
            ctrl_vv.redefinir_view_vendas_consultar(pagina=self._pagina, tabela_=self._tabela_vendas_consulta,
                                                    filtros_caixa_de_texto=self._filtros_texto,
                                                    filtro_cancelados=self._filtro_cancelados)

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


class DivisorHorizontal:
    def __init__(self, tamanho_container: int = 100, cor: str = ft.colors.PINK_300, espessura: int = 2,
                 pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0):
        self._tamanho_container = tamanho_container
        self._cor = cor
        self._espessura = espessura
        self._pad_cima = pad_cima
        self._pad_baixo = pad_baixo
        self._pad_direita = pad_direita
        self._pad_esquerda = pad_esquerda

        self.divisor = self._divisor()

    def _divisor(self):
        return ft.Container(
            width=self._tamanho_container,
            padding=ft.padding.only(
                top=self._pad_cima,
                bottom=self._pad_baixo,
                left=self._pad_esquerda,
                right=self._pad_direita
            ),

            content=ft.Divider(
                color=self._cor,
                thickness=self._espessura
            )
        )


class Tabs_:
    def __init__(self, pagina: ft.Page, conteudo_tabs_1_: ft.Container, conteudo_tabs_2_: ft.Container):
        self.conteudo_tabs_1_ = conteudo_tabs_1_
        self.conteudo_tabs_2_ = conteudo_tabs_2_
        self.tabs, self.tabs_container = self._retornar_tabs()

    def _retornar_tabs(self):
        tabs = ft.Tabs(
            indicator_tab_size=False,
            selected_index=0,
            divider_color='transparent',
            tabs=[
                ft.Tab(content=self.conteudo_tabs_1_),
                ft.Tab(content=self.conteudo_tabs_2_)
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
                                        value='VENDAS',
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


class TextoParaTitutlos:
    def __init__(self, label: str, tamanho_do_texto: int = 20, cor_do_texto: str = ft.colors.PINK_ACCENT_700,
                 peso: bool = True, pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0,
                 altura_container: int = 60, largura_container: int = 100, alinhamento_container: str = 'centro'):
        self._label = label
        self._tamanho_do_texto = tamanho_do_texto
        self._cor_do_texto = cor_do_texto
        self._peso = peso
        self._pad_cima = pad_cima
        self._pad_baixo = pad_baixo
        self._pad_direita = pad_direita
        self._pad_esquerda = pad_esquerda
        self._altura_container = altura_container
        self._largura_container = largura_container
        self._alinhamento_container = alinhamento_container
        self.item, self.item_container = self._retornar_texto()

    def _retornar_texto(self):
        item = ft.Text(
            value=self._label,
            size=self._tamanho_do_texto,
            color=self._cor_do_texto,
            weight=ft.FontWeight.BOLD if self._peso else None,
        )

        item_container = ft.Container(
            alignment=ft.alignment.center if self._alinhamento_container == 'centro' else None,
            width=self._largura_container,
            height=self._altura_container,
            padding=ft.padding.only(
                top=self._pad_cima,
                bottom=self._pad_baixo,
                right=self._pad_direita,
                left=self._pad_esquerda
            ),
            content=item
        )

        return item, item_container


class CaixaDeTextoPadrao:
    def __init__(self, label: str, altura_caixa_e_container: int = 70, largura_caixa_container: int = 100,
                 tamanho_do_texto: int = 15, fino: bool = False,
                 pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0,
                 alinhamento_do_texto_no_no_centro: bool = False, tipo_teclado: ft.KeyboardType=None):
        self._label = label
        self._altura_caixa_e_container = altura_caixa_e_container
        self._largura_caixa_container = largura_caixa_container
        self._tamanho_do_texto = tamanho_do_texto
        self._fino = fino
        self._pad_cima = pad_cima
        self._pad_baixo = pad_baixo
        self._pad_direita = pad_direita
        self._pad_esquerda = pad_esquerda
        self._tipo_teclado = tipo_teclado
        self._alinhamento_do_texto_no_no_centro = alinhamento_do_texto_no_no_centro

        self.item, self.item_container = self._item_caixa()

    def _item_caixa(self):
        item = ft.TextField(
            width=self._largura_caixa_container,
            height=self._altura_caixa_e_container,
            label=self._label,
            border_radius=50,
            border_color=ft.colors.PINK_ACCENT_700,
            focused_border_color=ft.colors.PINK_500,
            border_width=1 if self._fino else 2,
            focused_border_width=2 if self._fino else 3,
            text_align=ft.TextAlign.CENTER if self._alinhamento_do_texto_no_no_centro else None,
            label_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.PINK_900,
            ),
            text_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=self._tamanho_do_texto,
                weight=ft.FontWeight.BOLD,
            ),
        )

        if self._tipo_teclado is not None:
            item.keyboard_type = self._tipo_teclado

        item_container = ft.Container(
            padding=ft.padding.only(
                top=self._pad_cima,
                bottom=self._pad_baixo,
                left=self._pad_esquerda,
                right=self._pad_direita
            ),
            height=self._altura_caixa_e_container,
            width=self._largura_caixa_container,
            content=item,
            alignment=ft.alignment.top_center
        )

        return item, item_container


class CaixaDeEscolha:
    def __init__(self, label: str, altura_caixa_e_container: int = 70, largura_caixa_container: int = 100,
                 tamanho_do_texto: int = 15, fino: bool = False,
                 pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0,
                 alinhamento_do_texto_no_no_centro: bool = False):
        self._label = label
        self._altura_caixa_e_container = altura_caixa_e_container
        self._largura_caixa_e_container = largura_caixa_container
        self._tamanho_do_texto = tamanho_do_texto
        self._fino = fino
        self._pad_cima = pad_cima
        self._pad_baixo = pad_baixo
        self._pad_direita = pad_direita
        self._pad_esquerda = pad_esquerda
        self.item, self.item_container = self._item_caixa_de_escolha()

    def _item_caixa_de_escolha(self):
        item = ft.Dropdown(
            height=self._altura_caixa_e_container,
            width=self._largura_caixa_e_container,
            label=self._label,
            border_radius=50,
            border_color=ft.colors.PINK_ACCENT_700,
            focused_border_color=ft.colors.PINK_500,
            border_width=1 if self._fino else 2,
            focused_border_width=2 if self._fino else 3,
            label_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.PINK_900,
            ),
            text_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=self._tamanho_do_texto,
                weight=ft.FontWeight.BOLD,
            ),
        )

        item_container = ft.Container(
            padding=ft.padding.only(
                top=self._pad_cima,
                bottom=self._pad_baixo,
                left=self._pad_esquerda,
                right=self._pad_direita
            ),
            height=self._altura_caixa_e_container,
            width=self._largura_caixa_e_container,
            content=item,
            alignment=ft.alignment.top_center
        )

        return item, item_container


class TabelaCarrinhoDeCompras:
    def __init__(self, pagina: ft.Page, altura: int, valor_total: ft.TextField = None):
        self.pagina = pagina
        self.altura = altura
        self.linhas_tabela: list[ft.DataRow] = []
        self.item_tabela = self._item_tabela_produtos()
        self._valor_total = valor_total
        self.ids_produtos_utilizados = []

    def _item_tabela_produtos(self) -> ft.DataTable:
        tabela = ft.DataTable(
            heading_text_style=ft.TextStyle(size=10, weight=ft.FontWeight.BOLD),
            data_text_style=ft.TextStyle(size=10),
            divider_thickness=1,
            horizontal_lines=ft.BorderSide(width=5, color=ft.colors.YELLOW_ACCENT_100),
            column_spacing=70,
            heading_row_height=45,
            data_row_max_height=45,
            data_row_min_height=45,
            columns=[
                self.coluna_tabela_produtos(titulo_coluna='Cód.'),
                self.coluna_tabela_produtos(titulo_coluna='Prod.'),
                self.coluna_tabela_produtos(titulo_coluna='Qntd.'),
                self.coluna_tabela_produtos(titulo_coluna='Total'),
            ],
            rows=self.linhas_tabela
        )

        return tabela

    @staticmethod
    def coluna_tabela_produtos(titulo_coluna: str) -> ft.DataColumn:
        return ft.DataColumn(
            label=ft.Text(value=titulo_coluna)
        )

    def adicionar_linha_tabela_produtos(self, dados: tuple):
        self.ids_produtos_utilizados.append(dados[0])

        if dados[2] <= 0:
            return None

        linha = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(value=dados[0])),  # cod
                ft.DataCell(ft.Text(value=dados[1])),  # nome
                ft.DataCell(ft.Text(value=f'{dados[2]}x')),  # qntd
                ft.DataCell(ft.Text(value=f'R${dados[3]:.2f}')),  # val total
            ],
            on_select_changed=lambda e: self.ao_clicar_no_produto_do_carrinho(dados=dados)
        )

        self.linhas_tabela.append(linha)
        self.pagina.update()

    def ao_clicar_no_produto_do_carrinho(self, dados: tuple):
        indice = 0
        for linha in self.linhas_tabela:
            if linha.cells[0].content.value == dados[0]:
                break
            indice += 1

        self.ids_produtos_utilizados.remove(dados[0])
        self.linhas_tabela.pop(indice)

        self._valor_total.value = round(float(self._valor_total.value) - dados[-1], 2)
        self.pagina.update()


class TabelaProdutos:
    def __init__(self, pagina: ft.Page, largura_tabela: int = 500, altura_cabecalho: int = 45,
                 altura_caixa_e_container: int = 70, largura_caixa_container: int = 100,
                 pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0,
                 carrinho_compras: TabelaCarrinhoDeCompras = None, valor_total: ft.TextField = None):
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
        self._carrinho_de_compras = carrinho_compras
        self._valor_total = valor_total
        self.item, self.item_container = self._item_tabela_produtos()

    def _item_tabela_produtos(self):
        item = ft.DataTable(
            width=self._largura_tabela,
            heading_row_height=self._altura_cabecalho,
            data_row_min_height=self._altura_cabecalho,
            data_row_max_height=self._altura_cabecalho,
            divider_thickness=1,
            horizontal_lines=ft.BorderSide(1, ft.colors.GREY_700),
            border=ft.Border(bottom=ft.BorderSide(2, ft.colors.PINK_ACCENT_700)),
            border_radius=30,
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
                self._coluna_tabela_produtos(titulo_coluna='ID'),
                self._coluna_tabela_produtos(titulo_coluna='Nome'),
                self._coluna_tabela_produtos(titulo_coluna='Qntd.'),
                self._coluna_tabela_produtos(titulo_coluna='R$'),
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
        if dados[2] <= 0:
            return None

        linha = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(value=dados[0])),
                ft.DataCell(ft.Text(value=dados[1])),
                ft.DataCell(ft.Text(value=dados[2])),
                ft.DataCell(ft.Text(value=dados[3])),
            ],
            on_select_changed=lambda e: self._ao_clicar_no_produto(dados=dados)
        )

        self._linhas_tabela.append(linha)
        self._pagina.update()

    def _ao_clicar_no_produto(self, dados: tuple):
        id_ = dados[0]
        nome = dados[1]
        qntd_total = dados[2]
        val = dados[3]

        if qntd_total <= 0:
            return None

        self._carrinho_de_compras.adicionar_linha_tabela_produtos(dados=(id_, nome, 1, val))
        self._valor_total.value = round(float(self._valor_total.value) + val, 2)
        self._pagina.update()


class BotaoIconePadrao:
    def __init__(self, pagina: ft.Page, icone: str, tipo: str, tabela: TabelaProdutos = None,
                 itens_pesquisa: [CaixaDeTextoPadrao, CaixaDeEscolha] = None, tamanho_icone: int = 10,
                 cor_do_icone: str = ft.colors.PINK_ACCENT_700):
        self._pagina = pagina
        self._icone = icone
        self._tipo = tipo
        self._tabela = tabela
        self._itens_pesquisa = itens_pesquisa
        self._tamanho_icone = tamanho_icone
        self._cor_do_icone = cor_do_icone
        self.item, self.item_container = self._item_botao()

    def _item_botao(self):
        item = ft.IconButton(
            icon=self._icone,
            icon_size=self._tamanho_icone,
            icon_color=self._cor_do_icone,
            on_click=lambda _: self.ao_clicar()
        )

        item_container = ft.Container(
            content=item
        )

        return item, item_container

    def ao_clicar(self):
        match self._tipo:
            case 'consultar':
                id_produto = self._itens_pesquisa[0].item.value
                nome_produto = self._itens_pesquisa[1].item.value
                categoria_produto = self._itens_pesquisa[2].item.value

                invalido = id_produto == '' and nome_produto == '' and categoria_produto == ''
                if invalido:
                    util.mostrar_notificacao(page=self._pagina,
                                             mensagem='Ops! Você não aplicou nenhum filtro a pesquisa', emoji='😅')
                    return None

                id_condicao = f'id = {id_produto}'
                nome_condicao = f"nome LIKE '%{nome_produto}%'"
                categoria_condicao = f"categoria = '{categoria_produto}'"

                condicao_geral = ''

                if nome_produto != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += nome_condicao

                if id_produto != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += id_condicao
                    else:
                        condicao_geral += f' AND {id_condicao}'

                if categoria_produto != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += categoria_condicao
                    else:
                        condicao_geral += f' AND {categoria_condicao}'

                registros = db.recuperar_registros(tabela='produto', condicao=condicao_geral)

                if registros:
                    self._tabela._linhas_tabela.clear()
                    for reg in registros:
                        self._tabela.adicionar_linha_tabela_produtos(dados=reg)
                        for item_ in self._itens_pesquisa:
                            item_.item.value = ''
                    return None

                util.mostrar_notificacao(page=self._pagina, mensagem='Parece que não existe nenhum produto'
                                                                     ' com os filtros inseridos', emoji='😵')
                for item_ in self._itens_pesquisa:
                    item_.item.value = ''
            case 'redefinir':
                self._tabela._linhas_tabela.clear()
                registros = db.recuperar_registros(tabela='produto')

                for item_ in self._itens_pesquisa:
                    item_.item.value = ''

                for reg in registros:
                    self._tabela.adicionar_linha_tabela_produtos(reg)

        self._pagina.update()


class BotaoTextoPadrao:
    def __init__(self, pagina: ft.Page, texto: str, tipo: str, tabela: TabelaCarrinhoDeCompras = None,
                 tabela_produtos: TabelaProdutos = None,
                 itens_pesquisa: [CaixaDeTextoPadrao, CaixaDeEscolha] = None, tamanho_icone: int = 10,
                 cor_do_icone: str = ft.colors.PINK_500, icone: str = None,
                 tamanho_texto: int = 15, cor_do_texto: str = 'black', largura: int = 50, altura: int = 25,
                 cod_venda=None, timestamp_venda=None, item_cod_data_hota=None, campo_valor_total=None):
        self._pagina = pagina
        self._texto = texto
        self._icone = icone
        self._tipo = tipo
        self._tabela = tabela
        self._tabela_produtos = tabela_produtos
        self._itens_pesquisa = itens_pesquisa
        self._tamanho_icone = tamanho_icone
        self._cor_do_icone = cor_do_icone if icone is not None else None
        self._tamanho_texto = tamanho_texto
        self._cor_do_texto = cor_do_texto
        self._altura = altura
        self._largura = largura
        self._item_cod_data_hota = item_cod_data_hota
        self._cod_venda = cod_venda
        self._timestamp_venda = timestamp_venda
        self._campo_valor_total = campo_valor_total
        self.item, self.item_container = self._item_botao_texto()

    def _item_botao_texto(self):
        conteudo = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)

        if self._icone is not None:
            conteudo.controls.append(
                ft.Icon(name=self._icone, size=self._tamanho_icone)
            )

        conteudo.controls.append(
            ft.Text(value=self._texto, weight=ft.FontWeight.BOLD, size=self._tamanho_texto),
        )

        item = ft.TextButton(
            content=conteudo,
            width=self._largura,
            height=self._altura,

            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: ft.colors.WHITE,
                    ft.MaterialState.HOVERED: self._cor_do_texto,
                },
                bgcolor={
                    ft.MaterialState.DEFAULT: self._cor_do_texto,
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                }
            ),
            on_click=lambda e: self.ao_clicar_no_botao()
        )

        item_container = ft.Container(
            content=item,
            width=self._largura,
            height=self._altura,
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=10)
        )

        return item, item_container

    def ao_clicar_no_botao(self):
        match self._tipo:
            case 'finalizar_compra':
                if len(self._tabela.ids_produtos_utilizados) < 1:
                    util.mostrar_notificacao(page=self._pagina, mensagem='Ops! O carrinho está vazio. '
                                                                         'Adicione pelo menos um item para finalizar '
                                                                         'a compra',
                                             emoji='😢')
                    return None

                id_venda = self._cod_venda.value
                timestamp_venda = self._timestamp_venda.value
                produtos = []
                val_total = 0

                for cod_prod in self._tabela.ids_produtos_utilizados:
                    produto = db.recuperar_registros(tabela='produto', condicao=f'id = {cod_prod}')
                    produtos.append(produto[0])

                exito = True

                for produto in produtos:
                    val_total += produto[3]
                    exito = db.inserir_registros(tipo='venda_item', iv_id_venda=id_venda, iv_nome=produto[1],
                                                 iv_qntd_anterior=produto[2],
                                                 iv_estado=produto[5], iv_preco=produto[3],
                                                 iv_categoria=produto[4], iv_descricao=produto[6],
                                                 iv_id_produto=produto[0])

                    exito = db.editar_registros_produto(prod_id=produto[0], prod_nome=produto[1],
                                                        prod_quantidade=produto[2] - 1,
                                                        prod_estado=produto[5], prod_preco=produto[3],
                                                        prod_categoria=produto[4],
                                                        prod_descricao=produto[6], condicao=f'id = {produto[0]}')

                exito = db.inserir_registros(tipo='venda', venda_data_hora=timestamp_venda,
                                             venda_valor_total=round(val_total, 2))

                if exito:
                    util.mostrar_notificacao(page=self._pagina, mensagem='Oba! Venda realizada', tipo='exito', emoji='🥳')
                    ctrl_vv.redefinir_view_vendas_novo(pagina=self._pagina, tabela=self._tabela_produtos, tabela_carrinho_de_compras=self._tabela,
                                                       caixas_de_pesquisa=self._itens_pesquisa, texto_cod_data_hora=self._item_cod_data_hota,
                                                       texto_cod=self._cod_venda, texto_timestamp=self._timestamp_venda,
                                                       valor_total=self._campo_valor_total)
                    return True

                util.mostrar_notificacao(page=self._pagina, mensagem='Houve um erro ao realizar venda', tipo='erro', emoji='💔')

class TextoPadraoDoResumoDaCompra:
    def __init__(self, texto: str, tamanho: int = 10, bold: bool = False):
        self._texto = texto
        self._tamanho = tamanho
        self._bold = bold
        self.item_texto = self._item_texto()

    def _item_texto(self):
        return ft.Text(
            value=self._texto,
            size=self._tamanho,
            weight=ft.FontWeight.BOLD if self._bold else None
        )
