import flet as ft
import gui.menu_principal as menu

largura = 720 * 1.9
altura = 405 * 1.9


class ViewInicio:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina

    def view_(self):
        return ft.View(
            route='/inicio',
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
