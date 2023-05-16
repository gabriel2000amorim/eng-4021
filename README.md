1- Gerar uma chave secreta (SECRET_KEY) usando os seguintes comandos:

    python
    Copy code
    import secrets
    secrets.token_urlsafe(32)


2- Iniciar um novo aplicativo (app) usando o comando a seguir:

    python
    Copy code
    python manage.py startapp nome_do_app


3- Configurar um superusuário (SuperUser) usando o seguinte comando:

    python
    Copy code
    python manage.py createsuperuser

Digite um nome de usuário e senha para configurá-lo.
