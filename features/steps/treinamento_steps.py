from behave import given, when, then
from features.pages.treinamento_page import TreinamentoPage

# region Teste Click Botão
@given(u'que a página de treinamento seja acessada')
def step_given_acessar_pagina(context):
    context.driver.get("https://wcaquino.me/cypress/componentes.html")
    context.treinamento_page = TreinamentoPage(context.driver)

@when(u'o botão "click me" for clicado')
def step_when_clicar_botao_click_me(context):
    context.treinamento_page.clicar_botao_click_me()

@then(u'o seu valor deverá mudar para "{texto_correto}"')
def step_then_verificar_texto_botao(context, texto_correto):
    texto_obtido = context.treinamento_page.recuperar_texto_botao_click_me()
    assert texto_obtido == texto_correto, f"O texto obtido '{texto_obtido}' foi diferente do texto esperado '{texto_correto}'"
# endregion

# region Teste Alert Sobrenome Obrigatório
@when(u'o valor "{valor}" for inserido no campo Nome')
def step_when_inserir_valor_campo_nome(context, valor):
    context.treinamento_page.preencher_campo_nome(valor)

@when(u'o cadastro for efetuado')
def step_when_efetuar_cadastro(context):
    context.treinamento_page.clicar_botao_cadastrar()

@then(u'um alert com a mensagem "{mensagem}" deverá aparecer na tela')
def step_then_verificar_alert(context, mensagem):
    texto_alert = context.treinamento_page.recuperar_texto_alert()
    assert texto_alert == mensagem, f"Mensagem de erro:\nO texto do alert '{texto_alert}'\nfoi diferente do esperado '{mensagem}'"
# endregion

# region Teste Cadastro Simples
@when(u'o valor "{valor}" for inserido no campo Sobrenome')
def step_when_inserir_valor_campo_sobrenome(context, valor):
    context.treinamento_page.preencher_campo_sobrenome(valor)

@when(u'a opção "{opcao}" for marcada no campo Sexo')
def step_when_marcar_opcao_sexo(context, opcao):
    context.treinamento_page.clicar_sexo(opcao)

@when(u'clicar no botão "Cadastrar"')
def step_when_efetuar_cadastro(context):
    context.treinamento_page.clicar_botao_cadastrar()

@then(u'A mensagem "{texto}" deverá aparecer na tela')
def step_then_verificar_mensagem_cadastro(context, texto):
    valor_obtido = context.treinamento_page.recuperar_texto_resultado()
    assert texto == valor_obtido, f"Mensagem de erro:\nO texto do resultado '{valor_obtido}'\nfoi diferente do esperado '{texto}'"

# endregion
