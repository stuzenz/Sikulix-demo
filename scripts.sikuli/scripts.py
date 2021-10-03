# Demo script to show how you can use 

def openBrowser():
    """
    Simple script to open the browser
    """
    type(Key.CTRL+"t")
    wait(2)

def clearBrowserCache():
    """
    For testing we are best to clear the cache before doing our first test
    Possibly we do not care if it is not a performance or login related test
    I do not want to clear my main browser cache, so will do this from midori browser
    """

def hello():
    popup("Example scenario for Penny and Mick for using Sikulix")

def openDevTools():
    type(Key.CTRL + Key.SHIFT+"I")
    wait(0.5)
    
def openArcGISDemo():
    type(Key.CTRL+"t")
    wait(1)
    type("1633223686315.png","https://www.arcgis.com/home/webmap/viewer.html?webmap=286415a3edcd43f89fa266edc0c89b08"+Key.ENTER)
    wait(3)
    
def newTab():
       type(Key.CTRL,"t")
       wait(0.5)

def enterPhysicalAddress():
    type("1633224473540.png","1 The Terrace, Wellington" + Key.ENTER)
    wait(1)

# hello()
# newTab()
# openDevTools()
openArcGISDemo()
enterPhysicalAddress()

