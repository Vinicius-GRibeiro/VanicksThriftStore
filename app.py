import flet as ft
import gui.controlador_de_rotas as rotas
import gui.view_produtos as vp
import gui.view_inicio as vi
import gui.view_vendas as vv
import gui.view_configuracoes as vc
import gui.view_login as vl
import os

largura = 720 * 1.9
altura = 405 * 1.9


def main(page: ft.Page):
    def eventos_da_janela(e):
        if e.data == "close":
            page.dialog = confirmar_fechar_dialogo_de_confirmacao
            confirmar_fechar_dialogo_de_confirmacao.open = True
            page.update()

    page.window_width = largura
    page.window_height = altura
    page.window_maximized = True
    page.window_maximizable = False
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.title = "Vanick - Sistema de gestão"
    page.window_always_on_top = False
    page.window_prevent_close = True
    page.on_window_event = eventos_da_janela

    page.fonts = {
        'titulo_decorado': 'assets/fonts/beautiful_barbies.otf',
        'subtitulo_decorado': 'assets/fonts/headlines.otf',
        'versionamento': 'assets/fonts/monocode.ttf'
    }

    view_produtos = vp.ViewProdutos(pagina=page)
    view_inicio = vi.ViewInicio(pagina=page)
    view_vendas = vv.ViewVendas(pagina=page)
    view_configuracoes = vc.ViewConfiguracoes(pagina=page)
    view_login = vl.ViewLogin(pagina=page)

    rotas.controlador_de_rotas(page=page, lista_de_views=[view_inicio, view_produtos, view_vendas,
                                                          view_configuracoes, view_login])

    def confirmar_fechar_janela_ao_clicar_no_sim(e):
        os.environ["USER_ID"] = 'vazio'
        os.environ["USER_NOME"] = 'vazio'
        os.environ["USER_LOGIN"] = 'vazio'
        os.environ["USER_SENHA_HASH"] = 'vazio'
        os.environ["USER_EMAIL"] = 'vazio'
        os.environ["USER_TELEFONE"] = 'vazio'
        os.environ["USER_NIVEL_ACESSO"] = 'vazio'
        page.window_destroy()

    def confirmar_fechar_janela_ao_clicar_no_nao(e):
        confirmar_fechar_dialogo_de_confirmacao.open = False
        page.update()

    confirmar_fechar_dialogo_de_confirmacao = ft.AlertDialog(
        modal=True,
        title=ft.Text("Por favor, confirme", color=ft.colors.PINK_ACCENT_700, weight=ft.FontWeight.BOLD),
        content=ft.Text("Você realmente deseja fechar o programa?"),
        actions=[
            ft.TextButton(text='Sim, encerrar o programa',
                          style=ft.ButtonStyle(
                            color=ft.colors.PINK_ACCENT_700
                          ),
                          on_click=confirmar_fechar_janela_ao_clicar_no_sim),
            ft.TextButton(text='Não',
                          style=ft.ButtonStyle(
                              color=ft.colors.PINK_ACCENT_700
                          ),
                          on_click=confirmar_fechar_janela_ao_clicar_no_nao),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


ft.app(target=main)
