import pyautogui as pag

# Check your screen width and height
screenWidth, screenHeight = pag.size()
print("screenWidth",screenWidth,"screenHeight",screenHeight)

### Line 
# Bottom right corner : currentMouseX 1896 currentMouseY 1015
# Click : currentMouseX 1393 currentMouseY 432
# This is for the desktop version of Line
pag.moveTo(1896, 1015) 
pag.click()
pag.moveTo(1003 , 334) 
# pag.click(clicks=1000, interval=0.1)
pag.click(clicks=10000, interval=0.05)


### Discord setting
# currentMouseX 1071 currentMouseY 764

pag.moveTo(1071, 764)
pag.click()
for i in range(100):
    a = 'This is {} time for testing.'.format(i)
    pag.typewrite(a)
    pag.press('enter')
    pag.PAUSE = 0.5