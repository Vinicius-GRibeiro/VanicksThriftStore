from datetime import datetime
from pprint import pprint

import flet as ft
import data.data_model as sgdb
import controladores.utils as util
import controladores.controlador_view_vendas as ctrl_vv
import re

db = sgdb.SGBD()


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
    def __init__(self, label: str, icone_prefixo: str, altura: int = 45, largura: int = 150, tamanho_texto: int = 12,
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
    def __init__(self, label: str, icone_prefixo: str, altura: int = 45, largura: int = 150, tamanho_texto: int = 12,
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
                 pad_cima: int = 0, pad_baixo: int = 0, pad_direita: int = 0, pad_esquerda: int = 0,
                 filtros_texto=None, filtro_cancelados=None):
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
        self._filtros_texto = filtros_texto
        self._filtro_cancelados = filtro_cancelados
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
                ft.DataCell(ft.Text(value=f'{dados[0]} {dados[1]}')),
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
        linhas_produtos = []
        estilo_botao_fechar = ft.ButtonStyle(
            side=ft.BorderSide(1, ft.colors.PINK_ACCENT_700),
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PINK_ACCENT_700
        )
        estilo_botao_cancelar_compra = ft.ButtonStyle(
            side=ft.BorderSide(1, ft.colors.GREY_700) if dados[3] == 'cancelado' else ft.BorderSide(1,
                                                                                                    ft.colors.PINK_ACCENT_700),
            color=ft.colors.GREY_700 if dados[3] == 'cancelado' else ft.colors.PINK_ACCENT_700,
        )
        estilo_botao_deletar_registros = ft.ButtonStyle(
            side=ft.BorderSide(1, ft.colors.PINK_ACCENT_700),
            color=ft.colors.PINK_ACCENT_700,
        )

        for prod in dados[-1]:
            linhas_produtos.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=prod[0])),
                        ft.DataCell(ft.Text(value=prod[1])),
                        ft.DataCell(ft.Text(value=prod[2])),
                        ft.DataCell(ft.Text(value=prod[3])),
                        ft.DataCell(ft.Text(value=prod[4])),
                        ft.DataCell(ft.Text(value=prod[5])),
                    ]
                )
            )

        return ft.Banner(
            bgcolor=ft.colors.GREY_50,
            leading=ft.Container(
                content=ft.Icon(name=ft.icons.RECEIPT_LONG_ROUNDED, size=100, color=ft.colors.PINK_ACCENT_700)),
            content=ft.Column(controls=[
                ft.Row(controls=[
                    ft.Text(value='Cód. da venda: ', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[0], size=20, color=ft.colors.BLACK),

                    ft.Container(bgcolor=ft.colors.PINK_ACCENT_700, width=1, height=25),

                    ft.Text(value='Data e hora: ', size=20, color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[1], size=20, color=ft.colors.BLACK),

                    ft.Container(bgcolor=ft.colors.PINK_ACCENT_700, width=1, height=25),

                    ft.Text(value='Total: R$ ', size=20, color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[2], size=20, color=ft.colors.BLACK),

                    ft.Container(bgcolor=ft.colors.PINK_ACCENT_700, width=1, height=25),

                    ft.Text(value='Status: ', size=20, color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value=dados[3], size=20, color=ft.colors.BLACK),

                ]),

                ft.Container(height=2, width=1000, bgcolor=ft.colors.PINK_ACCENT_700),

                ft.Row(controls=[
                    ft.DataTable(
                        width=1000,
                        heading_row_height=30,
                        heading_row_color=ft.colors.PINK_ACCENT_700,
                        data_row_max_height=25,
                        data_row_min_height=25,
                        heading_text_style=ft.TextStyle(
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD
                        ),
                        columns=[
                            ft.DataColumn(label=ft.Text(value='Cód. produto')),
                            ft.DataColumn(label=ft.Text(value='Nome')),
                            ft.DataColumn(label=ft.Text(value='Preço R$')),
                            ft.DataColumn(label=ft.Text(value='Categoria')),
                            ft.DataColumn(label=ft.Text(value='Estado')),
                            ft.DataColumn(label=ft.Text(value='Descrição')),
                        ],
                        rows=linhas_produtos
                    )
                ])
            ]),
            actions=[
                ft.Row(controls=[ft.Container(padding=ft.padding.only(top=15, bottom=15))]),

                ft.Row(controls=[
                    ft.Container(
                        width=1350,
                        alignment=ft.alignment.center_right,
                        padding=ft.padding.only(bottom=15),
                        content=ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                            ft.OutlinedButton(text='Cancelar compra', style=estilo_botao_cancelar_compra,
                                              icon=ft.icons.BLOCK_ROUNDED,
                                              on_click=lambda e: self._ao_clicar_cancelar_compra(dados),
                                              disabled=True if dados[3] == 'cancelado' else False),

                            ft.OutlinedButton(text='Deletar registro', style=estilo_botao_deletar_registros,
                                              icon=ft.icons.DELETE_ROUNDED,
                                              on_click=lambda e: self._ao_clicar_deletar_registro(dados),
                                              disabled=True if dados[3] == 'cancelado' else False),

                            ft.Container(width=850),

                            ft.OutlinedButton(text='Fechar', style=estilo_botao_fechar,
                                              icon=ft.icons.CLOSE_ROUNDED,
                                              on_click=lambda e: self._ao_clicar_fechar()),
                        ])
                    )
                ])
            ],
        )

    def _ao_clicar_fechar(self):
        self._pagina.banner.open = False
        self._pagina.update()

    def _ao_clicar_cancelar_compra(self, dados):
        estilo_botoes = ft.ButtonStyle(color=ft.colors.PINK_ACCENT_700)
        dlg_confirmacao = ft.AlertDialog(
            title=ft.Text(value='Por favor, confirme'),
            content=ft.Text(value='Você deseja realmente cancelar a compra? Está ação não poderá ser desfeita'),
            actions=[
                ft.TextButton(text='Sim, cancelar compra', style=estilo_botoes, on_click=lambda e: cancelar_compra()),
                ft.TextButton(text='Não', style=estilo_botoes, on_click=lambda e: abrir_fechar_dialogo(abrir=False)),
            ]
        )

        def abrir_fechar_dialogo(abrir: bool):
            self._pagina.dialog = dlg_confirmacao
            dlg_confirmacao.open = abrir
            self._pagina.update()

        abrir_fechar_dialogo(abrir=True)

        def cancelar_compra():
            exito = db.marcar_venda_como_cancelada(id_venda=dados[0], produtos=dados[-1])
            abrir_fechar_dialogo(abrir=False)
            self._ao_clicar_fechar()

            if not exito:
                util.mostrar_notificacao(page=self._pagina, mensagem='Houve um erro ao cancelar venda',
                                         tipo='erro', emoji='😬')
            else:
                util.mostrar_notificacao(page=self._pagina, mensagem='Venda cancelada', tipo='exito', emoji='✔')
                ctrl_vv.redefinir_view_vendas_consultar(pagina=self._pagina, tabela_=self,
                                                        filtros_caixa_de_texto=self._filtros_texto,
                                                        filtro_cancelados=self._filtro_cancelados)

    def _ao_clicar_deletar_registro(self, dados):
        ...


