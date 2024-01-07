import flet as ft
import data.data_model
import gui.fabrica_de_views as fv
import gui.modelos_controles_vendas as mcv
from datetime import datetime

db = data.data_model.SGBD()

largura = 720 * 1.9
altura = 405 * 1.9


class ViewVendas:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina

        self.pesquisa_produto_cod = mcv.CaixaDeTextoPadrao(label='Cód.', pad_cima=0, pad_esquerda=20,
                                                           tamanho_do_texto=12)
        self.pesquisa_produto_nome = mcv.CaixaDeTextoPadrao(label='Nome', pad_cima=0, largura_caixa_container=130,
                                                            tamanho_do_texto=12)
        self.pesquisa_produto_categoria = mcv.CaixaDeEscolha(label='Categoria', pad_cima=0,
                                                             largura_caixa_container=130, tamanho_do_texto=12)
        self.valor_total = ft.TextField(
            width=100,
            border=ft.InputBorder.NONE,
            text_align=ft.TextAlign.END,
            prefix_text='R$',
            prefix_style=ft.TextStyle(
                color=ft.colors.BLACK,
                size=20,
                weight=ft.FontWeight.BOLD
            ),
            read_only=True,
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                size=20
            ),
            value='0'
        )

        venda = 'produto'
        self.texto_cod_data_hora = mcv.TextoPadraoDoResumoDaCompra(texto=f'COD. {db.recuperar_proximo_id(tabela=venda)} - DATA {datetime.now().strftime("%d/%m/%Y")} - HORA {datetime.now().strftime("%H:%M")}', bold=True).item_texto
        self.tabela_carrinho_de_compras = mcv.TabelaCarrinhoDeCompras(pagina=self.pagina, altura=450,
                                                                      valor_total=self.valor_total)

        self.tabela_produtos = mcv.TabelaProdutos(pagina=self.pagina, largura_tabela=400, altura_cabecalho=40,
                                                  largura_caixa_container=400, altura_caixa_e_container=350,
                                                  pad_esquerda=20, carrinho_compras=self.tabela_carrinho_de_compras,
                                                  valor_total=self.valor_total)
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

        return ft.Container(
            content=ft.Column(  # Coluna principal
                controls=[
                    ft.Row(
                        controls=[  # Linha do titulo
                            ft.Container(
                                alignment=ft.alignment.top_center,
                                content=titulo_da_tab_atual,
                                padding=ft.padding.only(bottom=20)
                            ),
                        ]
                    ),

                    ft.Row(
                        controls=[
                            ft.Row(  # Controles dos produtos, filtro, seleção
                                controls=[
                                    ft.Column(  # Coluna dos produtos e pesquisas
                                        controls=[

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
                                ]
                            ),
                            ft.Column(
                                controls=[
                                    ft.Row(  # Linha dos controles do carrinho de compra
                                        controls=[
                                            ft.Container(
                                                border=ft.Border(
                                                    top=ft.BorderSide(1, ft.colors.PINK_ACCENT_700),
                                                    right=ft.BorderSide(1, ft.colors.PINK_ACCENT_700),
                                                    bottom=ft.BorderSide(1, ft.colors.PINK_ACCENT_700),
                                                    left=ft.BorderSide(1, ft.colors.PINK_ACCENT_700)
                                                ),
                                                bgcolor=ft.colors.YELLOW_ACCENT_100,
                                                height=380,
                                                width=390,
                                                content=ft.Column(
                                                    # Coluna da linha dos controles do carrinho de compras
                                                    alignment=ft.MainAxisAlignment.START,
                                                    spacing=1,
                                                    scroll=ft.ScrollMode.ADAPTIVE,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Divider(color='transparent', height=10),
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='BRECHÓ VANICK',
                                                                                        bold=True).item_texto,
                                                        mcv.TextoPadraoDoResumoDaCompra(
                                                            texto='Rua Voluntário Cícero Lamartine da Silva Leme, 561').item_texto,
                                                        mcv.TextoPadraoDoResumoDaCompra(
                                                            texto='Vila Bianchi - Bragança Paulista - SP').item_texto,
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='-' * 90).item_texto,
                                                        self.texto_cod_data_hora,
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='RESUMO DA COMPRA',
                                                                                        bold=True).item_texto,
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='-' * 90).item_texto,
                                                        ft.Divider(color='transparent', height=1),
                                                        self.tabela_carrinho_de_compras.item_tabela
                                                    ]
                                                )
                                            )
                                        ]
                                    ),

                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        controls=[
                                            ft.Container(
                                                padding=ft.padding.only(right=150),
                                                content=ft.Text(value='VALOR TOTAL',
                                                                weight=ft.FontWeight.BOLD,
                                                                size=20)
                                            ),

                                            self.valor_total
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),


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
