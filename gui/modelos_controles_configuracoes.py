import os
import flet as ft
from flet.security import encrypt, decrypt
from abc import ABC, abstractmethod
import controladores.controlador_view_configuracoes as ctrl_vc
import controladores.utils as util
import data.data_model as sgdb
import re

db = sgdb.SGBD()


class Abas:
    def __init__(self, pagina: ft.Page, conteudo_tab_1: ft.Container, conteudo_tab_2: ft.Container,
                 conteudo_tab_3: ft.Container, conteudo_tab_4: ft.Container, conteudo_tab_5: ft.Container):
        self.conteudo_tab_1 = conteudo_tab_1
        self.conteudo_tab_2 = conteudo_tab_2
        self.conteudo_tab_3 = conteudo_tab_3
        self.conteudo_tab_4 = conteudo_tab_4
        self.conteudo_tab_5 = conteudo_tab_5
        self.tabs, self.tabs_container = self._retornar_tabs()

    def _retornar_tabs(self):
        tabs = ft.Tabs(
            indicator_tab_size=False,
            selected_index=0,
            divider_color='transparent',
            tabs=[
                ft.Tab(content=self.conteudo_tab_1),
                ft.Tab(content=self.conteudo_tab_2),
                ft.Tab(content=self.conteudo_tab_3),
                ft.Tab(content=self.conteudo_tab_4),
                ft.Tab(content=self.conteudo_tab_5)
            ]
        )

        tabs_container = ft.Container(
            width=800,
            height=600,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        width=800,
                        height=600,
                        content=ft.Stack(
                            controls=[
                                tabs,
                                ft.Container(  # Cabeçalho da página de vendas
                                    bgcolor=ft.colors.PINK_500,
                                    width=800,
                                    height=50,
                                    alignment=ft.alignment.center,
                                    border_radius=20,
                                    border=ft.border.only(
                                        top=ft.BorderSide(5, ft.colors.PINK_ACCENT_700),
                                        right=ft.BorderSide(5, ft.colors.PINK_ACCENT_700)
                                    ),
                                    content=ft.Text(
                                        value='CONFIGURAÇÕES',
                                        text_align=ft.TextAlign.CENTER,
                                        size=25,
                                        weight=ft.FontWeight.BOLD,
                                        color='white'
                                    )
                                ),
                            ]
                        )
                    )
                ]
            )
        )

        return tabs, tabs_container


class BotaoParaOSubMenu:
    def __init__(self, pagina: ft.Page, icone: str, texto: str, tamanho_icone: int, tamanho_texto: int, tabs: Abas,
                 caixas_de_texto: [ft.Control] = None):
        self._pagina = pagina
        self._icone = icone
        self._texto = texto
        self._tamanho_icone = tamanho_icone
        self._tamanho_texto = tamanho_texto
        self._tabs = tabs
        self._caixas_de_texto = caixas_de_texto
        self.item_container = self._item_botao()

    def _item_botao(self):
        botao = ft.IconButton(
            on_click=lambda _: self._ao_clicar_no_botao(),
            icon=self._icone,
            icon_size=self._tamanho_icone,
            icon_color=ft.colors.WHITE
        )

        item_container = ft.Container(
            on_click=lambda _: self._ao_clicar_no_botao(),
            on_hover=lambda e: self._destacar_botao(e),
            width=100,
            height=100,
            border_radius=20,
            content=ft.Column(
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    botao,
                    ft.Text(
                        value=self._texto,
                        size=self._tamanho_texto,
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD
                    ),

                ]
            )
        )

        return item_container

    def _ao_clicar_no_botao(self):
        match self._texto:
            case 'Conta':
                self._tabs.tabs.selected_index = 0
                ctrl_vc.resetar_aba_conta(pagina=self._pagina, caixas_de_texto=self._caixas_de_texto)
            case 'Geral':
                self._tabs.tabs.selected_index = 1
            case 'Relatórios':
                self._tabs.tabs.selected_index = 2
            case 'Usuários':
                self._tabs.tabs.selected_index = 3
            case 'DEV':
                self._tabs.tabs.selected_index = 4
        self._pagina.update()

    @staticmethod
    def _destacar_botao(e):
        if e.data == 'true':
            e.control.bgcolor = ft.colors.with_opacity(0.3, ft.colors.WHITE)
            e.control.update()
            e.control.content.controls[0].icon_color = ft.colors.WHITE
            e.control.content.controls[1].color = ft.colors.WHITE
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = ft.colors.WHITE
            e.control.content.controls[1].color = ft.colors.WHITE
            e.control.content.update()


