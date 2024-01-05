import flet as ft
import gui.controlador_de_rotas as rotas
import gui.view_produtos as vp
import gui.view_inicio as vi
import gui.view_vendas as vv
import gui.view_configuracoes as vc

largura = 720 * 1.9
altura = 405 * 1.9


def main(page: ft.Page):
    page.window_width = largura
    page.window_height = altura
    page.window_maximizable = False
    page.window_maximized = True
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    view_produtos = vp.ViewProdutos(pagina=page)
    view_inicio = vi.ViewInicio(pagina=page)
    view_vendas = vv.ViewVendas(pagina=page)
    view_configuracoes = vc.ViewConfiguracoes(pagina=page)

    rotas.controlador_de_rotas(page=page, lista_de_views=[view_inicio, view_produtos, view_vendas, view_configuracoes])


ft.app(target=main)