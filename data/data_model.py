import sqlite3
from pathlib import Path
from data.registros import Logger

_possiveis_excecoes = (sqlite3.DataError, sqlite3.OperationalError, sqlite3.IntegrityError, sqlite3.ProgrammingError,
                       sqlite3.InterfaceError, sqlite3.InternalError, sqlite3.DatabaseError, sqlite3.Error)


class SGBD:
    def __init__(self):
        self._nome_banco = f"{Path.home()}/OneDrive/Área de Trabalho/vanick_bdd.db"
        self._conexao = None
        self._cursor = None
        self._log = Logger()

    def _conectar(self):
        try:
            self._conexao = sqlite3.connect(self._nome_banco)
            self._cursor = self._conexao.cursor()
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Erro ao CONECTAR ao banco "{self._nome_banco}".\n\t'
                                              f'Descrição do erro: {e}\n')

    def _desconectar(self):
        try:
            self._cursor.close()
            self._conexao.close()
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Erro ao DESCONECTAR do banco "{self._nome_banco}".\n\t'
                                              f'Descrição do erro: {e}\n')

    def _criar_tabelas(self):
        try:
            self._conectar()

            criar_categoria = f'''
                                CREATE TABLE IF NOT EXISTS categoria (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT
                                )
                                '''

            criar_estado = f'''
                            CREATE TABLE IF NOT EXISTS estado (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT
                            )
                            '''

            criar_produto = f'''
                CREATE TABLE IF NOT EXISTS venda (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    quantidade INTEGER,
                    preco REAL,
                    categoria TEXT,
                    estado TEXT,
                    descricao TEXT
                )
            '''

            criar_venda = f'''
                CREATE TABLE IF NOT EXISTS venda (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_hora INTEGER,
                    valor_total REAL,
                    status TEXT DEFAULT 'realizado'
                )
            '''

            criar_itens_venda = f'''
                            CREATE TABLE IF NOT EXISTS itens_venda (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_produto INTEGER,
                                id_venda INTEGER,
                                nome TEXT,
                                qntd_anterior INTEGER,
                                preco REAL,
                                categoria TEXT,
                                estado TEXT,
                                descricao TEXT,
                                FOREIGN KEY (id_venda) REFERENCES venda(id)
                            )
                        '''

            self._cursor.execute(criar_venda)
            self._cursor.execute(criar_itens_venda)
            self._cursor.execute(criar_categoria)
            self._cursor.execute(criar_estado)
            self._cursor.execute(criar_produto)

            self._conexao.commit()

            self._desconectar()
        except _possiveis_excecoes as e:
            print(e)
            self._desconectar()

    def inserir_registros(self, tipo: str, categoria_nome: str = None, estado_nome: str = None,
                          prod_nome: str = None, prod_quantidade: int = None, prod_preco: float = None,
                          prod_categoria: str = None, prod_estado: str = None, prod_descricao: str = None,
                          venda_data_hora: int = None, venda_valor_total: float = None,item_venda_id: int = None,
                          iv_id_venda: int = None, iv_nome: str = None, iv_qntd_anterior: int = None,
                          iv_preco: float = None, iv_categoria: str = None, iv_estado: str = None,
                          iv_descricao: str = None, iv_id_produto: int = None) -> bool:
        query = None
        valores = None
        try:
            self._conectar()
            match tipo:
                case 'categoria':
                    query = f"INSERT INTO categoria (nome) VALUES (?)"
                    valores = (categoria_nome,)
                case 'estado':
                    query = f"INSERT INTO estado (nome) VALUES (?)"
                    valores = (estado_nome,)
                case 'produto':
                    query = (f"INSERT INTO produto (nome, quantidade, preco, categoria, estado, descricao)"
                             f" VALUES (?, ?, ?, ?, ?, ?)")
                    valores = (prod_nome, prod_quantidade, prod_preco, prod_categoria, prod_estado, prod_descricao,)
                case 'venda':
                    query = f"INSERT INTO venda (data_hora, valor_total) VALUES (?, ?)"
                    valores = (venda_data_hora, venda_valor_total,)
                case 'venda_item':
                    query = (f"INSERT INTO itens_venda (id_venda, id_produto, nome, qntd_anterior, preco, categoria, estado, descricao)"
                             f" VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
                    valores = (iv_id_venda, iv_id_produto, iv_nome, iv_qntd_anterior, iv_preco, iv_categoria, iv_estado, iv_descricao,)

            self._cursor.execute(query, valores)
            self._conexao.commit()

            self._log.registrar_info(mensagem=f'Registro inserido. "{str(tipo).capitalize()}" - {valores}\n')
            return True
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Erro ao inserir registro. "{str(tipo).capitalize()}" - {valores}\n\t'
                                              f'Descrição do erro: {e}\n')
            return False
        finally:
            self._desconectar()

    def recuperar_registros(self, tabela: str, colunas: str | tuple = '*',
                            condicao: str = None, ordernar_por_coluna: str = None):
        query = None
        try:
            self._conectar()
            query = f'SELECT {colunas} FROM {tabela}'

            if condicao is not None:
                query += f' WHERE {condicao}'
            if ordernar_por_coluna is not None:
                query += f' ORDER BY {ordernar_por_coluna}'

            self._cursor.execute(query)
            dados = self._cursor.fetchall()
            return dados
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Houve um erro ao tentar recuperar os registros da tabela "{tabela}".'
                                              f' Query "{query}".\n\tDescrição do erro: {e}\n')
            return None
        finally:
            self._desconectar()

    def recuperar_proximo_id(self, tabela: str):
        try:
            self._conectar()

            query = (f"SELECT seq FROM sqlite_sequence WHERE name = '{tabela}'")
            self._cursor.execute(query)
            proximo_id = self._cursor.fetchone()[0]
            return proximo_id + 1
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Houve um erro ao recuperar o ID da tabela "{tabela}".\n\t'
                                              f'Descrição do erro: {e}\n')
            return -1
        finally:
            self._desconectar()

    def deletar_registro(self, tabela: str, condicao: str) -> bool:
        deletado = None
        try:
            self._conectar()

            query_recuperar = f"SELECT * FROM {tabela} WHERE {condicao}"
            query_deletar = f"DELETE FROM {tabela} WHERE {condicao}"

            self._cursor.execute(query_recuperar)
            deletado = self._cursor.fetchall()

            self._cursor.execute(query_deletar)
            self._conexao.commit()

            self._log.registrar_info(mensagem=f'Registro deletado. Tabela: {tabela} - {deletado}\n')
            return True
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Houve um erro ao tentar excluir da tabela "{tabela}",'
                                              f' o registro {deletado}.\n\tDescrição do erro: {e}\n')
            return False
        finally:
            self._desconectar()

    def editar_registros_produto(self, prod_id: int = None, prod_nome: str = None, prod_quantidade: int = None,
                                 prod_preco: float = None, prod_categoria: str = None, prod_estado: str = None,
                                 prod_descricao: str = None, condicao: str = None) -> bool:
        query_update = None
        query_consulta = None
        valores = None

        try:
            antes = self.recuperar_registros(tabela='produto', condicao=f'id = {prod_id}')

            self._conectar()
            query_update = ("UPDATE produto "
                            "SET nome = ?, quantidade = ?, preco = ?, categoria = ?, estado = ?, descricao = ? "
                            f"WHERE {condicao}")
            valores = (prod_nome, prod_quantidade, prod_preco, prod_categoria, prod_estado, prod_descricao)

            self._cursor.execute(query_update, valores)
            self._conexao.commit()

            self._log.registrar_info(mensagem=f'Registro de produto editado.\n\tANTES: {antes}\n\tDEPOIS: {valores}\n')
            return True
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Erro ao editar registro de produto. PRODUTO: {prod_id} - {valores}\n\t'
                                              f'Descrição do erro: {e}\n')
            return False
        finally:
            self._desconectar()

    def marcar_venda_como_cancelada(self, id_venda: int, produtos: list[tuple]):
        try:
            query_venda = f"UPDATE venda SET status = 'cancelado' WHERE id = {id_venda}"
            self._conectar()
            self._cursor.execute(query_venda)

            for produto in produtos:
                query_produto = f"UPDATE produto SET quantidade = quantidade + 1 WHERE id = {produto[0]}"
                self._cursor.execute(query_produto)

            self._conexao.commit()
            self._log.registrar_info(mensagem=f'Venda com o código {id_venda} CANCELADA.')

            return True
        except _possiveis_excecoes as e:
            self._log.registrar_erro(mensagem=f'Erro ao cancelar venda {id_venda}\n\t'
                                              f'Descrição do erro: {e}\n')
            return False
        finally:
            self._desconectar()




