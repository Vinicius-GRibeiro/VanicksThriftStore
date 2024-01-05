import flet as ft
from abc import ABC, abstractmethod
import controladores.utils as util
from data.data_model import SGBD
import controladores.controlador_view_produtos as ctrl_vp

bdd = SGBD()


class CaixaDeTexto:
    def __init__(self, texto: str, texto_de_dica: str | None = None, altura_item: int = 70,
                 altura: int = 70, largura: int = 100, filtro: ft.InputFilter | None = None,
                 pad_cima: int = 5, pad_baixo: int = 5, pad_direita: int = 5, pad_esquerda: int = 5,
                 disabled: bool = False, preenchido: bool = False, estilo_texto: bool = False,
                 tamanho_fonte: int = 20, centralizado: bool = False, bold: bool = False):
        self.texto = texto
        self.texto_de_dica = texto_de_dica
        self.altura = altura if altura >= altura_item else altura_item - 100
        self.largura = largura
        self.pad_cima = pad_cima
        self.pad_baixo = pad_baixo
        self.pad_direita = pad_direita
        self.pad_esquerda = pad_esquerda
        self.filtro = filtro
        self.altura_item = altura_item
        self.disabled = disabled
        self.preenchido = preenchido
        self.estilo_texto = estilo_texto
        self.tamanho_fonte = tamanho_fonte
        self.centralizado = centralizado
        self.bold = bold
        self.item_caixa_de_texto, self.item_caixa_de_texto_container = self._item_caixa_de_texto()

    def _item_caixa_de_texto(self):
        item = ft.TextField(
            label=self.texto,
            hint_text=self.texto_de_dica,
            input_filter=self.filtro,
            height=self.altura_item,
            disabled=self.disabled,
            filled=self.preenchido,
            border_color=ft.colors.PINK_900,
            border_width=2,
            border_radius=30,
            text_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=self.tamanho_fonte,
                weight=ft.FontWeight.BOLD,
            ),
            label_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.PINK_900,
            ),
            focused_border_color=ft.colors.PINK_700,
            focused_border_width=3
        )

        if self.bold:
            item.text_style = ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=self.tamanho_fonte,
                weight=ft.FontWeight.BOLD
            )

        if self.centralizado:
            item.text_align = ft.TextAlign.CENTER

        item_container = ft.Container(
            width=self.largura,
            height=self.altura,
            padding=ft.padding.only(top=self.pad_cima, right=self.pad_direita,
                                    bottom=self.pad_baixo, left=self.pad_esquerda),
            content=item
        )

        return item, item_container


class CaixaDeEscolha:
    def __init__(self, texto: str,
                 altura: int = 70, largura: int = 100, altura_item: int = 70,
                 pad_cima: int = 5, pad_baixo: int = 5, pad_direita: int = 5, pad_esquerda: int = 5):
        self.texto = texto
        self.altura_item = altura_item
        self.altura = altura if altura >= altura_item else altura_item - 100
        self.largura = largura
        self.pad_cima = pad_cima
        self.pad_baixo = pad_baixo
        self.pad_direita = pad_direita
        self.pad_esquerda = pad_esquerda
        self.item_caixa_de_escolha, self.item_caixa_de_escolha_container = self._item_caixa_de_escolha()

    def _item_caixa_de_escolha(self):
        item = ft.Dropdown(
            label=self.texto,
            height=self.altura_item,
            border_color=ft.colors.PINK_900,
            border_width=2,
            border_radius=30,
            text_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=20,
                weight=ft.FontWeight.BOLD
            ),
            label_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.PINK_900,
            ),
            focused_border_color=ft.colors.PINK_700,
            focused_border_width=3
        )

        item_container = ft.Container(
            width=self.largura,
            height=self.altura,
            padding=ft.padding.only(top=self.pad_cima, right=self.pad_direita,
                                    bottom=self.pad_baixo, left=self.pad_esquerda),
            content=item
        )

        return item, item_container


class _Botao(ABC):
    def __init__(self, pagina: ft.Page, controles: list[ft.Control] = None,
                 icone: str | None = None, cor: str | None = None, texto: str | None = None,
                 altura: int = 70, largura: int = 100, pad_cima: int = 5,
                 pad_baixo: int = 5, pad_direita: int = 5, pad_esquerda: int = 5,
                 botoes: list | None = None):
        self.pagina = pagina
        self.icone = icone
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.pad_cima = pad_cima
        self.pad_baixo = pad_baixo
        self.pad_direita = pad_direita
        self.pad_esquerda = pad_esquerda
        self.texto = texto
        self.controles = controles
        self.botoes = botoes

    @abstractmethod
    def ao_clicar(self, e):
        pass


