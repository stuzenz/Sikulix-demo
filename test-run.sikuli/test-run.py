running = True
def runHotkey(event):
    global running
    running = False
Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

input_list = [
    "Liquid Laundromat Te Aro website in Te Aro, Wellington",
    "Agitator Laundrette website in Mount Victoria, Wellington",
    "Liquid Laundromats Newtown website in Berhampore, Wellington",
    "Tunnel 24 Hour Laundrette website in Hataitai, Wellington",
    "Janice Laundry - Newtown website in Newtown, Wellington",

for value in input_list:
    import random
    x_ran = random.randrange(-30,40)
    y_ran = random.randrange(-10,10)   
    
                
while exists(Pattern("1495843225731.png").similar(0.10)) and running:
    import random
    x_ran = random.randrange(-30,40)
    y_ran = random.randrange(-10,10)



if exists(Pattern("1541289046943.png").similar(0.71)):
    doubleClick(Pattern("1541289689152.png").similar(0.90).targetOffset(-39,3))
    wait(1)
    type(str(num))        
    type(Key.ENTER)
    wait(1)

else:
    wait(1)
    click(Pattern("1541289841740.png").similar(0.82))
    wait(1)
    type("1.wav")
    type(Key.ENTER)