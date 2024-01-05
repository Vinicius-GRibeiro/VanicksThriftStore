import flet as ft
import gui.fabrica_de_views as fv
import gui.modelos_controles_produtos as mc
import controladores.controlador_view_produtos as ctrl_vp

largura = 720 * 1.9
altura = 405 * 1.9


class ViewProdutos:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina

        self.id_ = mc.CaixaDeTexto(texto='', pad_cima=20, pad_esquerda=30, altura_item=200, disabled=True,
                                   preenchido=True, estilo_texto=True, tamanho_fonte=20, bold=True, centralizado=True)

        self.nome_ = mc.CaixaDeTexto(texto='Nome', pad_cima=20, largura=650, altura_item=200)

        filtro_estoque = ft.InputFilter(regex_string=r"[0-9+]", allow=True, replacement_string='')
        filtro_preco = ft.InputFilter(regex_string=r'^[0-9.]+$', allow=True, replacement_string='')

        self.estoque_ = mc.CaixaDeTexto(texto='Qntd.', pad_cima=10, largura=110, pad_esquerda=30, filtro=filtro_estoque,
                                        altura_item=200)
        self.preco_ = mc.CaixaDeTexto(texto='Preço', pad_cima=10, largura=110, filtro=filtro_preco, altura_item=200)
        self.categoria_ = mc.CaixaDeEscolha(texto='Categoria', pad_cima=10, largura=255, altura_item=200)
        self.estado_ = mc.CaixaDeEscolha(texto='Estado', pad_cima=10, largura=250, altura_item=200)

        self.descricao_ = mc.CaixaDeTexto(texto='Descrição', pad_cima=10, largura=750, altura_item=200, pad_esquerda=30)

        self.id_pesquisa_ = mc.CaixaDeTexto(texto='Cód.', pad_cima=20, altura_item=75, altura=75,
                                            estilo_texto=True, tamanho_fonte=15)
        self.nome_pesquisa_ = mc.CaixaDeTexto(texto='Nome.', pad_cima=20, altura_item=75, altura=75, largura=150,
                                              estilo_texto=True, tamanho_fonte=15)
        self.categoria_pesquisa_ = mc.CaixaDeEscolha(texto='Categoria', pad_cima=20, largura=150, altura_item=75,
                                                     altura=75)
        self.estado_pesquisa_ = mc.CaixaDeEscolha(texto='Estado', pad_cima=20, largura=150, altura_item=75, altura=75)

        self.controles_do_adicionar = [self.id_.item_caixa_de_texto, self.nome_.item_caixa_de_texto,
                                       self.categoria_.item_caixa_de_escolha, self.estoque_.item_caixa_de_texto,
                                       self.preco_.item_caixa_de_texto, self.descricao_.item_caixa_de_texto,
                                       self.estado_.item_caixa_de_escolha]

        self.lista_controles_submenu = [
            self._sbm_botao_com_container('Adicionar', ft.icons.ADD_ROUNDED, 'adicionar'),
            self._sbm_divisor_de_botao(),
            self._sbm_botao_com_container('Consultar', ft.icons.SEARCH_ROUNDED, 'consultar'),
            self._sbm_divisor_de_botao(),
        ]

        self.botao_salvar_alteracoes_ = mc.BotaoSalvarAlteracoesVIEWPRODUTO(pagina=self.pagina,
                                                                            controles=self.controles_do_adicionar)
        self.botao_excluir_produto_ = mc.BotaoExcluirVIEWPRODUTO(pagina=self.pagina,
                                                                 controles=self.controles_do_adicionar)
        self.botao_adicionar_ = mc.BotaoAdicionarVIEWPRODUTO(pagina=self.pagina, controles=self.controles_do_adicionar,
                                                             botoes=[self.botao_salvar_alteracoes_.item_btn_add,
                                                                     self.botao_excluir_produto_.item_btn_add])

        self.tabela_produtos = mc.TabelaProdutos(pagina=self.pagina, controles=self.controles_do_adicionar,
                                                 botoes=[self.botao_salvar_alteracoes_.item_btn_add,
                                                         self.botao_excluir_produto_.item_btn_add])
        estilo_caixa_de_selecao_pesquisa = ft.TextStyle(
            color=ft.colors.PINK_ACCENT_700,
            size=15,
            weight=ft.FontWeight.BOLD
        )

        self.categoria_pesquisa_.item_caixa_de_escolha.text_style = estilo_caixa_de_selecao_pesquisa
        self.estado_pesquisa_.item_caixa_de_escolha.text_style = estilo_caixa_de_selecao_pesquisa

        self.controles_pesquisa = [self.id_pesquisa_.item_caixa_de_texto,
                                   self.nome_pesquisa_.item_caixa_de_texto,
                                   self.categoria_pesquisa_.item_caixa_de_escolha,
                                   self.estado_pesquisa_.item_caixa_de_escolha,
                                   self.tabela_produtos]

        self.botao_pesquisar_filtros = mc.BotaoConsultasVIEWPRODUTO(pagina=self.pagina,
                                                                    cor=ft.colors.INDIGO_900,
                                                                    icone=ft.icons.SEARCH_ROUNDED,
                                                                    tipo='consultar',
                                                                    controles=self.controles_pesquisa)

        self.botao_resetar_filtros = mc.BotaoConsultasVIEWPRODUTO(pagina=self.pagina,
                                                                  icone=ft.icons.AUTORENEW_ROUNDED,
                                                                  cor=ft.colors.RED_900,
                                                                  tipo='resetar',
                                                                  controles=self.controles_pesquisa)

        self.lista_controles_principais = [
            ft.Container(
                width=800,
                height=600,
                content=ft.Stack(
                    controls=[
                        ft.Tabs(
                            indicator_tab_size=False,
                            selected_index=0,
                            divider_color='transparent',
                            tabs=[
                                ft.Tab(
                                    content=ft.Container(
                                        content=ft.Row(
                                            controls=self._prin_conteudo_principal_adicionar()
                                        )
                                    )
                                ),

                                ft.Tab(
                                    content=ft.Container(
                                        content=ft.Row(
                                            controls=self._prin_conteudo_principal_consultar()
                                        )
                                    )
                                )
                            ]
                        ),

                        ft.Container(  # Cabeçalho da página de produtos
                            bgcolor=ft.colors.PINK_500,
                            width=800,
                            height=50,
                            alignment=ft.alignment.center,
                            border_radius=20,
                            border=ft.border.only(top=ft.BorderSide(5, ft.colors.PINK_ACCENT_700),
                                                  right=ft.BorderSide(5, ft.colors.PINK_ACCENT_700)),
                            content=ft.Text(
                                value='PRODUTOS',
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

        self.tab_principal = self.lista_controles_principais[0].content.controls[0]

        self.conroles_do_adicionar = [
            self.id_.item_caixa_de_texto, self.nome_.item_caixa_de_texto,
            self.estoque_.item_caixa_de_texto, self.preco_.item_caixa_de_texto,
            self.categoria_.item_caixa_de_escolha, self.estado_.item_caixa_de_escolha,
            self.descricao_.item_caixa_de_texto
        ]

        self.controles_do_consultar = [
            self.id_pesquisa_.item_caixa_de_texto, self.nome_pesquisa_.item_caixa_de_texto,
            self.categoria_pesquisa_.item_caixa_de_escolha, self.estado_pesquisa_.item_caixa_de_escolha
        ]

    def _prin_conteudo_principal_adicionar(self):
        return [
            ft.Container(
                border_radius=20,
                alignment=ft.alignment.top_left,
                width=800,
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[  # O que fica em baixo do que
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    padding=ft.padding.only(top=20, left=10),
                                    width=800,
                                    border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_ACCENT_700)),
                                    border_radius=ft.border_radius.only(bottom_right=100),
                                    content=ft.Text(
                                        value='Adicionar novo produto',
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        color=ft.colors.PINK_ACCENT_700,
                                        expand=True
                                    ),
                                ),

                                ft.Row([self.id_.item_caixa_de_texto_container,
                                        self.nome_.item_caixa_de_texto_container]),
                                ft.Row([self.estoque_.item_caixa_de_texto_container,
                                        self.preco_.item_caixa_de_texto_container,
                                        self.categoria_.item_caixa_de_escolha_container,
                                        self.estado_.item_caixa_de_escolha_container]),
                                ft.Row([self.descricao_.item_caixa_de_texto_container]),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            padding=ft.padding.only(left=100, right=20),
                                            alignment=ft.alignment.center_right,
                                            width=800,
                                            content=ft.Container(
                                                padding=ft.padding.only(left=30),
                                                alignment=ft.alignment.center,
                                                width=300,
                                                content=ft.Row(
                                                    controls=[
                                                        self.botao_adicionar_.item_btn_add,
                                                        self.botao_salvar_alteracoes_.item_btn_add,
                                                        self.botao_excluir_produto_.item_btn_add
                                                    ]
                                                )
                                            )
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                            ]
                        )
                    ]
                )
            )
        ]

    def _prin_conteudo_principal_consultar(self):
        return [
            ft.Container(
                border_radius=20,
                alignment=ft.alignment.top_left,
                width=800,
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[  # O que fica em baixo do que
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    padding=ft.padding.only(top=20, left=10),
                                    width=800,
                                    border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_ACCENT_700)),
                                    border_radius=ft.border_radius.only(bottom_right=100),
                                    content=ft.Text(
                                        value='Estoque',
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        color=ft.colors.PINK_ACCENT_700,
                                        expand=True
                                    ),
                                ),

                                ft.Row(
                                    controls=[
                                        # copntroles de pesquisa
                                        self.id_pesquisa_.item_caixa_de_texto_container,
                                        self.nome_pesquisa_.item_caixa_de_texto_container,
                                        self.categoria_pesquisa_.item_caixa_de_escolha_container,
                                        self.estado_pesquisa_.item_caixa_de_escolha_container,
                                        ft.Container(
                                            padding=ft.padding.only(top=15, left=40),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.END,
                                                expand=True,
                                                controls=[
                                                    ft.Container(
                                                        alignment=ft.alignment.bottom_center,
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                self.botao_pesquisar_filtros.item_btn_consulta_vp,
                                                                self.botao_resetar_filtros.item_btn_consulta_vp
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),

                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=(
                                                ft.Column(
                                                    controls=[
                                                        self.tabela_produtos.item_tabela_produtos
                                                    ],
                                                    scroll=ft.ScrollMode.ADAPTIVE
                                                )
                                            ),
                                            height=400,
                                            border_radius=1,
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
        ]

    def _prin_conteudo_principal(self) -> list[ft.Control]:
        return [
            ft.Container(
                content=ft.Row(
                    controls=self.lista_controles_principais
                )
            )
        ]

    def view_(self):
        view = fv.ConstruirView(pagina=self.pagina, rota='/produtos', controles_submenu=self._sbm_conteudo_submenu(),
                                controles_principais=self._prin_conteudo_principal())
        return view.construir_view()

    def _sbm_conteudo_submenu(self) -> list[ft.Control]:
        return [
            ft.Container(
                padding=ft.padding.only(top=30),
                content=ft.Column(
                    controls=self.lista_controles_submenu
                )
            )
        ]

    def _sbm_botao_com_container(self, texto_do_botao: str, icone_do_botao: str, rota: str) -> ft.Container:
        return ft.Container(
            width=100,
            height=100,
            border_radius=20,
            on_click=lambda _: self._sbm_ao_clicar_no_botao(rota),
            on_hover=lambda e: self._sbm_destacar_botao(e),
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[

                    ft.Container(
                        padding=ft.padding.only(left=9, right=7),
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

    def _sbm_ao_clicar_no_botao(self, rota: str):
        if rota == 'adicionar':
            self.tab_principal.selected_index = 0
            ctrl_vp.atualizar_view_produtos_adicionar(controles=self.controles_do_adicionar, pagina=self.pagina,
                                                      botoes=[self.botao_salvar_alteracoes_.item_btn_add,
                                                              self.botao_excluir_produto_.item_btn_add])
        elif rota == 'consultar':
            self.tab_principal.selected_index = 1
        self.pagina.update()

    @staticmethod
    def _sbm_divisor_de_botao() -> ft.Container:
        return ft.Container(
            width=100,
            padding=ft.padding.only(left=20, right=20),
            content=ft.Divider(
                color=ft.colors.PINK_300,
                thickness=2
            )
        )

    @staticmethod
    def _sbm_destacar_botao(e):
        if e.data == 'true':
            e.control.bgcolor = ft.colors.with_opacity(.3, ft.colors.WHITE)
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
