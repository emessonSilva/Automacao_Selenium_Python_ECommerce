Funcionalidade: Treinamento de Automaçao

    @TesteLoginVálido
    Cenário: Login com credenciais válidas
      Dado que o usuário está na página de login
      Quando o usuário insere um nome de usuário e senha válidos
      E o usuário clica no botão de login
      Então o usuário deve ser redirecionado para a página principal
 
    @TesteFinalizarPedido
    Cenario: Teste Finalizar Pedido com Sucesso
      Dado que o usuário está na página de login
      E o usuário insere um nome de usuário e senha válidos
      E o usuário clica no botão de login
      E o usuário está na página inicial do e-commerce
      E o usuário adiciona um item ao carrinho de compras clicando no botão "Add to Cart"
      E o usuário visualiza o carrinho de compras
      Quando o usuário clica no botão "Checkout"
      E preenche os campos "First Name", "Last Name" e "Zip/Postal Code" com informações válidas
      E clica no botão "Continue"
      Então o usuário clica no botão "Finish" e deve visualizar uma mensagem de confirmação de pedido e o botão "Back Home"
        
    
    @CarrinhoDeCompras
    Cenário: Adicionar um item ao carrinho de compras
      Dado que o usuário está na página de login
      E o usuário insere um nome de usuário e senha válidos
      E o usuário clica no botão de login
      E o usuário deve ser redirecionado para a página principal
      Quando o usuário seleciona o item mochila, chamado "Sauce Labs Backpack"
      E clica no botão "Add to cart"
      Então o usuário adiciona o item selecionado ao carrinho e o item deve aparecer no carrinho de compras

   @MenuHamburguer
   Cenário: Clicar no Menu Hambúrguer
      Dado que o usuário está na página de login
      E o usuário insere um nome de usuário e senha válidos
      E o usuário clica no botão de login
      E o usuário deve ser redirecionado para a página principal
      Quando o usuário clica no botão do menu hambúrguer para visualizar as opções oferecidas
      Então é informado as opções: All Items, About, Logout e Reset App State para o usuário
  

  @GerenciamentoCarrinho
  Cenário: Adicionar dois produtos ao carrinho e retirar um
    Dado que o usuário está na página de login
    E o usuário insere um nome de usuário e senha válidos
    E o usuário clica no botão de login
    E o usuário deve ser redirecionado para a página principal
    Quando o usuário adicionar os produtos "Camiseta Sauce Labs Bolt" e "Macacão Sauce Labs" ao carrinho
    E ao remover o produto "Camiseta Sauce Labs Bolt" do carrinho
    Então o carrinho deverá ter apenas o item "Macacão Sauce Labs" no carrinho
     
  @NavegaçãoPáginaPrincipal
  Cenário: Navegação na página
    Dado que o usuário está na página de login
    E o usuário insere um nome de usuário e senha válidos
    E o usuário clica no botão de login
    E o usuário deve ser redirecionado para a página principal
    Quando o usuário clica no item "Jaqueta de lã Sauce Labs"
    E o usuário deve estar na página de detalhes do item
    E o usuário clica no botão "Continuar Comprando"
    Então o usuário deve ser redirecionado de volta à página principal e visualizará os produtos disponíveis


