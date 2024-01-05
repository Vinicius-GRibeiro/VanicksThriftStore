import flet as ft
import gui.fabrica_de_views as fv
import gui.modelos_controles_vendas as mcv

largura = 720 * 1.9
altura = 405 * 1.9


class ViewVendas:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina

        self.pesquisa_produto_cod = mcv.CaixaDeTextoPadrao(label='Cód.', pad_cima=30, pad_esquerda=20,
                                                           tamanho_do_texto=12)
        self.pesquisa_produto_nome = mcv.CaixaDeTextoPadrao(label='Nome', pad_cima=30, largura_caixa_container=130,
                                                            tamanho_do_texto=12)
        self.pesquisa_produto_categoria = mcv.CaixaDeEscolha(label='Categoria', pad_cima=30,
                                                             largura_caixa_container=130, tamanho_do_texto=12)
        self.tabela_produtos = mcv.TabelaProdutos(pagina=self.pagina, largura_tabela=400, altura_cabecalho=40,
                                                  largura_caixa_container=400, altura_caixa_e_container=350,
                                                  pad_esquerda=20)
        self.caixas_de_pesquisa = [self.pesquisa_produto_cod,
                                   self.pesquisa_produto_nome,
                                   self.pesquisa_produto_categoria]
        self.pesquisa_produto_botao_pesquisar = mcv.BotaoIconePadrao(pagina=self.pagina, tamanho_icone=20,
                                                                     icone=ft.icons.SEARCH_ROUNDED,
                                                                     cor_do_icone=ft.colors.INDIGO_800,
                                                                     tipo='consultar',
                                                                     tabela=self.tabela_produtos,
                                                                     itens_pesquisa=self.caixas_de_pesquisa)
        self.pesquisa_produto_botao_resetar = mcv.BotaoIconePadrao(pagina=self.pagina, tamanho_icone=20,
                                                                   icone=ft.icons.AUTORENEW_ROUNDED,
                                                                   cor_do_icone=ft.colors.RED_600, tipo='redefinir',
                                                                   tabela=self.tabela_produtos,
                                                                   itens_pesquisa=self.caixas_de_pesquisa)


        # Atributos daqui para baixo, devem ser os últimos
        self.tabs_cru = mcv.Tabs_(pagina=self.pagina, conteudo_tabs_1_=self.conteudo_tabs_1(),
                                  conteudo_tabs_2_=self.conteudo_tabs_2())
        self.botao_submenu_novo = mcv.BotaoParaOSubMenu(texto='Nova       ', icone=ft.icons.POINT_OF_SALE_ROUNDED,
                                                        rota='novo', pagina=self.pagina, tabs=self.tabs_cru.tabs,
                                                        caixas_de_pesquisa=self.caixas_de_pesquisa)
        self.botao_submenu_consultar = mcv.BotaoParaOSubMenu(texto='Consultar', icone=ft.icons.RECEIPT_ROUNDED,
                                                             rota='consultar', pagina=self.pagina,
                                                             tabs=self.tabs_cru.tabs,
                                                             caixas_de_pesquisa=self.caixas_de_pesquisa)

    def view_(self):
        view = fv.ConstruirView(pagina=self.pagina, rota='/vendas', controles_submenu=self.conteudo_submenu(),
                                controles_principais=self.conteudo_principal())
        return view.construir_view()

    def conteudo_submenu(self) -> list[ft.Control]:
        return [
            ft.Container(
                padding=ft.padding.only(top=25),
                content=ft.Column(
                    controls=[
                        self.botao_submenu_novo.botao,
                        mcv.DivisorHorizontal(pad_direita=20, pad_esquerda=20).divisor,
                        self.botao_submenu_consultar.botao,
                        mcv.DivisorHorizontal(pad_direita=20, pad_esquerda=20).divisor
                    ]
                )
            )
        ]

    def conteudo_principal(self) -> list[ft.Control]:
        return [
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.tabs_cru.tabs_container
                    ]
                )
            )
        ]

    def conteudo_tabs_1(self) -> ft.Container:
        titulo_da_tab_atual = mcv.TextoParaTitutlos(label='Nova venda', pad_cima=25, pad_baixo=5,
                                                    largura_container=850).item_container
        titulo_da_tab_atual.border = ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_ACCENT_700))

        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'a', 33.90, 'aaa'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'b', 33.90, 'bbb'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'c', 33.90, 'ccc'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'd', 33.90, 'ddd'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'a', 33.90, 'aaa'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'b', 33.90, 'bbb'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'c', 33.90, 'ccc'))
        self.tabela_produtos.adicionar_linha_tabela_produtos(dados=(1, 'd', 33.90, 'ddd'))

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            #  Titutlo
                            ft.Container(
                                alignment=ft.alignment.top_center,
                                content=titulo_da_tab_atual
                            ),

                            #  1ª linha de caixas de texto e caixa de escolha
                            ft.Row(
                                controls=[
                                    self.pesquisa_produto_cod.item_container,
                                    self.pesquisa_produto_nome.item_container,
                                    self.pesquisa_produto_categoria.item_container
                                ]
                            ),

                            #  2ª linha - Botões para pesquisa
                            ft.Row(
                                width=400,
                                alignment=ft.MainAxisAlignment.END,
                                controls=[
                                    self.pesquisa_produto_botao_pesquisar.item,
                                    self.pesquisa_produto_botao_resetar.item
                                ]
                            ),

                            #  3ª linha - Início da tabela de pesquisa de produtos
                            ft.Row(
                                width=400,
                                height=300,
                                controls=[
                                    ft.Column(
                                        width=400,
                                        height=350,
                                        scroll=ft.ScrollMode.ADAPTIVE,
                                        controls=[
                                            self.tabela_produtos.item_container
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),

                    ft.Column(
                        controls=[
                            # Coluna de carrinho de compras
                        ]
                    )
                ]
            )

        )

    def conteudo_tabs_2(self) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text('abba 2')
                ]
            )
        )
