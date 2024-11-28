from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    # Configurações do navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Modo anônimo
    options.add_argument("--start-maximized")  # Maximizar janela

    # Inicializa o navegador Chrome
    context.browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    # Ajusta o zoom da página (opcional)
    context.browser.execute_script("document.body.style.zoom='100%'")


def after_all(context):
    # Encerra o navegador após os testes
    context.browser.quit()