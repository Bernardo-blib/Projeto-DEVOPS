# Projeto DevOps — Sistema de Estoque

## 1. Sobre o projeto

Este projeto foi desenvolvido para a disciplina de DevOps.

O objetivo é criar um sistema simples de controle de estoque em Python e utilizar ferramentas de DevOps para automatizar testes e organizar o desenvolvimento.

## 2. Funcionalidades

O sistema permite:

- Cadastrar produtos.
- Listar produtos cadastrados.
- Calcular o valor total do estoque.
- Remover produtos pelo nome.
- Encerrar o programa.

## 3. Tecnologias utilizadas

- Python — linguagem de programação.
- Git — controle de versões.
- GitHub — armazenamento do código.
- Gitflow — organização das branches.
- GitHub Actions — automação dos testes.
- Unittest — testes automatizados do Python.
- Visual Studio Code — editor de código.

## 4. Organização do projeto

O projeto possui os seguintes arquivos:

- `main.py` — código principal do sistema de estoque.
- `test_main.py` — testes automatizados.
- `.github/workflows/python-tests.yml` — configuração da pipeline.
- `README.md` — documentação do projeto.

## 5. Gitflow

Foi utilizado o Gitflow para organizar o desenvolvimento.

As branches utilizadas foram:

- `main` — versão principal do projeto.
- `develop` — branch de integração das funcionalidades.
- `feature/remover-produto` — desenvolvimento da funcionalidade de remover produtos.

O fluxo realizado foi:

`feature/remover-produto` → `develop` → `main`

As alterações foram integradas por meio de Pull Requests no GitHub.

## 6. Comandos Git utilizados

```bash
git status
git checkout -b develop
git push -u origin develop
git checkout -b feature/remover-produto
git add main.py
git commit -m "Adiciona funcionalidade de remover produto"
git push -u origin feature/remover-produto
git checkout develop
git pull origin develop
git checkout main
git pull origin main
```

## 7. Pipeline de integração contínua

Foi configurada uma pipeline utilizando GitHub Actions.

A pipeline executa automaticamente os testes Python quando são realizados pushes ou Pull Requests nas branches `main` e `develop`.

O objetivo é verificar se os testes passam antes da integração das alterações.

## 8. Testes automatizados

Os testes foram desenvolvidos utilizando a biblioteca `unittest`.

Para executar os testes, utilize:

```bash
python -m unittest -v
```

Foram criados três testes automatizados:

1. Verificar se a lista de produtos começa vazia.
2. Verificar o cálculo do valor de um produto no estoque.
3. Verificar o cálculo do valor de vários produtos.

Os três testes foram executados com sucesso.

## 9. Como executar o sistema

No terminal, execute:

```bash
python main.py
```

O programa exibirá um menu para cadastrar, listar, remover produtos e calcular o valor do estoque.

## 10. Conclusão

O projeto permitiu praticar conceitos de DevOps, incluindo controle de versões, Gitflow, Pull Requests, integração contínua e testes automatizados.

A utilização do GitHub Actions possibilitou automatizar a execução dos testes durante o desenvolvimento.