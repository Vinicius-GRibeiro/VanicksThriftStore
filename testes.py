import flet as ft

largura = 720 * 1.9
altura = 405 * 1.9


def bottomsheet_de_edicao_de_produtos(pagina: ft.Page, dados: tuple, altura_bs: int = 800):
    def conteudo_bs():
        conteudo = ft.Container(
            alignment=ft.alignment.top_center,
            border=ft.Border(top=ft.BorderSide(8, ft.colors.PINK_ACCENT_700),
                             right=ft.BorderSide(8, ft.colors.PINK_ACCENT_700)),
            border_radius=25,
            height=altura_bs,
            width=800,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # PRIMEIRA LINHA
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=25),
                                content=ft.Text(
                                    value='Editando produto', size=20, weight=ft.FontWeight.BOLD
                                )
                            )
                        ]
                    )  # --------------
                ]
            )
        )

        return conteudo

    class CamposDeTextBS:
        ...

    class BottomSheetEdicao:
        def __init__(self):
            self.conteudo = conteudo_bs()
            self.item_bs = self.bs_item()
            pagina.overlay.append(self.item_bs)

        def bs_item(self):
            bs = ft.BottomSheet(
                elevation=altura_bs,
                open=True,
                content=self.conteudo
            )

            return bs

        def abrir_bs(self):
            self.item_bs.open = True
            pagina.update()

        def fechar_bs(self):
            self.item_bs.open = False
            pagina.update()

    bs = BottomSheetEdicao()
    bs.abrir_bs()
