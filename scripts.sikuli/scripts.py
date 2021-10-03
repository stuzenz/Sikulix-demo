# Demo script to show how you can use sikulix


def openBrowser():
    switchApp("Mozilla Firefox")
    wait(0.2)
    
def fullScreen():
    type(Key.F11)
    wait(0.3)
def clearBrowserCache():
    """
    For testing we are best to clear the cache before doing our first test
    Possibly we do not care if it is not a performance or login related test
    I do not want to clear my main browser cache, so will do this from midori browser
    """

def hello():
    popup("Example scenario for Penny and Mick for using Sikulix")

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

 
hello()
fullScreen()
openBrowser()
newTab()
openDevTools()
persistLogs()
#startPerformance()
urlFocus()
openArcGISDemo()
enterPhysicalAddress()
measure()
# closeDevTools()
wait(1)
measureArea()
wait(0.5)
# openDevTools
seeyoulater()

# startPerformanceAnalysis()

wait(10)



# measure()

# area()


