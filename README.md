
# bbbot-macro
## Instalações necessárias
### Instale o Chromedriver
https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_win32.zip
#
### Instale o Selenium
Abra o CMD e digite python -m pip install -U selenium
### Executando
Com o bbbot2.py e o chromedriver.exe na mesma pasta faça o seguinte:
  
1º Clique com o Shit+Botão direito do mouse no chromedriver e clique em "Copiar como caminho"

2º Clique para editar o arquivo bbbot2.py

3º Vá em "chrome_path" e apartir das aspas, apague o endereço e cole o endereço que copiou no 1º passo, ele irá ficar assim:
Exemplo: chrome_path = r"C:\Users\usuario\Desktop\pasta\chromedriver.exe"

4º Vá em "login_globo" e "senha_globo" e coloque seu email e senha para efetuar o login no site

5º Após isso, é só salvar a edição, executar o bbbot2.py e ser feliz ;)
