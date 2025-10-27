#!pip install SOAPpy
from SOAPpy import SOAPProxy
import config

def connect_afa(server):
    """Connect To AlgoSec FA

    Args:
        server (SOAPProxy): A SOAPProxy connection

    Returns:
        response (str): A string containing the session ID
    """
    username = config.algosec['username']
    password = config.algosec['password']
    response = server.ConnectRequest(UserName=username, Password=password)
    return response
