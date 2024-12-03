import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave.model_core import Status

# Diretório de relatórios
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)
REPORT_FILE = os.path.join(REPORT_DIR, "test_report.txt")

# Hooks
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)

def after_scenario(context, scenario):
    time.sleep(2)
    # Registrar os resultados do cenário no relatório
    with open(REPORT_FILE, "a") as report:
        status = "PASSED" if scenario.status == Status.passed else "FAILED"
        report.write(f"Scenario: {scenario.name}\n")
        report.write(f"Status: {status}\n")
        report.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    # Tirar uma screenshot se o cenário falhar
    if scenario.status == Status.failed:
        screenshot_dir = os.path.join(REPORT_DIR, "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)

    # Fechar o driver
    context.driver.quit()

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
