import pyautogui
from time import sleep
# Passo a passo da automação em um software simples de cadastro:
# Clicar e digitar meu usuario
pyautogui.click(1295, 542, duration=2)
pyautogui.write('philipe')
# Clicar e digitar minha senha
pyautogui.click(1296, 568, duration=2)
pyautogui.write('123456')
# Clicar em "Entrar"
pyautogui.click(1190, 595, duration=2)
# Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
    # clicar e digitar produto
    pyautogui.click(1047, 530, duration=2)
    pyautogui.write(produto)
    # clicar e digitar quantidade
    pyautogui.click(1042, 554, duration=2)
    pyautogui.write(quantidade)
    # clicar e digitar preço
    pyautogui.click(1034, 580, duration=2)
    pyautogui.write(preco)
    # clicar em registrar
    pyautogui.click(907, 734, duration=1)
    sleep(1)
