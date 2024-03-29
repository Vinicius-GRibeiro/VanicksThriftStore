import flet as ft
import controladores.controlador_view_produtos as ctrl_vp
import controladores.controlador_view_vendas as ctrl_vv
import controladores.controlador_view_configuracoes as ctrl_vc


def controlador_de_rotas(page: ft.Page, lista_de_views: list):
    def mudar_rota(route):  # type: ignore
        inicio = lista_de_views[0]
        produtos = lista_de_views[1]
        vendas = lista_de_views[2]
        configuracoes = lista_de_views[3]
        login = lista_de_views[-1]

        page.views.clear()
        page.views.append(login.view_())

        if page.route == '/login':
            page.views.append(login.view_())
        elif page.route == '/inicio':
            page.views.append(inicio.view_())
        elif page.route == '/produtos':
            page.views.append(produtos.view_())
            ctrl_vp.atualizar_view_produtos_adicionar(view=produtos, pagina=page)
            ctrl_vp.atualizar_view_produtos_consultar(view=produtos, pagina=page)
        elif page.route == '/vendas':
            page.views.append(vendas.view_())
            ctrl_vv.redefinir_view_vendas_novo(pagina=page, view=vendas)
        elif page.route == '/configuracoes':
            page.views.append(configuracoes.view_())
            ctrl_vc.resetar_aba_conta(pagina=page, view=configuracoes)

    def view_pop(view):  # type: ignore
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudar_rota
    page.on_view_pop = view_pop
    page.go(page.route)
