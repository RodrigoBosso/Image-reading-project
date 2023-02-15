from pytesseract import pytesseract
import cv2
from os import listdir, path
import time

#Traz o caminho do Pytesseract que necessita do caminho 
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#Traz o caminho do diretorio atual
path = path.dirname(path.realpath(__file__)) + "\Imagenseng"

#Armazena o nome dos arquivos numa lista
files = [f for f in listdir(path)]

#o Instanciando a Variavel Tesseract
pytesseract.tesseract_cmd = caminho_tesseract


var = 1 #auxiliar para abrir os arquivos
for file in files: # For que vai percorrer os Arquivos da pasta
  img = cv2.imread(f'Imagenseng/{file}') #img recebe cada arquivo por vez da pasta
  #Texto da imagem é lido Em portugues e enviado para a váriavel Texto
  tx = open("resulteng/img"+str(var)+".txt","w") # abrindo um txt para receber os resultados das imagens
  texto = pytesseract.image_to_string(img, lang="eng" )
  linhas = texto.split("\n")#Se divide a variavel Texto em Variaveis Linhas a cada quebra de linha
  for linha in linhas: # for que percorre cada linha no texto fornecido
     if not linha.isspace() and len (linha) > 0: # enquanto a linha não for nula
         tx.write(linha+"\n") # escreve a linha no txt correspondente
        
  var = var+1 # Var de escrita de arquivo aumenta em um para escrever o próximo arquivo de texto
  tx.close()



#-----------------------------------------------

import pyautogui

import os
from os import listdir, path


#Traz o caminho do diretorio atual
path = path.dirname(path.realpath(__file__)) + "\\resulteng"

#Armazena o nome dos arquivos numa lista
files = [f for f in listdir(path)]

    
pyautogui.PAUSE= 1
var=1
#aviso do controle
pyautogui.alert("O código vai tomar conta do seu pc por um tempo , por favor não toque em nada")
   
#abrir o menu do windows
pyautogui.press('winleft')
#abrir o Balabolka
pyautogui.write('balabolka.exe')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)
#ajustar para Portugues
pyautogui.moveTo(1075,151)
pyautogui.click()
pyautogui.moveTo(1200,190)
pyautogui.click()

# Repitir Enquanto tiver um arquivo existir
for file in files: # For que vai percorrer os Arquivos da pasta
    #abrir o arquivo
    time.sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('o')
    pyautogui.keyUp('ctrl')
    
    time.sleep(1)
    pyautogui.write(str(os.path.dirname(os.path.abspath(__file__)))+"\\resulteng\\")
    #escrever o caminho do arquivo de origem
    pyautogui.press('enter')
    #       Digite o nome do arquivo img(var).txt
    pyautogui.write("img"+str(var)+".txt")
    pyautogui.press('enter')

    #converter para mp3 e escrever o caminho do resultado
    pyautogui.keyDown('alt')
    pyautogui.press('s')
    pyautogui.keyUp('alt')

    pyautogui.write(str(os.path.dirname(os.path.abspath(__file__))+"\\AudioEng\\"))
    pyautogui.press('enter')
    pyautogui.write("img"+str(var)+".mp3")
    pyautogui.press('enter')
    #tempo de conversã
    #Liberar o computador do Py Auto Gui
    var=var+1
    
pyautogui.alert("O Computador já está liberado para uso, verifica a pasta de Audio para retirar os audios convertidos")



