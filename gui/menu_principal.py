import flet as ft
import controladores.controlador_view_vendas as ctrl_vv


class MenuPrincipal:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina


    @staticmethod
    def dados_do_usuario_atual(iniciais_usuario: str = 'UI', nome_usuario: str = 'Username',
                               nivel_de_acesso_usuario: str = 'User Access Level') -> ft.Container:

        return ft.Container(ft.Row(controls=[
            ft.Container(
                width=84, height=84, bgcolor=ft.colors.PINK_ACCENT_700,  # bluegrey900
                alignment=ft.alignment.center,
                border_radius=16,
                content=ft.Text(
                    value=iniciais_usuario,
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE
                )
            ),
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=2,
                controls=[
                    ft.Text(value=nome_usuario, size=22, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.Text(value=nivel_de_acesso_usuario, size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE70)
                ]
            )
        ]),
            padding=ft.padding.only(left=30, top=30)
        )

    def botao_com_container(self, texto_do_botao: str, icone_do_botao: str, rota: str | bool = False) -> ft.Container:
        return ft.Container(
            width=300,
            height=70,
            border_radius=20,
            on_hover=lambda e: self.destacar_linha(e),
            on_click=lambda _: self.ao_clicar_no_botao(rota=rota),
            padding=ft.padding.only(left=40),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icone_do_botao,
                        icon_size=36,
                        icon_color=ft.colors.PINK_ACCENT_700,
                        style=ft.ButtonStyle(
                            shape={
                                '': ft.RoundedRectangleBorder(radius=14),
                            },
                            overlay_color={
                                '': 'transparent',
                            }
                        ),
                    ),

                    ft.Text(
                        value=texto_do_botao,
                        color=ft.colors.WHITE,
                        size=22,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            )
        )

    def ao_clicar_no_botao(self, rota: str | bool = False, texto_do_botao: str | None = None):
        self.pagina.go(rota)


    @staticmethod
    def destacar_linha(e):
        if e.data == 'true':
            e.control.bgcolor = ft.colors.PINK_ACCENT_700
            e.control.update()

            e.control.content.controls[0].icon_color = ft.colors.WHITE
            e.control.content.controls[1].color = ft.colors.WHITE
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color = ft.colors.PINK_ACCENT_700
            e.control.content.controls[1].color = ft.colors.WHITE
            e.control.content.update()

    def build(self):
        return ft.Container(
            padding=ft.padding.only(left=20),
            content=ft.Container(
                width=300,
                height=650,
                padding=ft.padding.only(top=20),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREY_900,
                border_radius=ft.border_radius.only(top_left=50, bottom_left=50),
                border=ft.border.only(right=ft.BorderSide(5, ft.colors.PINK_ACCENT_700)),
                content=ft.Column(controls=[
                    #  Controles do menu
                    self.dados_do_usuario_atual(),
                    ft.Divider(height=30, color='transparent'),
                    self.botao_com_container(icone_do_botao=ft.icons.HOME_ROUNDED, texto_do_botao='Início',
                                             rota='/'),
                    self.botao_com_container(icone_do_botao=ft.icons.INVENTORY_ROUNDED, texto_do_botao='Produtos',
                                             rota='/produtos'),
                    self.botao_com_container(icone_do_botao=ft.icons.SHOPPING_CART_ROUNDED, texto_do_botao='Vendas',
                                             rota='/vendas'),
                    self.botao_com_container(icone_do_botao=ft.icons.SETTINGS_ROUNDED, texto_do_botao='Configurações',
                                             rota='/configuracoes'),
                    ft.Divider(height=10, color='transparent'),
                    ft.Divider(height=30, color=ft.colors.PINK_ACCENT_700),
                    self.botao_com_container(icone_do_botao=ft.icons.LOGOUT_ROUNDED, texto_do_botao='Sair')
                ])
            )
        )
