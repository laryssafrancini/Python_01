#passo escrever passo a passo do projeto
#pyautogui é um pacote de automação
#passo 1: Entrar no sistema da empresa 
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui (uma biblioteca que permite pegar posição ou usar mouse,teclado ou computador)
import pyautogui
import time

pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar em algum lugar
#pyautogui.write -> escrever em tal lugar (escrever texto)
#pyautogui.press -> quero apertar 1 tecla do meu teclado

#Próxima tarefa abrir o navegador (chrome)
#pyautogui.hotkey("","")
pyautogui.press("win")
pyautogui.press("Microsoft Edge")
pyautogui.click(x=375, y=850)
#pyautogui.write("Microsoft Edge")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(2)

#passo 2: fazer login
pyautogui.click(x=783, y=361)
pyautogui.write("franlys@gmail.com")

#escrever a senha 
pyautogui.press("tab")
pyautogui.write("12356")

#clicar no botão de logar
pyautogui.click(x=905, y=521)
time.sleep(3)

#passo 3: importar a base de dados (pandas) é uma ferramenta que trabalha com base de dados
#para instalar: pip install pandas numpy openpyxl 
#read (significa ler) pode ler um arquivo em pdf,xl,csv,html,exel etc
import pandas 
tabela = pandas.read_csv("produtos.csv")

print(tabela)


#passo 4: cadastrar 1 produto 
#para cada linha dentro da minha tabela (panda chama a numeração da tebela de index)
for linha in tabela.index:
    # clicar no 1º campo
    pyautogui.click(x=740, y=241)
    # digitar o código do produto 
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca do produto
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # categoria
    # str() string -> texto
    # str(1) -> 1 -> "1"
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    # botao enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)





#passo 5: repetir o processo de cadastro de produto até acabar a base de dados


#construir em python cada etapa


