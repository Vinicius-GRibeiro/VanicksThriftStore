import flet as ft
import gui.fabrica_de_views as fv
import gui.modelos_controles_configuracoes as mcc

largura = 720 * 1.9
altura = 405 * 1.9


class ViewConfiguracoes:
    def __init__(self, pagina: ft.Page):
        self._pagina = pagina

        '''--------------------CONTROLES DA ABA #CONTA--------------------'''
        self.conta_usuario_codigo = mcc.CaixaDeTextoBordaUnica(pagina=self._pagina, label='Cód.', largura_caixa=100,
                                                               largura_container=100, altura_container=60,
                                                               altura_caixa=300, somente_leitura=True)
        self.conta_usuario_nome = mcc.CaixaDeTextoBordaUnica(pagina=self._pagina, label='Nome', largura_caixa=300,
                                                             largura_container=500, altura_container=60,
                                                             altura_caixa=300)
        self.conta_usuario_usuario = mcc.CaixaDeTextoBordaUnica(pagina=self._pagina, label='Usuário', largura_caixa=300,
                                                                largura_container=300, altura_container=60,
                                                                altura_caixa=300, maiusculo=True)
        self.conta_usuario_email = mcc.CaixaDeTextoBordaUnica(pagina=self._pagina, label='E-mail', largura_caixa=300,
                                                              largura_container=300, altura_container=60,
                                                              altura_caixa=300)
        self.conta_usuario_telefone = mcc.CaixaDeTextoBordaUnica(pagina=self._pagina, label='Telefone',
                                                                 largura_caixa=300, largura_container=300,
                                                                 altura_container=60, altura_caixa=300,
                                                                 regex_filtro="^[0-9]+$")
        self.conta_usuario_nivel = mcc.CaixaDeTextoBordaUnica(pagina=self._pagina, label='Nível de acesso',
                                                              largura_caixa=300, largura_container=300,
                                                              altura_container=60, altura_caixa=300,
                                                              somente_leitura=True)
        self.contas_controles = [self.conta_usuario_codigo.item,
                                 self.conta_usuario_nome.item,
                                 self.conta_usuario_usuario.item,
                                 self.conta_usuario_email.item,
                                 self.conta_usuario_telefone.item,
                                 self.conta_usuario_nivel.item]

        self.conta_botao_salvar_alteracoes = mcc.BotaoTextoPadraoConta(pagina=self._pagina, texto='Salvar alterações',
                                                                       tipo='conta_salvar_alteracoes',
                                                                       icone=ft.icons.SAVE_ROUNDED,
                                                                       largura=200, altura=50, tamanho_icone=25,
                                                                       controles_da_aba=self.contas_controles)
        self.conta_botao_alterar_senha = mcc.BotaoTextoPadraoConta(pagina=self._pagina, texto='Alterar senha',
                                                                   tipo='conta_alterar_senha',
                                                                   icone=ft.icons.LOCK_ROUNDED,
                                                                   largura=200, altura=50, tamanho_icone=25,
                                                                   controles_da_aba=self.contas_controles)

        #  Últimos controles
        self._tab = mcc.Abas(pagina=self._pagina, conteudo_tab_1=self.conteudo_tab_1(),
                             conteudo_tab_2=self.conteudo_tab_2(), conteudo_tab_3=self.conteudo_tab_3(),
                             conteudo_tab_4=self.conteudo_tab_4(), conteudo_tab_5=self.conteudo_tab_5())

        self.submenu_botao_conta = mcc.BotaoParaOSubMenu(pagina=self._pagina, icone=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                                                         texto='Conta', tamanho_icone=40, tamanho_texto=15,
                                                         tabs=self._tab, caixas_de_texto=self.contas_controles)
        self.submenu_botao_gerais = mcc.BotaoParaOSubMenu(pagina=self._pagina, icone=ft.icons.TUNE_ROUNDED,
                                                          texto='Geral', tamanho_icone=40, tamanho_texto=15,
                                                          tabs=self._tab)
        self.submenu_botao_relatorios = mcc.BotaoParaOSubMenu(pagina=self._pagina, icone=ft.icons.BAR_CHART_ROUNDED,
                                                              texto='Relatórios', tamanho_icone=40, tamanho_texto=15,
                                                              tabs=self._tab)
        self.submenu_botao_usuarios = mcc.BotaoParaOSubMenu(pagina=self._pagina, icone=ft.icons.MANAGE_ACCOUNTS_ROUNDED,
                                                            texto='Usuários', tamanho_icone=40, tamanho_texto=15,
                                                            tabs=self._tab)
        self.submenu_botao_desenvolvedor = mcc.BotaoParaOSubMenu(pagina=self._pagina, icone=ft.icons.CODE_ROUNDED,
                                                                 texto='DEV', tamanho_icone=40, tamanho_texto=15,
                                                                 tabs=self._tab)

    def view_(self):
        view = fv.ConstruirView(pagina=self._pagina, rota='/configuracoes', controles_submenu=self.conteudo_submenu(),
                                controles_principais=self.conteudo_principal())
        return view.construir_view()

    def conteudo_submenu(self) -> list[ft.Control]:
        return [
            ft.Container(
                padding=ft.padding.only(top=15),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=1,
                    controls=[
                        self.submenu_botao_conta.item_container,
                        ft.Container(width=50, height=2, bgcolor=ft.colors.PINK_300, alignment=ft.alignment.center),
                        self.submenu_botao_gerais.item_container,
                        ft.Container(width=50, height=2, bgcolor=ft.colors.PINK_300, alignment=ft.alignment.center),
                        self.submenu_botao_relatorios.item_container,
                        ft.Container(width=50, height=2, bgcolor=ft.colors.PINK_300, alignment=ft.alignment.center),
                        self.submenu_botao_usuarios.item_container,
                        ft.Container(width=50, height=2, bgcolor=ft.colors.PINK_300, alignment=ft.alignment.center),
                        self.submenu_botao_desenvolvedor.item_container,
                        ft.Container(width=50, height=2, bgcolor=ft.colors.PINK_300, alignment=ft.alignment.center),
                    ]
                )
            )
        ]

    def conteudo_principal(self) -> list[ft.Control]:
        return [
            ft.Container(
                content=ft.Row(
                    controls=[
                        self._tab.tabs_container
                    ]
                )
            )
        ]

    def conteudo_tab_1(self) -> ft.Container:  # Conta
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(  # Título da página
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=20),
                                content=ft.Text('Informações do usuário', color=ft.colors.PINK_ACCENT_700, size=30,
                                                weight=ft.FontWeight.BOLD),
                                border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_500)),
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ]
                    ),

                    ft.Container(  # Linha ZERO - Avatar de usuário
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(left=100, right=100),
                        content=ft.Row(  # Primeira linha de conteúdo
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                                    size=100,
                                    color=ft.colors.PINK_ACCENT_700
                                )
                            ]
                        )
                    ),

                    ft.Container(  # Primeira linha de conteúdo
                        padding=ft.padding.only(left=100, right=100),
                        content=ft.Row(  # Primeira linha de conteúdo
                            controls=[
                                self.conta_usuario_codigo.item_container,
                                self.conta_usuario_nome.item_container
                            ]
                        )
                    ),

                    ft.Container(  # Segunda linha de conteúdo
                        padding=ft.padding.only(left=100, right=100, top=25),
                        content=ft.Row(  # Segunda linha de conteúdo
                            controls=[
                                self.conta_usuario_usuario.item_container,
                                self.conta_usuario_email.item_container
                            ]
                        )
                    ),

                    ft.Container(  # Terceira linha de conteúdo
                        padding=ft.padding.only(left=100, right=100, top=25),
                        content=ft.Row(  # Terceira linha de conteúdo
                            controls=[
                                self.conta_usuario_telefone.item_container,
                                self.conta_usuario_nivel.item_container
                            ]
                        )
                    ),

                    ft.Container(  # Quarta linha de conteúdo
                        bgcolor='blue',
                        padding=ft.padding.only(left=100, right=100),
                        content=ft.Row(  # Terceira linha de conteúdo
                            alignment=ft.MainAxisAlignment.END,
                            width=600,
                            controls=[

                            ]
                        )
                    ),

                    ft.Container(  # Quinta linha de conteúdo - Botões
                        padding=ft.padding.only(left=100, right=90),
                        content=ft.Row(  # Terceira linha de conteúdo
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            width=650,
                            controls=[
                                self.conta_botao_salvar_alteracoes.item_container,
                                self.conta_botao_alterar_senha.item_container
                            ]
                        )
                    ),
                ]
            )
        )

    def conteudo_tab_2(self) -> ft.Container:  # Gerais
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=20),
                                content=ft.Text('Configurações gerais', color=ft.colors.PINK_ACCENT_700, size=30,
                                                weight=ft.FontWeight.BOLD),
                                border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_500)),
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ]
                    ),
                    #  Continuar próxima linha de conteúdo aqui
                ]
            )
        )

    def conteudo_tab_3(self) -> ft.Container:  # Relatórios
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=20),
                                content=ft.Text('Relatórios', color=ft.colors.PINK_ACCENT_700, size=30,
                                                weight=ft.FontWeight.BOLD),
                                border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_500)),
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ]
                    ),
                    #  Continuar próxima linha de conteúdo aqui

                ]
            )
        )

    def conteudo_tab_4(self) -> ft.Container:  # Usuários
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=20),
                                content=ft.Text('Configurações de usuários', color=ft.colors.PINK_ACCENT_700, size=30,
                                                weight=ft.FontWeight.BOLD),
                                border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_500)),
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ]
                    ),
                    #  Continuar próxima linha de conteúdo aqui

                ]
            )
        )

    def conteudo_tab_5(self) -> ft.Container:  # DEV
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=20),
                                content=ft.Text('Configurações de desenvolvedor', color=ft.colors.PINK_ACCENT_700,
                                                size=30,
                                                weight=ft.FontWeight.BOLD),
                                border=ft.Border(bottom=ft.BorderSide(1, ft.colors.PINK_500)),
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ]
                    ),
                    #  Continuar próxima linha de conteúdo aqui

                ]
            )
        )
