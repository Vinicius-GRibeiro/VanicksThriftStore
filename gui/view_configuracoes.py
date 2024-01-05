import flet as ft
import gui.fabrica_de_views as fv

largura = 720 * 1.9
altura = 405 * 1.9


class ViewConfiguracoes:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina

    def view_(self):
        view = fv.ConstruirView(pagina=self.pagina, rota='/configuracoes', controles_submenu=self.conteudo_submenu(),
                                controles_principais=self.conteudo_principal())
        return view.construir_view()

    def conteudo_submenu(self) -> list[ft.Control]:
        return [
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text('configuracoes')
                    ]
                )
            )
        ]

    def conteudo_principal(self) -> list[ft.Control]:
        return [
            ft.Container(
                content=ft.Row(
                    controls=[

                    ]
                )
            )
        ]
