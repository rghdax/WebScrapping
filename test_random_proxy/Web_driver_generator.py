import random
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def read_proxies(filename):
    # Selección aleatoria de proxy ubicada en el fichero proxy_list.txt
    proxy_list = open(filename).read().splitlines()
    return random.choice(proxy_list)

def User_Agent_and_Proxy ():

    # Creando un User-Agent aleatorio
    # Se elegiran tanto nombres de Mozilla como de Google Chrome
    software_names = [SoftwareName.FIREFOX.value, SoftwareName.CHROME.value]
    # Se elegiran sistemas operativos Windows y Linux
    operating_systems = [OperatingSystem.WINDOWS.value, 
                        OperatingSystem.LINUX.value]
        
    user_agent_rotator = UserAgent(software_names= software_names, 
                        operating_systems= operating_systems,
                        limit= 100)
    
    # Elección al azar del User Agent    
    user_agent = user_agent_rotator.get_random_user_agent()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", f"{user_agent}")

    # Configuración del navegador
    PROXY = read_proxies('./test_random_proxy/proxy_list.txt')

    webdriver.DesiredCapabilities.FIREFOX['proxy'] ={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        "proxyType": "MANUAL",
        }

    # Inicializando Web Driver
    options = webdriver.FirefoxOptions()
    options.add_argument("--incognito")
    options.add_argument("-- headless")
    driver = webdriver.Firefox(executable_path="./drivers/geckodriver.exe", 
                            firefox_profile = profile,
                            firefox_options = options)
        
    return(driver)
