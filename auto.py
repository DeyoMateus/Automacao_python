# Automação de cadastro 

#Importando recursos
import pyautogui as pt
import pandas as pd
import time

#Modelagem de passos, login
pt.PAUSE=(1.5)
pt.press("win")
pt.write("chrome")
pt.press("enter")
pt.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pt.press("enter")
pt.press("tab")
pt.write("mhenriteus@gmail.com")
pt.press("tab")
pt.press("enter")
pt.write("senha")
pt.press("enter")

#Modelagem de passos, cadastro
tabela = pd.read_csv("Cópia de produtos.csv")
time.sleep(1)
# Repetição
for linha in tabela.index:
    pt.click(x=568, y=292)
    codigo = tabela.loc[linha, "codigo"]
    pt.write(str(codigo))
    pt.press("tab")

    marca = tabela.loc[linha, "marca"]
    pt.write(str(marca))
    pt.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pt.write(str(tipo))
    pt.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pt.write(str(categoria))
    pt.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pt.write(str(preco_unitario))
    pt.press("tab")

    custo = tabela.loc[linha, "custo"]
    pt.write(str(custo))
    pt.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pt.write(str(tabela.loc[linha, "obs"]))
    pt.press("tab")
    pt.press("enter")
    pt.scroll(2500)
    pt.click(x=493, y=290)

