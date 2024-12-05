from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

"""
BasePage, é uma classe base (ou pai) para todas as páginas do seu projeto de automação de testes com Selenium. 
Ele encapsula funcionalidades comuns usadas em várias páginas para reduzir a duplicação de código e facilitar a reutilização.
"""
class BasePage:
    """
    A classe é inicializada com um objeto driver, que representa o navegador em que os testes estão sendo executados. 
    Esse driver é compartilhado entre as páginas e é usado para executar ações no navegador.
    O construtor recebe o driver do Selenium e o armazena como um atributo da classe. 
    Isso permite que qualquer método da classe utilize o driver para interagir com o navegador.
    """
    def __init__(self, driver):
        self.driver = driver

    """
    O método find_element localiza e retorna um elemento da página.
    O argumento *locator permite passar uma tupla contendo a estratégia de localização (ex.: By.ID, By.XPATH, etc.) e o seletor.
    """    

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    # def get_element_text(self, elemento):
    #     return elemento.get_attribute("value")
    
    # def get_alert_text(self):
    #     alert = Alert(self.driver)
    #     return alert.text
    
    # def accept_alert(self):
    #     alert = Alert(self.driver)
    #     alert.accept()

    """
    O método wait_for_element da classe BasePage é utilizado para aguardar a presença de um elemento na página antes de interagir com ele.
    Ele utiliza o WebDriverWait do Selenium, que implementa uma espera explícita, garantindo que o código não falhe devido a tentativas de 
    acessar elementos que ainda não estão disponíveis no DOM (Document Object Model).

    O método aceita dois parâmetros principais: timeout, que especifica o tempo máximo (em segundos) que o Selenium deve esperar pelo elemento, 
    e *locator, que é uma tupla contendo a estratégia de localização (como By.ID ou By.XPATH) e o seletor do elemento desejado.
    
    Quando a condição é atendida dentro do período especificado pelo timeout, o método retorna o elemento encontrado. 
    Caso o tempo se esgote sem que o elemento seja localizado, uma exceção TimeoutException será levantada.
    """
    def wait_for_element(self, timeout, *locator):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))