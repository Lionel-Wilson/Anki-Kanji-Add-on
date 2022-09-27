# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
#import anki module
from anki import *

def Menu_setup():
    #Create the button on the top left of anki. mw = main window(of anki)
    Kanji_unlocker_menu = QMenu("Kanji Unlocker", aqt.mw)

    #create buttons that will carry out actions
    settings_action = QAction("Settings", aqt.mw)
    Kanji_unlocker_menu.addAction(settings_action)


def Mark_known_kanji():
    pass
    #MarkKnownDialog.show_modal(parent=aqt.mw)

Menu_setup()


