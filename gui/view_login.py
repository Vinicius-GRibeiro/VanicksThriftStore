import flet as ft
import data.data_model as sgbd
import gui.modelos_controles_login as mcl

db = sgbd.SGBD()


class ViewLogin:
    def __init__(self, pagina):
        self._pagina = pagina

    def view_(self):
        return ft.View(
            route='/login',
            controls=self._conteudo_view_login(),
            bgcolor=ft.colors.BLACK,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def _conteudo_view_login(self) -> list[ft.Control]:
        versoes = db.recuperar_registros(tabela='controle_versao', colunas='versaoSoftware, versaoBancoDeDados')

        conteudo = [
            ft.Stack(
                controls=[
                    ft.Image(src='assets/img/bg_image.jpg'),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        height=700,
                        controls=[
                            ft.Container(
                                blur=50,
                                height=700,
                                width=500,
                                border=ft.border.only(right=ft.BorderSide(5, ft.colors.PINK_ACCENT_700)),
                                content=ft.Column(
                                    controls=[  # Formulário de login

                                    ]
                                )
                            ),

                            #  Titulos e versionamento
                            ft.Container(
                                width=830,
                                padding=ft.padding.only(top=50),
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[
                                        ft.Container(
                                            padding=ft.padding.only(left=250),
                                            content=ft.Text(
                                                spans=[
                                                    ft.TextSpan(
                                                        text="Vanick",
                                                        style=ft.TextStyle(
                                                            size=150,
                                                            font_family='titulo_decorado',
                                                            color='white',
                                                            foreground=ft.Paint(
                                                                color=ft.colors.PINK_ACCENT_700,
                                                                stroke_width=10,
                                                                stroke_join=ft.StrokeJoin.ROUND,
                                                                style=ft.PaintingStyle.STROKE,
                                                            ),
                                                        )
                                                    )
                                                ],
                                            )
                                        ),

                                        ft.Container(
                                            padding=ft.padding.only(left=450, top=-50),
                                            content=ft.Text(
                                                spans=[
                                                    ft.TextSpan(
                                                        text="Thrift Store",
                                                        style=ft.TextStyle(
                                                            size=40,
                                                            font_family='subtitulo_decorado',
                                                            color='white'
                                                        )
                                                    )
                                                ],
                                            )
                                        ),

                                        ft.Container(height=355),

                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.END,
                                                controls=[
                                                    ft.Text(value='Programa', color='white', size=20,
                                                            font_family='versionamento'),
                                                    ft.Text(value=f'v{versoes[0][0]}', color='white',
                                                            size=20, weight=ft.FontWeight.BOLD,
                                                            font_family='versionamento'),
                                                ]
                                            ),
                                        ),

                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.END,
                                                controls=[
                                                    ft.Text(value='Banco de dados', color='white', size=20,
                                                            font_family='versionamento'),
                                                    ft.Text(value=f'v{versoes[0][1]}', color='white',
                                                            size=20, weight=ft.FontWeight.BOLD,
                                                            font_family='versionamento'),
                                                ]
                                            ),
                                        ),
                                    ]
                                )
                            )
                        ]
                    ),
                ]
            )
        ]

        return conteudo