class CaixaDeTextoBordaUnica:
    def __init__(self, pagina: ft.Page, label: str, largura_caixa: int, largura_container: int, altura_caixa: int,
                 altura_container: int,
                 texto_dica: str = None, destacar: bool = False, somente_leitura: bool = False,
                 regex_filtro: str = None, maiusculo: bool = False):
        self._pagina = pagina
        self._label = label
        self._texto_dica = texto_dica
        self._largura_caixa = largura_caixa
        self._largura_container = largura_container
        self._altura_caixa = altura_caixa
        self._altura_container = altura_container
        self._destacar = destacar
        self._somente_leitura = somente_leitura
        self._regex_filtro = regex_filtro
        self._maiusculo = maiusculo
        self.item, self.item_container = self._item_caixa()

    def _item_caixa(self):
        item = ft.TextField(
            label=self._label,
            border=ft.InputBorder('underline'),
            border_color=ft.colors.PINK_ACCENT_700,
            focused_border_color=ft.colors.PINK_ACCENT_700,
            content_padding=ft.padding.only(bottom=10),
            hint_text=self._texto_dica,
            width=self._largura_caixa,
            height=self._altura_caixa,
            label_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                weight=ft.FontWeight.BOLD,
                size=20
            ),
            text_style=ft.TextStyle(
                color=ft.colors.PINK_ACCENT_700,
                size=20
            ),
            read_only=self._somente_leitura,
            input_filter=ft.InputFilter(regex_string=self._regex_filtro) if self._regex_filtro is not None else None,
            capitalization=ft.TextCapitalization.CHARACTERS if self._maiusculo else ft.TextCapitalization.NONE
        )

        item_container = ft.Container(
            bgcolor='blue' if self._destacar else None,
            content=item,
            width=self._largura_container,
            height=self._altura_container,
        )

        return item, item_container


class _BotaoTextoPadrao(ABC):
    def __init__(self, pagina: ft.Page, tipo: str, controles_da_aba: [ft.Control], texto: str = None, icone: str = None,
                 tamanho_icone: int = 10, cor_padrao: str = ft.colors.PINK_500, tamanho_texto: int = 15,
                 largura: int = 50, altura: int = 25):
        self.pagina = pagina
        self.texto = texto
        self.icone = icone
        self.tipo = tipo
        self.tamanho_icone = tamanho_icone
        self.tamanho_texto = tamanho_texto
        self.altura = altura
        self.largura = largura
        self.cor_padrao = cor_padrao
        self.controles_da_aba = controles_da_aba
        self.item, self.item_container = self._item_botao_texto()

    def _item_botao_texto(self):
        conteudo = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)

        if self.icone is not None:
            conteudo.controls.append(
                ft.Icon(name=self.icone, size=self.tamanho_icone)
            )

        if self.texto is not None:
            conteudo.controls.append(
                ft.Text(value=self.texto, weight=ft.FontWeight.BOLD, size=self.tamanho_texto),
            )

        item = ft.TextButton(
            content=conteudo,
            width=self.largura,
            height=self.altura,

            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: ft.colors.WHITE,
                    ft.MaterialState.HOVERED: self.cor_padrao
                },
                bgcolor={
                    ft.MaterialState.DEFAULT: self.cor_padrao,
                    ft.MaterialState.HOVERED: ft.colors.WHITE
                }
            ),
            on_click=lambda e: self._ao_clicar_no_botao()
        )

        item_container = ft.Container(
            content=item,
            width=self.largura,
            height=self.altura,
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=10)
        )

        return item, item_container

    @abstractmethod
    def _ao_clicar_no_botao(self):
        ...


