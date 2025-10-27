# Instala o cliente SOAP moderno
!pip install zeep

from zeep import Client, Settings
from zeep.transports import Transport
from requests import Session
import config  
def connect_afa(wsdl_url):
    """
    Conecta-se ao AlgoSec Firewall Analyzer (AFA) via SOAP (Zeep).
    
    Args:
        wsdl_url (str): URL do arquivo WSDL do servidor AlgoSec
                        (ex: "https://<server>/AFA/php/wsdl.php")

    Returns:
        response (dict): resposta SOAP com o session ID ou erro
    """
    username = config.algosec['username']
    password = config.algosec['password']

    # Configurações de transporte (para HTTPS seguro)
    session = Session()
    session.verify = False  # desativa verificação SSL (somente para testes)
    transport = Transport(session=session)

    # Cria o cliente Zeep
    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(wsdl=wsdl_url, settings=settings, transport=transport)

    # Realiza a autenticação
    try:
        response = client.service.ConnectRequest(UserName=username, Password=password)
        print("Conexão bem-sucedida com o AlgoSec AFA")
        return response
    except Exception as e:
        print("Erro ao conectar ao servidor AlgoSec:", e)
        return None

# Exemplo de uso:
# wsdl = "https://<seu-servidor>/AFA/php/wsdl.php"
# session_id = connect_afa(wsdl)
# print(session_id)