class BotaoPadraConsulta:
    def __init__(self, pagina: ft.Page, tipo: str, icone: str, cor_padrao: str, tamanho_icone: int,
                 tabela: TabelaProdutosConsultar = None, filtros_texto=None, filtro_cancelados=None):
        self._pagina = pagina
        self._tipo = tipo
        self._icone = icone
        self._cor_padrao = cor_padrao
        self._tamanho_icone = tamanho_icone
        self._tabela = tabela
        self._filtro_texto = filtros_texto
        self._filtro_cancelados = filtro_cancelados
        self.item = self._item_botao()

    def _item_botao(self):
        botao = ft.IconButton(
            icon=self._icone,
            icon_color=self._cor_padrao,
            icon_size=self._tamanho_icone,
            on_click=lambda e: self._ao_clicar_no_botao()
        )

        return botao

    def _ao_clicar_no_botao(self):
        match self._tipo:
            case 'consultar':
                self._ao_clicar_no_botao_consulta_de_filtros()
            case 'resetar':
                ctrl_vv.redefinir_view_vendas_consultar(pagina=self._pagina, tabela_=self._tabela,
                                                        filtros_caixa_de_texto=self._filtro_texto,
                                                        filtro_cancelados=self._filtro_cancelados)

    def _ao_clicar_no_botao_consulta_de_filtros(self):
        padrao_data = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

        val_data_inicial = self._filtro_texto[0].item.value
        val_data_final = self._filtro_texto[1].item.value
        val_valor_inicial = self._filtro_texto[2].item.value
        val_valor_final = self._filtro_texto[3].item.value
        cancelado = self._filtro_cancelados.value

        condicao_filtro_vendas = ''

        if val_data_inicial != '' and val_data_final != '':
            if re.match(padrao_data, val_data_inicial) and re.match(padrao_data, val_data_final):
                data_inicial_timestamp = int(datetime.strptime(val_data_inicial, "%d/%m/%Y").timestamp())
                data_final_timestamp = int(datetime.strptime(val_data_final, "%d/%m/%Y").timestamp())
                condicao_filtro_vendas += f'data_hora >= {data_inicial_timestamp} AND data_hora <= {data_final_timestamp}'

        if val_valor_inicial != '' and val_valor_final != '':
            if len(condicao_filtro_vendas) < 1:
                condicao_filtro_vendas += f'valor_total >= {val_valor_inicial} AND valor_total <= {val_valor_final}'
            else:
                condicao_filtro_vendas += f' AND valor_total >= {val_valor_inicial} AND valor_total <= {val_valor_final}'

        if cancelado:
            if len(condicao_filtro_vendas) < 1:
                condicao_filtro_vendas += f"status = 'cancelado'"
            else:
                condicao_filtro_vendas += f" AND status = 'cancelado'"

        vendas_filtradas = db.recuperar_registros(tabela='venda', condicao=condicao_filtro_vendas)

        self._tabela._linhas_tabela.clear()
        if vendas_filtradas is not None:
            for venda in vendas_filtradas:
                id_venda = venda[0]
                produtos_da_venda = db.recuperar_registros(tabela='itens_venda', condicao=f'id_venda = {id_venda}',
                                                           colunas='id_produto, nome, preco, categoria, estado, descricao')
                venda_editado = list(venda)
                venda_editado[1] = datetime.fromtimestamp(venda_editado[1]).strftime("%d/%m/%Y %H:%M")
                venda_e_produto = list(venda_editado)
                venda_e_produto.append(tuple(produtos_da_venda))

                self._tabela.adicionar_linha_tabela_produtos(tuple(venda_e_produto))

