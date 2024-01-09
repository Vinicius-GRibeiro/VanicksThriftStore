import flet as ft
import data.data_model as sgdb
import gui.view_vendas as vv
from datetime import datetime

db = sgdb.SGBD()


def redefinir_view_vendas_novo(pagina: ft.Page, tabela=None, caixas_de_pesquisa=None,
                               view: vv.ViewVendas | None = None, texto_cod_data_hora=None,
                               texto_cod=None, texto_timestamp=None, tabela_carrinho_de_compras=None,
                               valor_total=None):

    itens_caixa_de_pesquisa = view.caixas_de_pesquisa if view is not None else caixas_de_pesquisa if caixas_de_pesquisa is not None else None
    item_tabela = view.tabela_produtos if view is not None else tabela if tabela is not None else None
    cod_data_hora = view.texto_cod_data_hora if view is not None else texto_cod_data_hora
    codigo = view.cod_venda if view is not None else texto_cod
    timestamp_ = view.timestamp if view is not None else texto_timestamp
    tabela_carrinho = view.tabela_carrinho_de_compras if view is not None else tabela_carrinho_de_compras
    val_total = view.valor_total if view is not None else valor_total

    val_total.value = 0

    id_compra = db.recuperar_proximo_id('venda')
    timestamp = int(datetime.timestamp(datetime.now()))
    codigo.value = id_compra
    timestamp_.value = timestamp
    data = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
    cod_data_hora.value = f'COD. VENDA {id_compra} - DATA {data}'

    for caixa in itens_caixa_de_pesquisa:
        caixa.item.value = ''

    categorias = db.recuperar_registros(tabela='categoria', colunas='nome')

    itens_caixa_de_pesquisa[-1].item.options.clear()
    for categoria in categorias:
        itens_caixa_de_pesquisa[-1].item.options.append(ft.dropdown.Option(categoria[0]))

    if item_tabela is not None:
        produtos = db.recuperar_registros(tabela='produto')
        item_tabela._linhas_tabela.clear()
        for produto in produtos:
            item_tabela.adicionar_linha_tabela_produtos(dados=produto)

    if tabela_carrinho is not None:
        tabela_carrinho.linhas_tabela.clear()
        pagina.update()


def redefinir_view_vendas_consultar(pagina: ft.Page, view: vv.ViewVendas | None = None):
    pass
