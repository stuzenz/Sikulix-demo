# Demo script to show how you can use 

def openBrowser():
    """
    Simple script to open the browser
    """

def clearBrowserCache():
    """
    For testing we are best to clear the cache before doing our first test
    Possibly we don't care if it is not a performance or login related test
    I don't want to clear my main browser cache, so will do this from midori browser
    """

def hello():
    popup("Example scenario for Penny and Mick for using Sikulix")

def newAddress():
    find("1633079190945.png")
    click("1633079190945.png")
    type("1633080775389.png","mpi.govt.nz"+Key.ENTER)
    wait(2)
    
def newTab():
       click("1633079190945.png")


    

def muckingAround():
    find("1633079190945.png")
    hover("1633079190945.png")
    mouseDown()
    wait(0.3)
    hover("1633080775389.png")
    wait(0.3)
    mouseUp()

hello()
hello()
newAddress()
newTab()