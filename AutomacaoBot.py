import pyautogui
import time
import pandas 

tabela = pandas.read_csv("produtos.csv")

#Passo a passo
#1- abrir o google
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=723, y=611)

#Digitar o site da automação
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#No site, preencher o login e senha
time.sleep(5)
pyautogui.click(x=788, y=368)
pyautogui.write("teste.automacao@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha321")
pyautogui.press("tab")
pyautogui.press("enter")

#Preenchimento dos dados do produto
for linha in tabela.index:
    pyautogui.click(x=703, y=256)
    pyautogui.write (str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "categoria"]))   
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
            pyautogui.write (str(obs))
    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")