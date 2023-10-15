# Demo script to show how you can use sikulix

import random

input_list = [
    "Liquid Laundromat Te Aro website in Te Aro, Wellington",
    "Agitator Laundrette website in Mount Victoria, Wellington",
    "Liquid Laundromats Newtown website in Berhampore, Wellington",
    "Tunnel 24 Hour Laundrette website in Hataitai, Wellington",
    "Janice Laundry - Newtown website in Newtown, Wellington",
    "Laundromat website in Newtown, Wellington",
    "Liquid Laundromats Kilbirnie website in Kilbirnie, Wellington",
    "Newtown Laundry and Dryclean website in Newtown, Wellington",
    "Spinfresh Laundromat KARORI website in Karori, Wellington",
    "Liquid Laundromats Newlands website in Newlands, Wellington",
    "Liquid Laundromats Johnsonville website in Johnsonville, Wellington",
    "Laundry Drop website in Johnsonville, Wellington",
    "Q Laundromat website in Tawa, Wellington",
    "Janice Laundry - Tawa website in Tawa, Wellington",
    "Liquid Laundromat Porirua CBD website in CBD, Wellington",
    "Spinfresh Laundromat EPUNI website in Epuni, Wellington",
    "Liquid Laundromat Moera website in Moera, Wellington",
    "Laundromat - Easy Key Self Service Laundromats (Wainuiomata) website in Wainuiomata, Wellington",
    "Besties Drycleaning And Laundry Services website in Paparangi, Wellington",
    "Liquid Laundromats Waterloo website in Waterloo, Wellington",
    "The Hub Laundromat website in Wainuiomata, Wellington",
    "Liquid Laundromat Wainuiomata website in Wainuiomata, Wellington",
    "Crystal Laundromat Lower Hutt website in Central, Wellington",
    "Wellington Laundry Services website in Gracefield, Wellington",
    "Janice Laundry - Newlands website in Newlands, Wellington",
    "Lavendera Laundromat website in Boulcott, Wellington",
    "Petone Clock Tower Laundromat website in Petone, Wellington",
    "Petone Self Service Laundromat website in Petone, Wellington",
    "Liquid Laundromats Lower Hutt website in Hutt Central, Wellington",
    "Liquid Laundromats Cannons Creek website in Cannons Creek, Porirua",
    "Executive Commercial Laundry website in Petone, Wellington",
    "Kokiri Laundrette website in Wainuiomata, Wellington",
    "🧺Hub Laundromat Taita website in Taitā, Wellington",
    "Liquid Laundromat Taita website in Taitā, Wellington",
    "Siv's Laundry Services website in Naenae, Wellington",
    "Waitangirua Laundromat website in Waitangirua, Porirua",
    "Laundromat website in Wainuiomata, Wellington",
    "Liquid Laundromats Stokes Valley website in Stokes Valley, Wellington",
    "Takapuwahia Laundromat website in Elsdon, Porirua",
    "Porirua Coin Laundromat website in Porirua",
    "Mungavin Laundromat website in Rānui, Porirua",
    "Liquid Laundromat Upper Hutt CBD website in Upper Hutt Central, Upper Hutt",
    "Liquid Laundromats Fergusson Drive website in Trentham, Upper Hutt",
    "Fergusson Laundromat website in Clouston Park, Upper Hutt",
    "Dolly Wash Laundry website in Trentham, Upper Hutt"
        ]

def hello():
    popup("To get laundromat pricing data")


def openBrowser():
    switchApp("Mozilla Firefox")
    wait(0.2)

def enterRequest(input_item):

    click("1697073313699.png")
    type("can you get prices for {} and please provide the results in json format. Can you please start the first node of the json as the website url").format(input_item)
    type(Key.ENTER)
    wait(60)

def fullScreen():
    type(Key.F11)
    wait(0.3)
def clearBrowserCache():
    """
    For testing we are best to clear the cache before doing our first test
    Possibly we do not care if it is not a performance or login related test
    I do not want to clear my main browser cache, so will do this from midori browser
    """


def newTab():
       keyDown(Key.CTRL+"t")
       keyUp()
       wait(0.1)
       type(Key.BACKSPACE)

def openDevTools():
    keyDown(Key.CTRL + Key.SHIFT+"I")
    keyUp()  
    wait(0.5)
def startPerformance():
   click( "1633237283966.png")
   wait(0.1)
   click("1633237353763.png")
   wait(0.2)
   click("1633237385961.png")

def persistLogs():
    click("1633236015299.png")
    wait(0.1)
    click("1633236718858.png")
    
    
def startPerformanceAnalysis():
    click("1633231374776.png")
    
def urlFocus():
    keyDown(Key.ALT+"d")

    keyUp()
    wait(0.2)    
#    type(Key.BACKSPACE)
#    wait(0.3)

def openArcGISDemo():
#    keyDown(Key.ALT+"d")
#    keyUp()
#    wait(1)  
    paste("https://www.arcgis.com/home/webmap/viewer.html?webmap=286415a3edcd43f89fa266edc0c89b08")
    type(Key.ENTER)
    wait(5)
    
def closeDevTools():
    click("1633242446999.png")

def enterPhysicalAddress():
    type("1633224473540.png","1 The Terrace, Wellington" + Key.ENTER)
    wait(3)

def measure():
    click("1633231670826.png")
    wait(0.2)
    click("1633231894570.png")
    wait(0.2)
    click("1633236202678.png")

def measureArea():

    coord_list = []
    coord_list.append(Location(777, 619))
    coord_list.append(Location(832, 626))
    coord_list.append(Location(838, 621))
    coord_list.append(Location(870, 620))
    coord_list.append(Location(872, 632))
    coord_list.append(Location(879, 636))
    coord_list.append(Location(965, 704))
    coord_list.append(Location(930, 749))
    coord_list.append(Location(995, 838))
    coord_list.append(Location(809, 978))
    coord_list.append(Location(690, 962))
    coord_list.append(Location(692, 938))
    coord_list.append(Location(685, 928))
    coord_list.append(Location(712, 741))
    coord_list.append(Location(721, 746))
    coord_list.append(Location(729, 716))
    coord_list.append(Location(763, 720))
    final = Location(781, 622)

    for value in coord_list:
        click(value)
        wait(0.2)
    doubleClick(final)
          
def seeyoulater():
    popup("Get in touch if you have questions")

 
# hello()
openBrowser()

for value in input_list:
    enterRequest(value)
# fullScreen()
# newTab()
# openDevTools()
# persistLogs()
#startPerformance()
# urlFocus()
# openArcGISDemo()
# enterPhysicalAddress()
# measure()
# closeDevTools()
wait(1)
# measureArea()
# wait(0.5)
# openDevTools
# seeyoulater()

# startPerformanceAnalysis()

# wait(10)



# measure()

# area()


