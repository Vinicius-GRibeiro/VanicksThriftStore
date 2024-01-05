import flet as ft


def mostrar_notificacao(page: ft.Page,  mensagem: str, tipo: str | None = None, emoji: str | None = None):
    cor_do_texto = ft.colors.BLACK
    cor_de_fundo = ft.colors.YELLOW_500

    match tipo:
        case 'exito':
            cor_de_fundo = ft.colors.LIGHT_GREEN
        case 'erro':
            cor_do_texto = ft.colors.WHITE
            cor_de_fundo = ft.colors.RED_900

    conteudo = ''
    if emoji is None:
        conteudo = ft.Text(value=mensagem, color=cor_do_texto, weight=ft.FontWeight.BOLD)
    else:
        conteudo = ft.Row(
            controls=[
                ft.Text(value=emoji, size=50),
                ft.Text(value=mensagem, color=cor_do_texto, weight=ft.FontWeight.BOLD)
            ]
        )

    notificacao = ft.SnackBar(
        padding=ft.padding.only(bottom=50, right=30, left=30, top=10),
        elevation=500,
        content=conteudo,
        bgcolor=cor_de_fundo,
        show_close_icon=True,
        close_icon_color=cor_do_texto
    )

    page.snack_bar = notificacao
    page.snack_bar.open = True
    page.update()


def verificar_se_existem_campos_vazios(page: ft.Page, controles: list) -> bool:
    nao_esta_vazio = True

    for item in controles:
        if item.label != 'Descrição':
            if item.value == '' or item.value is None:
                item.error_text = 'vazio'
                mostrar_notificacao(page=page, mensagem='Parece que você deixou alguns campos vazios', emoji='😅')
                nao_esta_vazio = False
            else:
                item.error_text = None

    page.update()
    return nao_esta_vazio
