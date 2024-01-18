from dotenv import load_dotenv
from flet.security import encrypt, decrypt
import os
import flet as ft

load_dotenv()

print(encrypt('a', os.getenv('CHAVE_DE_CODIFICACAO')))
