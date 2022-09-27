# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardcount = mw.col.cardcount()
    # show a message box
    # % to specify where in a string you want to insert a certain data type.
    #%d specifies that you want to insert an interger data type. after the string, you must follow with %
    #and the value you want to insert. in this case cardcount. can also be used with print function.
    showInfo("Card count: %d" % cardcount)


# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)