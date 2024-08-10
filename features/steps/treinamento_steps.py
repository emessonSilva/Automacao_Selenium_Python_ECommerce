from behave import given, when, then
from features.pages.treinamento_page import TreinamentoPage

# Region Teste Login Válido
@given(u'o usuário está na página de login')
def step_given_o_usuario_esta_na_pagina_de_login(context):
    context.driver.get("https://www.saucedemo.com")
    context.treinamento_page = TreinamentoPage(context.driver)

@when(u'o usuário insere um nome de usuário e senha válidos')
def step_when_o_usuario_inserir_credenciais_validas(context):
    context.treinamento_page.preencher_campo_usuario('standard_user')
    context.treinamento_page.preencher_campo_senha('secret_sauce')

@when(u'o usuário clica no botão de login')
def step_when_o_usuario_clica_no_botao_login(context):
    context.treinamento_page.clicar_botao_login()

@then(u'o usuário deve ser redirecionado para a página principal')
def step_then_o_usuario_deve_estar_na_pagina_principal(context):
    ...
# End Region