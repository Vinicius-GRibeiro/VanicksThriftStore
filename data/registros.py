import logging
from pathlib import Path


class Logger:
    def __init__(self):
        caminho_documentos = Path.home() / "Documents"
        sistema_vanick_path = caminho_documentos / "Sistema Vanick"
        sistema_vanick_path.mkdir(parents=True, exist_ok=True)
        caminho_log = sistema_vanick_path / "vanick.log"

        self.nome_arquivo = caminho_log
        self.logger = self._configurar_logger()

    def _configurar_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(self.nome_arquivo)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    def registrar_info(self, mensagem):
        self.logger.info(mensagem)

    def registrar_erro(self, mensagem):
        self.logger.error(mensagem)