class BotaoTextoPadraoConta(_BotaoTextoPadrao):
    def __init__(self, pagina: ft.Page, tipo: str, controles_da_aba: [ft.Control], texto: str = None, icone: str = None,
                 tamanho_icone: int = 10, cor_padrao: str = ft.colors.PINK_500, tamanho_texto: int = 15,
                 largura: int = 50, altura: int = 25):
        super().__init__(pagina, tipo, controles_da_aba, texto, icone, tamanho_icone, cor_padrao, tamanho_texto, largura,
                         altura)

    def _ao_clicar_no_botao(self):
        tamanho_minimo_de_nome_de_usuario = 5
        match self.tipo:
            case 'conta_salvar_alteracoes':
                codigo = self.controles_da_aba[0]
                nome = self.controles_da_aba[1]
                usuario = self.controles_da_aba[2]
                email = self.controles_da_aba[3]
                telefone = self.controles_da_aba[4]
                nivel = self.controles_da_aba[5]

                if len(usuario.value) < tamanho_minimo_de_nome_de_usuario:
                    util.mostrar_notificacao(page=self.pagina, mensagem='O nome de usuário deve ter no mínimo '
                                                                        f'{tamanho_minimo_de_nome_de_usuario} '
                                                                        f'caracteres. Ele será usado para realizar '
                                                                        f'o login.', emoji='🥺')
                    return None

                padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                if not re.match(padrao_email, email.value):
                    util.mostrar_notificacao(page=self.pagina, mensagem='O e-mail inserido não é válido', emoji='🥺')
                    return None

                if nome.value == '' or telefone.value == '':
                    util.mostrar_notificacao(page=self.pagina, mensagem='Nenhum campo pode ficar vazio', emoji='🥺')
                    return None

                exito = db.editar_registro_usuario(id_=codigo.value, nome=nome.value, login=usuario.value,
                                                   email=email.value, telefone=str(telefone.value))

                if not exito:
                    util.mostrar_notificacao(page=self.pagina, tipo='erro', mensagem='Houve um erro ao salvar os dados'
                                                                                     ' do usuario', emoji='🥴')
                    return None

                util.mostrar_notificacao(page=self.pagina, tipo='exito', mensagem='Os novos dados do usuário, '
                                                                                  'foram salvos. Os dados serão '
                                                                                  'atualizados na próxima vez em que '
                                                                                  'você fizer login', emoji='😉')

            case 'conta_alterar_senha':
                senha_atual = ft.TextField(label='Senha atual', password=True,
                                           can_reveal_password=True,
                                           border_color=ft.colors.PINK_ACCENT_700,
                                           border_radius=10,
                                           text_style=ft.TextStyle(
                                               color=ft.colors.PINK_ACCENT_700,
                                               size=20
                                           ),
                                           label_style=ft.TextStyle(
                                               color=ft.colors.PINK_ACCENT_700,
                                               weight=ft.FontWeight.BOLD
                                           ))
                nova_senha = ft.TextField(label='Nova senha', password=True,
                                          can_reveal_password=True,
                                          border_color=ft.colors.PINK_ACCENT_700,
                                          border_radius=10,
                                          text_style=ft.TextStyle(
                                              color=ft.colors.PINK_ACCENT_700,
                                              size=20
                                          ),
                                          label_style=ft.TextStyle(
                                              color=ft.colors.PINK_ACCENT_700,
                                              weight=ft.FontWeight.BOLD
                                          ))
                confirmar_nova_senha = ft.TextField(label='Confirme a nova senha', password=True,
                                                    can_reveal_password=True,
                                                    border_color=ft.colors.PINK_ACCENT_700,
                                                    border_radius=10,
                                                    text_style=ft.TextStyle(
                                                        color=ft.colors.PINK_ACCENT_700,
                                                        size=20
                                                    ),
                                                    label_style=ft.TextStyle(
                                                        color=ft.colors.PINK_ACCENT_700,
                                                        weight=ft.FontWeight.BOLD
                                                    ))
                texto_retorno = ft.Text(value='')
                senha = decrypt(os.getenv('USER_SENHA_HASH'), os.getenv('CHAVE_DE_CODIFICACAO'))

                def _ao_clicar_em_cancelar():
                    dlg.open = False
                    self.pagina.update()

                def _ao_clicar_em_confirmar():
                    if senha_atual.value == '' or nova_senha.value == '' or confirmar_nova_senha.value == '':
                        texto_retorno.value = 'Preencha todos os campos'
                        texto_retorno.color = ft.colors.RED_900
                        self.pagina.update()
                        return None

                    if senha_atual.value != senha:
                        texto_retorno.value = 'A senha atual está incorreta'
                        texto_retorno.color = ft.colors.RED_900
                        self.pagina.update()
                        return None

                    if nova_senha.value != confirmar_nova_senha.value:
                        texto_retorno.value = 'As novas senhas não são iguais'
                        texto_retorno.color = ft.colors.RED_900
                        self.pagina.update()
                        return None

                    senha_hash = encrypt(nova_senha.value, os.getenv('CHAVE_DE_CODIFICACAO'))
                    exito_ = db.editar_registro_usuario(id_=self.controles_da_aba[0].value, senha=str(senha_hash))
                    if exito_:
                        senha_atual.value = ''
                        nova_senha.value = ''
                        confirmar_nova_senha.value = ''
                        texto_retorno.value = 'Senha alterada'
                        texto_retorno.color = ft.colors.GREEN_800
                        self.pagina.update()
                        return None

                    dlg.open = False
                    util.mostrar_notificacao(page=self.pagina, mensagem='Houve um erro ao tentar alterar a senha',
                                             tipo='erro', emoji='🙀')
                    self.pagina.update()

                dlg = ft.AlertDialog(
                    title=ft.Text('Confirmação', color=ft.colors.PINK_ACCENT_700, weight=ft.FontWeight.BOLD),
                    content=ft.Column(
                        height=250,
                        controls=[
                            ft.Text('Por favor, confirme sua senha atual e a nova senha', color=ft.colors.PINK_ACCENT_700),
                            senha_atual, nova_senha, confirmar_nova_senha, texto_retorno,
                            ft.Container(height=100, width=10)
                        ]
                    ),
                    actions=[
                        ft.TextButton(text='Confirmar', style=ft.ButtonStyle(color=ft.colors.PINK_ACCENT_700),
                                      on_click=lambda e: _ao_clicar_em_confirmar()),
                        ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.PINK_ACCENT_700),
                                      on_click=lambda e: _ao_clicar_em_cancelar())
                    ],
                    actions_alignment=ft.MainAxisAlignment.END
                )

                self.pagina.dialog = dlg
                dlg.open = True
                self.pagina.update()
