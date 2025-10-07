# Aula 05
- API
- Git (GitHub com Visual Studio Code)

# Api 

[API Awesome](https://docs.awesomeapi.com.br/)

[API Dolar](https://economia.awesomeapi.com.br/json/last/USD-BRL)




# Dicas para trabalhar com Git

- Verificar instalação do GIT

```Bash
git --version
```

- Caso não tenha, baixar e instalar (se não for administrador da máquina, baixa a versão portable)
[Instalar Git](https://git-scm.com/downloads)

- Via Power Shell
```Power Shell
winget install --id Git.Git -e --source winget
```

- Configurar conta

```Power Shell
git config --global user.name "Seu Nome Completo"
git config --global user.email "seuemail@provedor.com"
```

# testando mudanças na branch teste e main

## Fazer um merge entre duas branches

    Branch main - principal
    Branch teste - criado para fazer o merge

- Verificar em qual branch está
    - git status

- Ir para a branch de destino

    - git checkout main

- Fazer o merge buscando a branch que possuí a alteração

    git merge teste

