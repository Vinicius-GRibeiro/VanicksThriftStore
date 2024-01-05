import flet as ft
import data.data_model as sgdb
import gui.view_vendas as vv

db = sgdb.SGBD()


def redefinir_view_vendas_novo(pagina: ft.Page, tabela=None, caixas_de_pesquisa=None,
                               view: vv.ViewVendas | None = None):

    itens_caixa_de_pesquisa = view.caixas_de_pesquisa if view is not None else caixas_de_pesquisa if caixas_de_pesquisa is not None else None
    item_tabela = view.tabela_produtos if view is not None else tabela if tabela is not None else None

    for caixa in itens_caixa_de_pesquisa:
        caixa.item.value = ''

    categorias = db.recuperar_registros(tabela='categoria', colunas='nome')

    itens_caixa_de_pesquisa[-1].item.options.clear()
    for categoria in categorias:
        itens_caixa_de_pesquisa[-1].item.options.append(ft.dropdown.Option(categoria[0]))

    if tabela is not None:
        tabela.item_tabela_produtos.rows.clear()
        produtos = db.recuperar_registros(tabela='produto')
        for produto in produtos:
            tabela.adicionar_linha_tabela_produtos(produto)


    pagina.update()


def redefinir_view_vendas_consultar(pagina: ft.Page, view: vv.ViewVendas | None = None):
    pass
