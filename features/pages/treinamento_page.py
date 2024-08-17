from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class TreinamentoPage(BasePage):
    ICONE_CARRINHO = (By.CSS_SELECTOR, '#shopping_cart_container')
    CAMPO_USUARIO = (By.CSS_SELECTOR, '#user-name')
    CAMPO_SENHA = (By.CSS_SELECTOR, '#password')
    BOTAO_LOGIN = (By.CSS_SELECTOR, '#login-button')
    BOTAO_CONTINUE = (By.CSS_SELECTOR, '#continue')
    BOTAO_FINISH = (By.CSS_SELECTOR, '#finish')
    BOTAO_ADD_TO_CART_BAG = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    BOTAO_CHECKOUT = (By.CSS_SELECTOR, '#checkout')
    IMAGEM_BLACKPACK = (By.CSS_SELECTOR, '#item_4_img_link')
    CAMPO_FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    CAMPO_LAST_NAME = (By.CSS_SELECTOR, '#last-name')
    CAMPO_POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')
    BOTAO_MENU = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    BOTAO_ADD_TO_CART = (By.CSS_SELECTOR, '#shopping_cart_container')
    BOTAO_ADD_BOLT_SHIRT = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    BOTAO_ADD_MACACAO = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
    BOTAO_REMOVER_BOLT_SHIRT= (By.CSS_SELECTOR, '#remove-sauce-labs-bolt-t-shirt')
    BOTAO_CONTINUAR_COMPRANDO = (By.CSS_SELECTOR, '#continue-shopping')

    
    def clicar_botao_menu(self):
        self.driver.find_element(*self.BOTAO_ADD_BOLT_SHIRT).click()

    def clicar_botao_continuar_comprando(self):
       self.driver.find_element(*self.BOTAO_CONTINUAR_COMPRANDO).click()

    def clicar_botao_adicionar_bolt_tshirt(self):
       self.driver.find_element(*self.BOTAO_ADD_MACACAO).click()
    
    def clicar_botao_remover_bolt_tshirt(self):
       self.driver.find_element(*self.BOTAO_REMOVER_BOLT_SHIRT).click()
    
    def clicar_botao_adicionar_macacao(self):
       self.driver.find_element(*self.BOTAO_MENU).click()

    def clicar_imagem_blackpacK(self):
        self.driver.find_element(*self.IMAGEM_BLACKPACK).click()
    
    def preencher_campo_usuario(self, usuario):
        campo_usuario = self.driver.find_element(*self.CAMPO_USUARIO)
        campo_usuario.send_keys(usuario)

    def preencher_campo_senha(self, senha):
        campo_senha = self.driver.find_element(*self.CAMPO_SENHA)
        campo_senha.send_keys(senha)

    def clicar_botao_login(self):
        self.driver.find_element(*self.BOTAO_LOGIN).click()

    def clicar_carrinho_compras(self):
        self.driver.find_element(*self.ICONE_CARRINHO).click()
    
    def clicar_botao_add_to_cart_bag(self):
        self.driver.find_element(*self.BOTAO_ADD_TO_CART_BAG).click()
    
    def clicar_botao_add_to_cart(self):
        self.driver.find_element(*self.BOTAO_ADD_TO_CART).click()
    
    def clicar_botao_checkout(self):
     self.driver.find_element(*self.BOTAO_CHECKOUT).click()
    
    def preencher_campo_first_name(self, nome):
        campo_nome = self.driver.find_element(*self.CAMPO_FIRST_NAME)
        campo_nome.send_keys(nome)
    
    def preencher_campo_last_name(self, sobrenome):
        campo_nome = self.driver.find_element(*self.CAMPO_LAST_NAME)
        campo_nome.send_keys(sobrenome)
    
    def preencher_campo_postal_code(self, postalcode):
        campo_nome = self.driver.find_element(*self.CAMPO_POSTAL_CODE)
        campo_nome.send_keys(postalcode)
    
    def clicar_botao_continue(self):
     self.driver.find_element(*self.BOTAO_CONTINUE).click()
    
    def clicar_botao_finish(self):
     self.driver.find_element(*self.BOTAO_FINISH).click()
