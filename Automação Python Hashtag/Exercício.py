import pyautogui as pa
import time

time.sleep(3)

pa.press('win')
pa.PAUSE = 2
pa.write('Chrome')
pa.PAUSE = 2
pa.press('ENTER')
pa.PAUSE = 2
pa.click(x=531, y=55)
pa.PAUSE = 2
pa.write('https://www.hashtagtreinamentos.com/?origemurl=75502579145&gad_source=1&gclid=Cj0KCQjwgJyyBhCGARIsAK8LVLMDG-0G1pcxTJzrvgBHg0LdlijxwgcfgxsSG0m0eKLDwQnwWpK-6JoaAsxOEALw_wcB')
pa.press('ENTER')
pa.PAUSE = 4
pa.click(x=791, y=121)
pa.PAUSE = 2
pa.scroll(-220)
pa.PAUSE = 2
pa.click(x=307, y=670)
pa.PAUSE=2
pa.write('Saint')
pa.PAUSE = 2
pa.press('tab')
pa.PAUSE = 2
pa.write('saintalmeida88@gmail.com')
pa.PAUSE = 2
pa.press('tab')
pa.PAUSE = 2
pa.write('92995367385')
pa.PAUSE = 2
pa.press('tab')