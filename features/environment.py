import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave.model_core import Status

# Hooks
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window() 
    context.wait = WebDriverWait(context.driver, 10)

def after_scenario(context, scenario):
    time.sleep(10)
    print(scenario.name)
    if scenario.status == Status.failed:
        # Tirar uma screenshot se o cenário falhar
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)
    context.driver.quit()