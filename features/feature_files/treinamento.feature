Funcionalidade: Treinamento de Automaçao

    @TesteSimples
    Cenário: Interagir com botões
        Dado que a página de treinamento seja acessada
        Quando o botao click me for clicado
        Então o seu valor deverá mudar para "Obrigado!!!!!!"

    @TesteSobrenome
    Cenário: Verificar que o não é possível cadastrar um registro sem sobrenome
        Dado que a página de treinamento seja acessada
        Quando o valor "David" for inserido no campo Nome
        E o cadastro for efetuado
        Então um alert com a mensagem "Sobrenome eh obrigatorio!" deverá aparecer na tela

    
    @CadastroSimples
    Cenário: Cadastro com dados mínimos
        Dado que a página de treinamento seja acessada
        Quando o valor "João" for inserido no campo Nome
        E o valor "Silva" for inserido no campo Sobrenome
        E a opção "Masculino" for marcada no campo Sexo 
        E clicar no botão "Cadastrar"
        Então a mensagem "Cadastrado!" deverá aparecer na tela


