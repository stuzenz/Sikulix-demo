# Demo script to show how you can use 



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
    type("https://www.arcgis.com/home/webmap/viewer.html?webmap=286415a3edcd43f89fa266edc0c89b08"+Key.ENTER)
    wait(8)
    


def enterPhysicalAddress():
    type("1633224473540.png","1 The Terrace, Wellington" + Key.ENTER)
    wait(8)

def measure():
    click("1633231670826.png")
    wait(0.2)
    click("1633231894570.png")
    wait(0.2)
    click("1633236202678.png")

def area():
    click("1633231741073.png")
# hello()
# fullScreen()
newTab()
openDevTools()
persistLogs()
startPerformance()
urlFocus()
openArcGISDemo()
enterPhysicalAddress()
measure()

# startPerformanceAnalysis()
wait(5)

# measure()

# area()


