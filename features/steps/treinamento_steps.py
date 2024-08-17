from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from features.pages.treinamento_page import TreinamentoPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Region Teste Login Válido
@given(u'que o usuário está na página de login')
def step_given_o_usuario_esta_na_pagina_de_login(context):
    context.driver.get("https://www.saucedemo.com")
    context.treinamento_page = TreinamentoPage(context.driver)

@given(u'o usuário insere um nome de usuário e senha válidos')
@when(u'o usuário insere um nome de usuário e senha válidos')
def step_when_o_usuario_inserir_credenciais_validas(context):
    context.treinamento_page.preencher_campo_usuario('standard_user')
    context.treinamento_page.preencher_campo_senha('secret_sauce')
    
@given(u'o usuário clica no botão de login')
@when(u'o usuário clica no botão de login')
def step_when_o_usuario_clica_no_botao_login(context):
    context.treinamento_page.clicar_botao_login()

@given(u'o usuário deve ser redirecionado para a página principal')
@then(u'o usuário deve ser redirecionado para a página principal')
def step_then_o_usuario_deve_estar_na_pagina_principal(context):
   WebDriverWait(context.driver, 5).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    ) 
#endregion


# Region Teste Finalizar Pedido com Sucesso
@when(u'o usuário está na página inicial do e-commerce')
@given(u'o usuário está na página inicial do e-commerce')
def step_when_pagina_home(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )

@given(u'o usuário adiciona um item ao carrinho de compras clicando no botão "Add to Cart"')
def step_when_adicionar_item_ao_carrinho(context):
   context.treinamento_page.clicar_botao_add_to_cart_bag()

@given(u'o usuário visualiza o carrinho de compras')
def step_when_visualizar_carrinho(context):
    context.treinamento_page.clicar_carrinho_compras()

@when(u'o usuário clica no botão "Checkout"')
def step_when_clicar_checkout(context):
    context.treinamento_page.clicar_botao_checkout()

@when(u'preenche os campos "First Name", "Last Name" e "Zip/Postal Code" com informações válidas')
def step_when_preencher_dados_entrega(context):
    context.treinamento_page.preencher_campo_first_name('John')
    context.treinamento_page.preencher_campo_last_name('Smith')
    context.treinamento_page.preencher_campo_postal_code('12345678')

@when(u'clica no botão "Continue"')
def step_when_clicar_continue(context):
    context.treinamento_page.clicar_botao_continue()

@then(u'o usuário clica no botão "Finish" e deve visualizar uma mensagem de confirmação de pedido e o botão "Back Home"')
def step_then_clicar_finish(context):
    context.treinamento_page.clicar_botao_finish()    
#endregion

# Region Test adicionar item ao carrinho
@when(u'o usuário seleciona o item mochila, chamado "Sauce Labs Backpack"')
def step_when_clicar_imagem_blackpacK(context):
    context.treinamento_page.clicar_imagem_blackpacK()

@when(u'clica no botão "Add to Cart"')
def step_when_clicar_botao_add_to_cart(context):
    context.treinamento_page.clicar_botao_add_to_cart()

@then(u'o usuário adiciona o item selecionado ao carrinho e o item deve aparecer no carrinho de compras')
def step_then_vizualizar_item_carrinho(context):
    context.treinamento_page.ICONE_CARRINHO()
#endregion

#Region Teste Menu Hamburguer
@when(u'o usuário clica no botão do menu hambúrguer para visualizar as opções oferecidas')
def step_when_clicar_botao_menu(context):
    context.treinamento_page.clicar_botao_menu()
    
@then(u'é informado as opções: All Items, About, Logout e Reset App State para o usuário')
def step_when_mostrar_informacoes(context):
    ...
#endregion



# Region Teste Gerenciamento de Carrinho
@when(u'o usuário adicionar os produtos "Camiseta Sauce Labs Bolt" e "Macacão Sauce Labs" ao carrinho')
def step_when_adicionar_camiseta_e_macaca_ao_carrinho(context):
    context.treinamento_page.clicar_botao_adicionar_bolt_tshirt()
    context.treinamento_page.clicar_botao_adicionar_macacao()
    context.treinamento_page.clicar_botao_add_to_cart()

@when(u'ao remover o produto "Camiseta Sauce Labs Bolt" do carrinho')
def step_when_remover_camiseta_do_carrinho(context):
    context.treinamento_page.clicar_botao_remover_bolt_tshirt()
    
@then(u'Então o carrinho deverá ter apenas o item "Macacão Sauce Labs" no carrinho')
def step_when_mostrar_carrinho_com_um_item(context):
    ...
#endregion


# Region Teste Navegação para a Página Principal
@when(u'o usuário clica no item "Jaqueta de lã Sauce Labs"')
def step_when_adicionar_camiseta_e_macaca_ao_carrinho(context):
    context.treinamento_page.clicar_botao_adicionar_macacao()

@when(u'o usuário deve estar na página de detalhes do item')
def step_when_ver_detalhes_do_item(context):
    context.treinamento_page.clicar_botao_add_to_cart()

@when(u'o usuário clica no botão "Continuar Comprando"')
def step_when_clicar_botao_continuar_comprando(context):
    context.treinamento_page.clicar_botao_continuar_comprando()
    
@then(u'o usuário deve ser redirecionado de volta à página principal e visualizará os produtos disponíveis')
def step_when_mostrar_página_home(context):
    ...
#endregion
