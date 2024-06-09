import selenium,pyautogui,time

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://studio.youtube.com/channel/UCDnylffhsQ0Q1X8Vaf4PYqA/videos/upload?filter=%5B%5D&sort=%7B"columnType"%3A"date"%2C"sortOrder"%3A"DESCENDING"%7D')
pyautogui.press('enter')
time.sleep(3)
print(pyautogui.position())
# Point(x=86, y=226) posicao pasta youtube
