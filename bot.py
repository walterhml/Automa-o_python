import pyautogui

# entrar no google

pyautogui.press('win')
pyautogui.PAUSE = 4
pyautogui.write('chrome')
pyautogui.press('enter')

# posição do git - entrando no git e no meu perfil

pyautogui.click(x=1185, y=125) #clicando no link do GitHub
pyautogui.click(x=1857, y=187) # clicando na foto do perfil
pyautogui.click(x=1641, y=312) # clicando na opção "PERFIL"



#posição do linkdin
pyautogui.click(x=610, y=125) # clicando no link onde vai para o linkedin
pyautogui.click(x=379, y=393) # clicando na opçao do "perfil"




# import time

# time.sleep(5)
# x, y = pyautogui.position() 
# print(f'A posição atual do mouse é ({x}, {y})')