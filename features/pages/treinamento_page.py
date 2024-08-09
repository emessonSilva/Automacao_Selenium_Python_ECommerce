from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class TreinamentoPage(BasePage):
    BOTAO_CLICK_ME = (By.CSS_SELECTOR, '#buttonSimple')
    CAMPO_NOME = (By.CSS_SELECTOR, '#formNome')
    CAMPO_SOBRENOME = (By.CSS_SELECTOR, '#formSobrenome')
    RADIO_SEXO_MASCULINO = (By.CSS_SELECTOR, "#formSexoMasc")
    RADIO_SEXO_FEMININO = (By.CSS_SELECTOR, "#formSexoFem")
    BOTAO_CADASTRAR = (By.CSS_SELECTOR, "#formCadastrar")
    TEXTO_RESULTADO = (By.CSS_SELECTOR, "#resultado span") 

    def recuperar_texto_resultado(self):
        elemento = self.find_element(*self.TEXTO_RESULTADO)
        return elemento.get_attribute("textContent") 
    
    def preencher_campo_nome(self, valor):
        campo_nome = self.find_element(*self.CAMPO_NOME)
        campo_nome.clear()  
        campo_nome.send_keys(valor)

    def preencher_campo_sobrenome(self, valor):
        campo_sobrenome = self.find_element(*self.CAMPO_SOBRENOME)
        campo_sobrenome.clear()  
        campo_sobrenome.send_keys(valor)

    def clicar_sexo(self, sexo):
        if sexo == "Masculino":
            self.find_element(*self.RADIO_SEXO_MASCULINO).click()
        elif sexo == "Feminino":
            self.find_element(*self.RADIO_SEXO_FEMININO).click()
        else:
            raise ValueError(f"Sexo '{sexo}' não reconhecido")

    def clicar_botao_cadastrar(self):
        self.find_element(*self.BOTAO_CADASTRAR).click()

    def clicar_botao_click_me(self):
        botao_click_me = self.find_element(*self.BOTAO_CLICK_ME)
        texto_botao_antes = self.get_element_text(botao_click_me)
        assert texto_botao_antes == "Clique Me!"
        botao_click_me.click()

    def recuperar_texto_botao_click_me(self):
        return self.get_element_text(self.find_element(*self.BOTAO_CLICK_ME))

    def recuperar_texto_alert(self):
        texto_alert = self.get_alert_text()
        return str(texto_alert)
