from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class TreinamentoPage(BasePage):
    ICONE_CARRINHO = (By.CSS_SELECTOR, '#shopping_cart_container')
    CAMPO_USUARIO = (By.CSS_SELECTOR, '#user-name')
    CAMPO_SENHA = (By.CSS_SELECTOR, '#password')
    BOTAO_LOGIN = (By.CSS_SELECTOR, '#login-button')

    def preencher_campo_usuario(self, usuario):
        campo_usuario = self.driver.find_element(*self.CAMPO_USUARIO)
        campo_usuario.send_keys(usuario)

    def preencher_campo_senha(self, senha):
        campo_senha = self.driver.find_element(*self.CAMPO_SENHA)
        campo_senha.send_keys(senha)

    def clicar_botao_login(self):
        self.driver.find_element(*self.BOTAO_LOGIN).click()
