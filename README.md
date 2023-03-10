<div align="center" id="top"> 
  <img src="media/readme/logo.png" alt="Freelaway" />

<!-- &#xa0; -->

  <!-- <a href="https://freelaway.netlify.com">Demo</a> -->
</div>

<div align="center"> 
  <h1 align="center">Freelaway</h1>
  <!-- <img src="./public/pystack_week.png" alt="Freelaway" width=200 /> -->
</div>

<p align="center">
  <img alt="Principal linguagem do projeto" src="https://img.shields.io/github/languages/top/navegantes/freelaway?color=56BEB8" />

  <img alt="Quantidade de linguagens utilizadas" src="https://img.shields.io/github/languages/count/navegantes/freelaway?color=56BEB8" />

  <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/navegantes/freelaway?color=56BEB8" />

  <img alt="Licença" src="https://img.shields.io/github/license/navegantes/freelaway?color=56BEB8" />

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/navegantes/freelaway?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/navegantes/freelaway?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/navegantes/freelaway?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Freelaway 🚀 Em construção...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#sparkles-funcionalidades">Funcionalidades</a> &#xa0; | &#xa0;
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-pré-requisitos">Pré requisitos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-começando">Começando</a> &#xa0; | &#xa0;
  <a href="#memo-licença">Licença</a> &#xa0; | &#xa0;
  <a href="https://github.com/gustavonovais1" target="_blank">Autor</a>
</p>

<p align="center">
  <img alt="Login" src="media/readme/login.png" width=250>
  <img alt="cadastrar" src="media/readme/cadastrar.png" width=250>
  <img alt="Recuprerar senha" src="media/readme/recuperar_senha.png" width=250>
  <img alt="Encontrar job" src="media/readme/encontrar_jobs.png" width=250>
  <img alt="Job" src="media/readme/job.png" width=250>
  <img alt="Perfil" src="media/readme/perfil.png" width=250>
</p>

## 🎯 Sobre

A proposta é criar um sistema de ofertas de trabalhos para contratar profissionais freelancer.

## ✨ Funcionalidades

✔️ Login/Logout;\
✔️ Cadastro de usuários;\
✔️ Recuperação de senha;\
✔️ Histórico de trabalhos realizados;

## 🚀 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Bootstrap](https://getbootstrap.com/)


## ✅ Pré requisitos

Antes de começar 🏁, você precisa ter o [Python](https://www.python.org/downloads/) instalado em sua maquina.

## 🏁 Começando

1 - Primeiro clone o repositório e entre na pasta do projeto.

```bash
# Clone este repositório
$ git clone https://github.com/gustavonovais1/FreelaWay.git

# Entre na pasta
$ cd FreelaWay
```

2 - Segundo inicie um ambiente virtual

```bash
# Criar
  # Linux
    $ python3 -m venv venv
  # Windows
    $ python -m venv venv

#Ativar
  # Linux
    $ source venv/bin/activate
  # Windows
    $ venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

  $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3 - Instale as dependências

```bash
# Instale as dependências
# Linux
$ pip3 install -r requirements.txt
# Windows
$ pip install -r requirements.txt
```

4 - Faça as migrações.

```bash
# Linux
python3 manage.py migrate
# Windows
python manage.py migrate
```

5 - Crie um super usuário

```bash
$ python3 .\manage.py createsuperuser
$ python .\manage.py createsuperuser
```

6 - Inicie a aplicação

```bash
# Para iniciar o projeto
# Linux
$ python3 manage.py runserver
# Windows
$ python manage.py runserver

# O app vai inicializar em <http://127.0.0.1:8000/>

# Para iniciar o projeto em uma porta especifica
$ python manage.py runserver <porta>

# O app vai inicializar em <http://127.0.0.1:<porta>/>

```

## 📝 Licença

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Feito com ❤️ por <a href="https://github.com/gustavonovais1/FreelaWay" target="_blank">Gustavo Novais</a>

&#xa0;

<a href="#top">Voltar para o topo</a>