class BotaoAdicionarVIEWPRODUTO(_Botao):
    def __init__(self, pagina: ft.Page, controles: list[ft.Control], botoes: list | None = None):
        super().__init__(pagina=pagina, controles=controles)
        self.item_btn_add = self._item_btn_adicionar_vp()

    def _item_btn_adicionar_vp(self):
        btn = ft.IconButton(
            icon=ft.icons.ADD_ROUNDED,
            icon_size=50,
            icon_color=ft.colors.GREEN_800,
            on_click=self.ao_clicar
        )

        return btn

    def ao_clicar(self, e):
        if util.verificar_se_existem_campos_vazios(self.pagina, controles=self.controles):
            nome = self.controles[1].value
            categoria = self.controles[2].value
            quantidade = int(self.controles[3].value)
            preco = float(self.controles[4].value)
            descricao = self.controles[5].value if self.controles[5].value != '' else None
            estado = self.controles[6].value

            valido = bdd.inserir_registros(tipo='produto', prod_nome=nome, prod_categoria=categoria,
                                           prod_quantidade=quantidade, prod_preco=preco, prod_descricao=descricao,
                                           prod_estado=estado)

            if valido:
                ctrl_vp.atualizar_view_produtos_adicionar(pagina=self.pagina, controles=self.controles,
                                                          botoes=self.botoes)
                self.pagina.go('/')
                self.pagina.go('/produtos')
                util.mostrar_notificacao(page=self.pagina, mensagem='Produto adicionado', tipo='exito', emoji='✅')
            else:
                util.mostrar_notificacao(page=self.pagina, mensagem='Ops! Ocorreu um erro ao tentar adicionar '
                                                                    'o produto', tipo='erro', emoji='😬')


class BotaoSalvarAlteracoesVIEWPRODUTO(_Botao):
    def __init__(self, pagina: ft.Page, controles: list[ft.Control]):
        super().__init__(pagina=pagina, controles=controles)
        self.item_btn_add = self._item_btn_adicionar_vp()

    def _item_btn_adicionar_vp(self):
        btn = ft.IconButton(
            icon=ft.icons.NOTE_ADD,
            icon_size=50,
            icon_color=ft.colors.GREY_700,
            on_click=self.ao_clicar
        )

        return btn

    def ao_clicar(self, e):
        if util.verificar_se_existem_campos_vazios(self.pagina, controles=self.controles):
            id_prod = self.controles[0].value
            nome = self.controles[1].value
            categoria = self.controles[2].value
            quantidade = int(self.controles[3].value)
            preco = float(self.controles[4].value)
            descricao = self.controles[5].value if self.controles[5].value != '' else None
            estado = self.controles[6].value

            valido = bdd.editar_registros_produto(prod_id=id_prod, prod_nome=nome, prod_preco=preco, prod_estado=estado,
                                                  prod_categoria=categoria, prod_descricao=descricao,
                                                  prod_quantidade=quantidade, condicao=f'id = {id_prod}')
            if valido:
                ctrl_vp.atualizar_view_produtos_adicionar(pagina=self.pagina, controles=self.controles,
                                                          botoes=self.botoes)
                self.pagina.go('/')
                self.pagina.go('/produtos')
                util.mostrar_notificacao(page=self.pagina, mensagem='Tudo certo! Alterações realizadas',
                                         tipo='exito', emoji='✅')
            else:
                util.mostrar_notificacao(page=self.pagina, mensagem='Ops! Ocorreu um erro ao tentar editar o produto',
                                         tipo='erro', emoji='😬')


class BotaoExcluirVIEWPRODUTO(_Botao):
    def __init__(self, pagina: ft.Page, controles: list[ft.Control]):
        super().__init__(pagina=pagina, controles=controles)
        self.item_btn_add = self._item_btn_adicionar_vp()

    def _item_btn_adicionar_vp(self):
        btn = ft.IconButton(
            icon=ft.icons.CLEAR_ROUNDED,
            icon_size=50,
            icon_color=ft.colors.GREY_700,
            on_click=self.ao_clicar
        )

        return btn

    def ao_clicar(self, e):

        id_prod = self.controles[0].value
        nome = self.controles[1].value
        categoria = self.controles[2].value
        quantidade = int(self.controles[3].value)
        preco = float(self.controles[4].value)
        descricao = self.controles[5].value
        estado = self.controles[6].value

        valido = bdd.deletar_registro(tabela='produto', condicao=f'id = {id_prod}')

        if valido:
            ctrl_vp.atualizar_view_produtos_adicionar(pagina=self.pagina, controles=self.controles,
                                                      botoes=self.botoes)
            util.mostrar_notificacao(page=self.pagina, mensagem='Pronto! Produto excluido',
                                     tipo='exito', emoji='✅')
            self.pagina.go('/')
        else:
            util.mostrar_notificacao(page=self.pagina, mensagem='Ops! Ocorreu um erro ao tentar excluir o produto',
                                     tipo='erro', emoji='😬')


