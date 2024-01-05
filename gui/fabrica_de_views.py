import flet as ft
import gui.menu_principal as menu

largura = 720 * 1.9
altura = 405 * 1.9


class ConstruirView:
    def __init__(self, pagina: ft.Page, rota: str, controles_submenu: list[ft.Control],
                 controles_principais: list[ft.Control]):
        self.pagina = pagina
        self.rota = rota
        self.controles_submenu = controles_submenu
        self.controles_principais = controles_principais

    def construir_view(self) -> ft.View:
        return ft.View(
            route=self.rota,
            bgcolor=ft.colors.BLACK54,
            controls=[
                ft.Container(
                    padding=0,
                    expand=True,
                    content=ft.Stack(
                        expand=5,
                        height=650,
                        controls=[
                            ft.Image(
                                src='assets/img/bg_image.jpg',
                                width=largura,
                                height=altura,
                                top=0,
                                left=0
                            ),
                            ft.Column([
                                ft.Divider(height=5, color='transparent'),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    menu.MenuPrincipal(self.pagina).build(),
                                                    ft.Container(  # Container principal. Tem o submenu e o conteudo
                                                        alignment=ft.alignment.center_right,
                                                        width=1000,
                                                        height=650,
                                                        border_radius=ft.border_radius.only(top_right=50,
                                                                                            bottom_right=50),
                                                        border=ft.Border(ft.BorderSide(5, ft.colors.PINK_ACCENT_700)),
                                                        bgcolor=ft.colors.with_opacity(0.7, ft.colors.PINK_50),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.START,
                                                            controls=[
                                                                ft.Container(  # Container submenu
                                                                    bgcolor=ft.colors.PINK_600,
                                                                    width=120,
                                                                    height=650,
                                                                    border=ft.border.only(
                                                                        right=ft.BorderSide(width=10,
                                                                                            color=ft.colors.PINK_800)),
                                                                    border_radius=ft.border_radius.only(
                                                                        top_right=30,
                                                                        bottom_right=30
                                                                    ),
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.Column(
                                                                        controls=self.controles_submenu

                                                                    )
                                                                ),

                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        controls=self.controles_principais
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                ],
                                            ),
                                        )
                                    ]
                                )
                            ])
                        ]
                    ),
                )
            ]
        )