if __name__ == '__main__':
    db = SGBD()
    db._criar_tabelas()

    # db.inserir_registros(tipo='categoria', categoria_nome='ROUPAS')
    # db.inserir_registros(tipo='categoria', categoria_nome='ELETRÔNICOS')
    # db.inserir_registros(tipo='categoria', categoria_nome='BRINQUEDOS')
    # db.inserir_registros(tipo='categoria', categoria_nome='ALIMENTOS')

    # db.inserir_registros(tipo='estado', estado_nome='NOVO')
    # db.inserir_registros(tipo='estado', estado_nome='SEMINOVO')
    # db.inserir_registros(tipo='estado', estado_nome='USADO')

    # db.inserir_registros(tipo='produto', prod_nome='Camisa social', prod_preco=73.20, prod_quantidade=1,
    #                      prod_categoria='ROUPAS', prod_estado='NOVO')
    #
    # db.inserir_registros(tipo='produto', prod_nome='Casinha de boneca', prod_preco=255,
    #                      prod_quantidade=1, prod_categoria='BRINQUEDOS', prod_estado='NOVO')
    #
    # db.inserir_registros(tipo='produto', prod_nome='Fone de ouvido bluetooth', prod_preco=83.20, prod_quantidade=1,
    #                      prod_categoria='ELETRÔNICOS', prod_estado='NOVO')
