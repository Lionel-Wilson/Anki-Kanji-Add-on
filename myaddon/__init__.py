# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
#import anki module
from anki import *

def Menu_setup():
    #Create a sub-menu item
    Kanji_unlocker_menu = QMenu("Kanji Unlocker",mw)
    #put sub-menu in Anki "Tool" menu.
    mw.form.menuTools.addMenu(Kanji_unlocker_menu)

    #create buttons that will carry out actions
    Kanji_unlocker_option = QAction("Select Main Kanji Deck",mw)
    Kanji_unlocker_menu.addAction(Kanji_unlocker_option)

    Kanji_unlocker_option = QAction("Select Vocab/Sentence Decks",mw)
    Kanji_unlocker_menu.addAction(Kanji_unlocker_option)

    Kanji_unlocker_option = QAction("Select Fields to be Parsed",mw)
    Kanji_unlocker_menu.addAction(Kanji_unlocker_option)

    Kanji_unlocker_option = QAction("Suspend All Kanji",mw)
    Kanji_unlocker_menu.addAction(Kanji_unlocker_option)

def Mark_known_kanji():
    MarkKnownDialog.show_modal(parent=aqt.mw)

Menu_setup()


