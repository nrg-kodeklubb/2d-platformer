from pysimpleGUI import *
import copy

def turnTo(GM, params):
    GM.currentLayout = params[0]

def getGUIs(WS):
    r = []
    #Wirite GUIs here
    layout = Layout()
    myRect = GUIRect((50, 50), (50, 50), BLUE)

    layout.addButton(Button(myRect, turnTo, params=[1]))

    r += [copy.deepcopy(layout)]

    layout = Layout()
    myRect = GUIRect((20, 20), (20, 20), RED)

    layout.addButton(Button(myRect, turnTo, params=[0]))

    r += [copy.deepcopy(layout)]

    [l.setSurface(WS) for l in r]
    return r
