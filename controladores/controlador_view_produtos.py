import gui.view_produtos as vp
import flet as ft
from data.data_model import SGBD

bdd = SGBD()


def atualizar_view_produtos_adicionar(pagina, view: vp.ViewProdutos | None = None, controles: list | None = None,
                                      botoes: list | None = None):
    tab = pagina.views[-1].controls[0].content.controls[1].controls[1].controls[0].content.controls[1].content.controls[
        1].content.controls[0].content.controls[0].content.controls[0]
    btn_add = \
        tab.tabs[0].content.content.controls[0].content.controls[0].controls[4].controls[0].content.content.controls[0]

    btn_add.disabled = False
    btn_add.icon_color = ft.colors.GREEN_800

    if view is not None:
        view.id_.item_caixa_de_texto.value = bdd.recuperar_proximo_id(tabela='produto')
        view.id_.item_caixa_de_texto.error_text = None

        view.nome_.item_caixa_de_texto.value = ''
        view.nome_.item_caixa_de_texto.error_text = None

        view.estoque_.item_caixa_de_texto.value = ''
        view.estoque_.item_caixa_de_texto.error_text = None

        view.preco_.item_caixa_de_texto.value = ''
        view.preco_.item_caixa_de_texto.error_text = None

        carregar_categorias_e_estados(caixa_categorias=view.categoria_.item_caixa_de_escolha,
                                      caixa_estados=view.estado_.item_caixa_de_escolha)

        view.estado_.item_caixa_de_escolha.error_text = None
        view.categoria_.item_caixa_de_escolha.error_text = None

        view.descricao_.item_caixa_de_texto.value = ''
        view.descricao_.item_caixa_de_texto.error_text = None

        view.botao_salvar_alteracoes_.item_btn_add.disabled = True
        view.botao_salvar_alteracoes_.item_btn_add.icon_color = ft.colors.GREY_700

        view.botao_excluir_produto_.item_btn_add.disabled = True
        view.botao_excluir_produto_.item_btn_add.icon_color = ft.colors.GREY_700

    elif controles is not None:
        if botoes is not None:
            botoes[0].diseabled = True
            botoes[0].icon_color = ft.colors.GREY_700
            botoes[1].diseabled = True
            botoes[1].icon_color = ft.colors.GREY_700

        categoria = None
        estado = None

        for c in controles:
            if c.label == 'Categoria':
                categoria = c
            if c.label == 'Estado':
                estado = c

            if c.label != '':
                c.value = ''
            else:
                c.value = bdd.recuperar_proximo_id(tabela='produto')

            c.error_text = None

        carregar_categorias_e_estados(caixa_categorias=categoria,
                                      caixa_estados=estado)

    pagina.update()


def atualizar_view_produtos_consultar(pagina, view: vp.ViewProdutos | None = None, controles: list | None = None):
    # TODO: IMPLEMENTAR CONSULTA NO BANCO E ADICIONAR DADOS NA LISTA
    produtos = bdd.recuperar_registros(tabela='produto')

    if view is not None:
        view.tabela_produtos.linhas_tabela.clear()
        for prod in produtos:
            view.tabela_produtos.adicionar_linha_tabela_produtos(prod)

        view.id_pesquisa_.item_caixa_de_texto.value = ''
        view.id_pesquisa_.item_caixa_de_texto.error_text = None
        view.nome_pesquisa_.item_caixa_de_texto.value = ''
        view.nome_pesquisa_.item_caixa_de_texto.error_text = None
        view.categoria_pesquisa_.item_caixa_de_escolha.value = ''
        view.categoria_pesquisa_.item_caixa_de_escolha.error_text = None
        view.estado_pesquisa_.item_caixa_de_escolha.value = ''
        view.estado_pesquisa_.item_caixa_de_escolha.error_text = None

        carregar_categorias_e_estados(caixa_categorias=view.categoria_pesquisa_.item_caixa_de_escolha,
                                      caixa_estados=view.estado_pesquisa_.item_caixa_de_escolha)
    elif controles is not None:
        categoria = None
        estado = None

        for c in controles:
            if c.label == 'Categoria':
                categoria = c
            if c.label == 'Estado':
                estado = c

            if c.label != '':
                c.value = ''
            else:
                c.value = bdd.recuperar_proximo_id(tabela='produto')

            c.error_text = None

        carregar_categorias_e_estados(caixa_categorias=categoria,
                                      caixa_estados=estado)

    pagina.update()


def carregar_categorias_e_estados(caixa_categorias: ft.Dropdown, caixa_estados: ft.Dropdown):
    categorias = bdd.recuperar_registros(tabela='categoria', colunas='nome')
    if categorias is not None:
        caixa_categorias.options.clear()
        for cat in categorias:
            caixa_categorias.options.append(
                ft.dropdown.Option(cat[0])
            )

    estados = bdd.recuperar_registros(tabela='estado', colunas='nome')
    if estados is not None:
        caixa_estados.options.clear()
        for estado in estados:
            caixa_estados.options.append(
                ft.dropdown.Option(estado[0])
            )


def passar_valores_para_pagina_no_modo_de_edicao(pagina: ft.Page, controles: list[ft.Control],
                                                 dados_: tuple, botoes: list[ft.Control]):
    controles[0].value = dados_[0]
    controles[1].value = dados_[1]
    controles[2].value = dados_[4]
    controles[3].value = dados_[2]
    controles[4].value = dados_[3]
    controles[5].value = dados_[6]
    controles[6].value = dados_[5]

    for botao in botoes:
        botao.disabled = False

    botoes[0].icon_color = ft.colors.LIME_500
    botoes[1].icon_color = ft.colors.RED_ACCENT_700

    tab = pagina.views[-1].controls[0].content.controls[1].controls[1].controls[0].content.controls[1].content.controls[
        1].content.controls[0].content.controls[0].content.controls[0]
    btn_add = \
        tab.tabs[0].content.content.controls[0].content.controls[0].controls[4].controls[0].content.content.controls[0]
    btn_add.disabled = True
    btn_add.icon_color = ft.colors.GREY_700
    tab.selected_index = 0
    pagina.update()
