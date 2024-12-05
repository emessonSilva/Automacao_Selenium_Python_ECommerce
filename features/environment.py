import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave.model_core import Status

"""
REPORT_DIR: Define o diretório onde os relatórios serão armazenados.
os.makedirs: Cria a pasta reports caso ela ainda não exista.
REPORT_FILE: Especifica o caminho do arquivo de relatório (test_report.txt) dentro da pasta reports.

Como o valor de CURRENT_TIMESTAMP muda a cada execução (com base na data e hora), um novo arquivo é gerado sempre que o comando behave é executado.
Isso garante que os relatórios de diferentes execuções não sejam sobrescritos.
"""

# Diretório de relatórios
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)
CURRENT_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_FILE = os.path.join(REPORT_DIR, f"test_report_{CURRENT_TIMESTAMP}.txt")

"""
Função: Executada antes de cada cenário de teste.
context.driver: Inicializa o navegador (Chrome) para ser usado no teste.
implicitly_wait: Define um tempo máximo para o Selenium esperar por elementos no DOM.
maximize_window: Maximiza a janela do navegador.
WebDriverWait: Cria uma instância para esperas explícitas no Selenium.
"""
# Hooks
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 5)

"""
Função: Executada após cada cenário de teste.
time.sleep(1): Aguarda 1 segundos (útil para finalizar qualquer interação com o navegador antes de fechar).
Relatório de Cenário:
Abre o arquivo de relatório (REPORT_FILE) em modo de escrita.
Registra:
Nome do cenário (scenario.name).
Status do cenário (PASSED ou FAILED).
Data e hora em que o cenário foi executado.
"""
def after_scenario(context, scenario):
    time.sleep(1)
    # Registrar os resultados do cenário no relatório
    with open(REPORT_FILE, "a") as report:
        status = "PASSED" if scenario.status == Status.passed else "FAILED"
        report.write(f"Scenario: {scenario.name}\n")
        report.write(f"Status: {status}\n")
        report.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    """
    Se o cenário falhar, o Selenium captura uma screenshot e a imagem é armazenada na pasta screenshots
    """
    # Tirar uma screenshot se o cenário falhar
    if scenario.status == Status.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)

    # Fechar o driver
    context.driver.quit()

"""
Função: Executada após todos os cenários terem sido executados.
Relatório de Resumo:
Registra:
Total de cenários executados.
Quantidade de cenários aprovados e reprovados.
Data e hora do final da execução.
context._runner.features[0].scenarios: Acessa todos os cenários de teste.
Conta os cenários que falharam e calcula os aprovados.

"""

def after_all(context):
    # Consolidar resultados ao final de todos os testes
    with open(REPORT_FILE, "a") as report:
        report.write("\n")
        report.write("=" * 40 + "\n")
        report.write("Test Execution Summary\n")
        report.write("=" * 40 + "\n")
        total_scenarios = len(context._runner.features[0].scenarios)
        failed_scenarios = len([s for s in context._runner.features[0].scenarios if s.status == Status.failed])
        passed_scenarios = total_scenarios - failed_scenarios

        report.write(f"Total Scenarios: {total_scenarios}\n")
        report.write(f"Passed: {passed_scenarios}\n")
        report.write(f"Failed: {failed_scenarios}\n")
        report.write(f"Execution Finished At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write("=" * 40 + "\n")
