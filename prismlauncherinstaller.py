print('Prism Launcher Installer (Version 1.0.0) von PaperTarsier692')
print('Starte das Program . . .')
print('Importiere Libraries . . .')

import keyboard
import pyautogui
import pygetwindow
import time

print('Pakete importiert')

print('\r\n\r\n______                   _____              _           \r\n| ___ \\                 |_   _|           '
      ' (_)          \r\n| |_/ /_ _ _ __   ___ _ __| | __ _ _ __ ___ _  ___ _ __ \r\n|  __/ _` | \'_ \\ / _ \\ \'__| '
      '|/ _` | \'__/ __| |/ _ \\ \'__|\r\n| | | (_| | |_) |  __/ |  | | (_| | |  \\__ \\ |  __/ |   \r\n\\_|  \\__,'
      '_| .__/ \\___|_|  \\_/\\__,_|_|  |___/_|\\___|_|   \r\n          | |                                           '
      '\r\n          |_|                                           \r\n\r\n')
time.sleep(3)

def update(version):
      url = "https://example.com/meine-datei.txt"
      path = "pfad/zum/speicherort/meine-datei.txt"

      response = requests.get(url)
      if response.status_code == 200:
            with open(speicherort, 'wb') as file:
                  file.write(response.content)
                  print("Datei erfolgreich heruntergeladen!")
      else:
            print("Fehler beim Herunterladen der Datei:", response.status_code)
