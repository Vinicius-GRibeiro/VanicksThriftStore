import flet as ft
import data.data_model
import gui.fabrica_de_views as fv
import gui.modelos_controles_vendas as mcv
import gui.modelos_controles_vendas_consultar as mcvc

db = data.data_model.SGBD()

largura = 720 * 1.9
altura = 405 * 1.9


class ViewVendas:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina

        self.pesquisa_produto_cod = mcv.CaixaDeTextoPadrao(label='Cód.', pad_cima=0, pad_esquerda=20,
                                                           tamanho_do_texto=12, fino=True)
        self.pesquisa_produto_nome = mcv.CaixaDeTextoPadrao(label='Nome', pad_cima=0, largura_caixa_container=130,
                                                            tamanho_do_texto=12, fino=True)
        self.pesquisa_produto_categoria = mcv.CaixaDeEscolha(label='Categoria', pad_cima=0,
                                                             largura_caixa_container=130, tamanho_do_texto=12,
                                                             fino=True)
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

        self.cod_venda = ft.Text(value='')
        self.timestamp = ft.Text(value='')
        self.texto_cod_data_hora = mcv.TextoPadraoDoResumoDaCompra(texto='', bold=True).item_texto

        self.tabela_carrinho_de_compras = mcv.TabelaCarrinhoDeCompras(pagina=self.pagina, altura=350,
                                                                      valor_total=self.valor_total)
        self.lista_de_ids_de_produtos_no_carrinho = ft.Text(value='')
        self.tabela_produtos = mcv.TabelaProdutos(pagina=self.pagina, largura_tabela=400,
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
        self.pesquisa_produto_botao_pesquisar.item_container.padding = ft.padding.only(left=20)
        self.pesquisa_produto_botao_resetar = mcv.BotaoIconePadrao(pagina=self.pagina, tamanho_icone=20,
                                                                   icone=ft.icons.AUTORENEW_ROUNDED,
                                                                   cor_do_icone=ft.colors.RED_600, tipo='redefinir',
                                                                   tabela=self.tabela_produtos,
                                                                   itens_pesquisa=self.caixas_de_pesquisa)
        self.botao_finalizar_compra = mcv.BotaoTextoPadrao(pagina=self.pagina, texto='Finalizar compra',
                                                           tipo='finalizar_compra', largura=200, altura=40,
                                                           tamanho_texto=18, cor_do_texto=ft.colors.PINK_500,
                                                           icone=ft.icons.DONE_ROUNDED, tamanho_icone=18,
                                                           tabela=self.tabela_carrinho_de_compras,
                                                           tabela_produtos=self.tabela_produtos,
                                                           itens_pesquisa=[
                                                               self.pesquisa_produto_cod,
                                                               self.pesquisa_produto_nome,
                                                               self.pesquisa_produto_categoria],
                                                           cod_venda=self.cod_venda,
                                                           timestamp_venda=self.timestamp,
                                                           item_cod_data_hota=self.texto_cod_data_hora,
                                                           campo_valor_total=self.valor_total
                                                           )
        _filtro_data = ft.InputFilter(regex_string='^[0-9/]+$', allow=True, replacement_string="")
        _filtro_monetario = ft.InputFilter(regex_string='^[0-9.]+$', allow=True)

        self.consulta_switch_cancelados = ft.Switch(label='cancelados', value=False)
        self.consulta_switch_cancelados.active_color = ft.colors.PINK_ACCENT_700

        self.consulta_caixa_data_inicial = mcvc.CaixaDeTextoPadraoCONSULTA(label='Data inicial',
                                                                           icone_prefixo=ft.icons.CALENDAR_TODAY_ROUNDED)
        self.consulta_caixa_data_inicial.item.input_filter = _filtro_data

        self.consulta_caixa_data_final = mcvc.CaixaDeTextoPadraoCONSULTA(label='Data final',
                                                                         icone_prefixo=ft.icons.CALENDAR_TODAY_ROUNDED)
        self.consulta_caixa_data_final.item.input_filter = _filtro_data

        self.consulta_caixa_valor_inicial = mcvc.CaixaDeTextoPadraoCONSULTA(label='Valor inicial',
                                                                            icone_prefixo=ft.icons.ATTACH_MONEY_ROUNDED)
        self.consulta_caixa_valor_inicial.item.input_filter = _filtro_monetario

        self.consulta_caixa_valor_final = mcvc.CaixaDeTextoPadraoCONSULTA(label='Valor final',
                                                                          icone_prefixo=ft.icons.ATTACH_MONEY_ROUNDED)
        self.consulta_caixa_valor_final.item.input_filter = _filtro_monetario

        self.filtros_caixa_de_texto = [
            self.consulta_caixa_data_inicial,
            self.consulta_caixa_data_final,
            self.consulta_caixa_valor_inicial,
            self.consulta_caixa_valor_final
        ]

        self.consulta_tabela_vendas = mcvc.TabelaProdutosConsultar(pagina=self.pagina, altura_cabecalho=50,
                                                                   filtro_cancelados=self.consulta_switch_cancelados,
                                                                   filtros_texto=self.filtros_caixa_de_texto)

        self.consulta_botao_consultar = mcvc.BotaoPadraConsulta(pagina=self.pagina, tipo='consultar',
                                                                icone=ft.icons.SEARCH_ROUNDED,
                                                                cor_padrao=ft.colors.PINK_ACCENT_700,
                                                                tamanho_icone=30,
                                                                filtros_texto=self.filtros_caixa_de_texto,
                                                                filtro_cancelados=self.consulta_switch_cancelados,
                                                                tabela=self.consulta_tabela_vendas)

        self.consulta_botao_resetar_filtro = mcvc.BotaoPadraConsulta(pagina=self.pagina, tipo='resetar',
                                                                     icone=ft.icons.FIND_REPLACE_ROUNDED,
                                                                     cor_padrao=ft.colors.INDIGO_700,
                                                                     tamanho_icone=30,
                                                                     filtros_texto=self.filtros_caixa_de_texto,
                                                                     filtro_cancelados=self.consulta_switch_cancelados,
                                                                     tabela=self.consulta_tabela_vendas
                                                                     )
        # Atributos daqui para baixo, devem ser os últimos
        self.tabs_cru = mcv.Tabs_(pagina=self.pagina, conteudo_tabs_1_=self.conteudo_tabs_1(),
                                  conteudo_tabs_2_=self.conteudo_tabs_2())
        self.botao_submenu_novo = mcv.BotaoParaOSubMenu(texto='Nova       ', icone=ft.icons.POINT_OF_SALE_ROUNDED,
                                                        rota='novo', pagina=self.pagina, tabs=self.tabs_cru.tabs,
                                                        caixas_de_pesquisa=self.caixas_de_pesquisa,
                                                        cod_data_hora=self.texto_cod_data_hora,
                                                        texto_cod=self.cod_venda, texto_timestamp=self.timestamp,
                                                        valor_total=self.valor_total)
        self.botao_submenu_consultar = mcv.BotaoParaOSubMenu(texto='Consultar', icone=ft.icons.RECEIPT_ROUNDED,
                                                             rota='consultar', pagina=self.pagina,
                                                             tabs=self.tabs_cru.tabs,
                                                             caixas_de_pesquisa=self.caixas_de_pesquisa,
                                                             tabela_vendas_consulta=self.consulta_tabela_vendas,
                                                             filtros_texto=self.filtros_caixa_de_texto,
                                                             filtro_cancelados=self.consulta_switch_cancelados)

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
        titulo_da_tab_atual = mcv.TextoParaTitutlos(label='Nova venda', pad_cima=5, pad_baixo=5,
                                                    largura_container=850).item_container
        titulo_da_tab_atual.border = ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_ACCENT_700))

        return ft.Container(
            content=ft.Column(  # Coluna principal
                spacing=1,
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
                                            #  1ª linha - Início da tabela de pesquisa de produtos
                                            ft.Column(
                                                height=300,
                                                controls=[
                                                    ft.Row(
                                                        width=400,
                                                        height=300,
                                                        controls=[
                                                            ft.Column(
                                                                width=400,
                                                                height=300,
                                                                scroll=ft.ScrollMode.ADAPTIVE,
                                                                controls=[
                                                                    self.tabela_produtos.item_container
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            ),

                                            #  2ª linha de caixas de texto e caixa de escolha
                                            ft.Row(
                                                controls=[
                                                    self.pesquisa_produto_cod.item_container,
                                                    self.pesquisa_produto_nome.item_container,
                                                    self.pesquisa_produto_categoria.item_container
                                                ]
                                            ),

                                            #  3ª linha - Botões para pesquisa
                                            ft.Row(
                                                width=400,
                                                alignment=ft.MainAxisAlignment.START,
                                                controls=[
                                                    self.pesquisa_produto_botao_pesquisar.item_container,
                                                    self.pesquisa_produto_botao_resetar.item_container
                                                ]
                                            ),
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
                                                height=350,
                                                width=390,
                                                content=ft.Column(
                                                    # Coluna da linha dos controles do carrinho de compras
                                                    alignment=ft.MainAxisAlignment.START,
                                                    spacing=1,
                                                    scroll=ft.ScrollMode.ADAPTIVE,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Divider(color='transparent', height=5),
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='-' * 90).item_texto,
                                                        self.texto_cod_data_hora,
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='RESUMO DA COMPRA',
                                                                                        bold=True).item_texto,
                                                        mcv.TextoPadraoDoResumoDaCompra(texto='-' * 90).item_texto,
                                                        ft.Divider(color='transparent', height=1),
                                                        self.tabela_carrinho_de_compras.item_tabela,
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
                                    ),

                                    ft.Row(
                                        controls=[
                                            self.botao_finalizar_compra.item_container
                                        ],
                                        alignment=ft.MainAxisAlignment.END,
                                        width=390
                                    )
                                ]
                            )
                        ]
                    ),

                ]
            )
        )

    def conteudo_tabs_2(self) -> ft.Container:
        titulo_da_tab_atual = mcv.TextoParaTitutlos(label='Consultar vendas', pad_cima=5, pad_baixo=5,
                                                    largura_container=850).item_container
        titulo_da_tab_atual.border = ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_ACCENT_700))

        return ft.Container(alignment=ft.alignment.top_right, content=ft.Column(spacing=25, controls=[
            ft.Row(controls=[ft.Container(content=titulo_da_tab_atual, height=50)]),  # Linha de titulo

            ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[  # Linha do conteúdo principal, que possui as duas colunas

                       ft.Container(width=320, content=ft.Column(controls=[  # Coluna dos filtros de pesquisa

                           ft.Row(controls=[mcvc.TextoPadrao(texto='Por período', container_largura=150,
                                                             container_altura=25,
                                                             peso=True).item_container,
                                            self.consulta_switch_cancelados
                                            ]),

                           ft.Row(controls=[self.consulta_caixa_data_inicial.item_container,
                                            self.consulta_caixa_data_final.item_container]),

                           ft.Divider(thickness=10, opacity=0),

                           mcvc.TextoPadrao(texto='Por valor total R$', container_largura=150, container_altura=25,
                                            peso=True).item_container,
                           ft.Row(controls=[self.consulta_caixa_valor_inicial.item_container,
                                            self.consulta_caixa_valor_final.item_container]),

                           ft.Divider(thickness=10, opacity=0),

                           ft.Row(
                               alignment=ft.MainAxisAlignment.END,
                               controls=[
                                   self.consulta_botao_resetar_filtro.item,
                                   self.consulta_botao_consultar.item,
                               ]
                           ),

                           ft.Container(height=100)
                       ])),

                       ft.Container(width=480, height=450, content=ft.Column(scroll=ft.ScrollMode.ADAPTIVE, height=450,
                                                                             controls=[  # Coluna da lista de vendas
                                                                                 self.consulta_tabela_vendas.item_container
                                                                             ], alignment=ft.MainAxisAlignment.START)),

                   ])
        ]))