class BotaoConsultasVIEWPRODUTO:
    def __init__(self, pagina: ft.Page, icone: str, cor: str, tipo: str, controles: list[ft.Control]):
        self.pagina = pagina
        self.icone = icone
        self.cor = cor
        self.tipo = tipo
        self.controles = controles
        self.item_btn_consulta_vp = self._item_btn_consulta_vp()

    def _item_btn_consulta_vp(self):
        return ft.IconButton(
            icon=self.icone,
            icon_size=35,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: self.cor,
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                },
                overlay_color=self.cor
            ),
            on_click=self.ao_clicar
        )

    def ao_clicar(self, e):

        match self.tipo:
            case 'consultar':
                id_, id_valor_ = self.controles[0], self.controles[0].value
                nome, nome_valor = self.controles[1], self.controles[1].value
                categoria, categoria_valor = self.controles[2], self.controles[2].value
                estado, estado_valor = self.controles[3], self.controles[3].value
                tabela = self.controles[4]

                invalido = id_valor_ == '' and nome_valor == '' and categoria_valor == '' and estado_valor == ''
                if invalido:
                    util.mostrar_notificacao(page=self.pagina, mensagem='Ops! Você não aplicou nenhum filtro a pesquisa'
                                             , emoji='😅')
                    return None

                id_condicao = f'id = {id_valor_}'
                nome_condicao = f"nome LIKE '%{nome_valor}%'"
                categoria_condicao = f"categoria = '{categoria_valor}'"
                estado_condicao = f"estado = '{estado_valor}'"

                condicao_geral = ''

                if nome_valor != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += nome_condicao

                if id_valor_ != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += id_condicao
                    else:
                        condicao_geral += f' AND {id_condicao}'

                if categoria_valor != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += categoria_condicao
                    else:
                        condicao_geral += f' AND {categoria_condicao}'

                if estado_valor != '':
                    if len(condicao_geral) == 0:
                        condicao_geral += estado_condicao
                    else:
                        condicao_geral += f' AND {estado_condicao}'

                registros = bdd.recuperar_registros(tabela='produto', condicao=condicao_geral)

                if registros:
                    tabela.item_tabela_produtos.rows.clear()

                    produtos = bdd.recuperar_registros(tabela='produto', condicao=condicao_geral)
                    for produto in produtos:
                        tabela.adicionar_linha_tabela_produtos(produto)
                    self.pagina.update()
                else:
                    util.mostrar_notificacao(page=self.pagina, mensagem='Parece que não existe nenhum produto'
                                                                        ' com os filtros inseridos', emoji='😵')
            case 'resetar':
                id_ = self.controles[0]
                nome = self.controles[1]
                categoria = self.controles[2]
                estado = self.controles[3]
                tabela = self.controles[4]

                id_.value = ''
                nome.value = ''
                categoria.value = ''
                estado.value = ''

                tabela.item_tabela_produtos.rows.clear()

                produtos = bdd.recuperar_registros(tabela='produto')
                for produto in produtos:
                    tabela.adicionar_linha_tabela_produtos((produto))
                self.pagina.update()


class TabelaProdutos:
    def __init__(self, pagina: ft.Page,
                 controles: list[ft.Control] | None = None,
                 botoes: list[ft.Control] | None = None):
        self.pagina = pagina
        self.controles = controles
        self.botoes = botoes
        self.linhas_tabela: list[ft.DataRow] = []
        self.item_tabela_produtos = self._item_tabela_produtos()

    def _item_tabela_produtos(self) -> ft.DataTable:
        tabela = ft.DataTable(
            width=800,
            divider_thickness=1,
            border_radius=30,
            horizontal_lines=ft.BorderSide(1, ft.colors.GREY_700),
            border=ft.Border(bottom=ft.BorderSide(2, ft.colors.PINK_ACCENT_700)),
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
                self.coluna_tabela_produtos(titulo_coluna='ID'),
                self.coluna_tabela_produtos(titulo_coluna='Nome'),
                self.coluna_tabela_produtos(titulo_coluna='Qntd.'),
                self.coluna_tabela_produtos(titulo_coluna='R$'),
                self.coluna_tabela_produtos(titulo_coluna='Categoria'),
                self.coluna_tabela_produtos(titulo_coluna='Estado'),
                self.coluna_tabela_produtos(titulo_coluna='Descrição'),
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
        linha = ft.DataRow(
            on_select_changed=lambda e: ctrl_vp.passar_valores_para_pagina_no_modo_de_edicao(pagina=self.pagina,
                                                                                             controles=self.controles,
                                                                                             dados_=dados,
                                                                                             botoes=self.botoes),
            cells=[
                ft.DataCell(ft.Text(value=dados[0])),
                ft.DataCell(ft.Text(value=dados[1])),
                ft.DataCell(ft.Text(value=dados[2])),
                ft.DataCell(ft.Text(value=dados[3])),
                ft.DataCell(ft.Text(value=dados[4])),
                ft.DataCell(ft.Text(value=dados[5])),
                ft.DataCell(ft.Text(value=dados[6])),
            ]
        )

        self.linhas_tabela.append(linha)
        self.pagina.update()
