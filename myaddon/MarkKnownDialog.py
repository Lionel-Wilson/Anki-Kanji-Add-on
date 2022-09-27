import aqt
from aqt.qt import *

import anki.find

from . import util
from . import text_parser
from .card_type_radio_buttons import CardTypeRadioButtons


class MarkKnownDialog(QDialog):

    presets = [
        ('JLPT',                 'jlpt',           1, 5,     5,  5),
        ('Kanken',               'kanken',         1, 10,    10, 10),
        ('Frequency',            'frequency_rank', 1, 99999, 1,  25),
        ('School Year',          'grade',          1, 6,     1,  1),
        ('RTK ID (Edition 1-5)', 'heisig_id5',     1, 99999, 1,  25),
        ('RTK ID (Edition 6+)',  'heisig_id6',     1, 99999, 1,  25),
        ('WaniKani',             'wk',             1, 60,    1,  1),
    ]#Might delete later(REMOVE LATER)


    def __init__(self, initial_kanji=None, parent=None):
        super(QDialog, self).__init__(parent) #Inherit from Qt Qdialog class to access Qt Methods

        #lyt -> Layout(REMOVE LATER)
        Layout = QVBoxLayout()#Method that allows me to build a layout where objects are arranged vertically.
        self.setLayout(Layout)#setlayout() will place the QVBoxLayout() onto the Window/QDialog widget(i think)

        self.setWindowIcon(util.default_icon())#this holds the window icon. my face
        self.setWindowTitle('LionelvsLifeTV Kanji - Mark Kanji Known')#Set Title of Window

        #info_lbl -> Mark_known_explanation (REMOVE LATER)
        #QLabel = Provides a display for text/images.
        Mark_known_explanation = QLabel('All kanji in the box below will be marked known for the specified learning type when you press OK.\n\n' \
                          'Kanji that have a kanji card associated with them will not be marked.\n\n' \
                          'If you want to unmark a kanji later, go to the lookup browser and hit the "Unmark as known" button. ' \
                          'You can also mark individual kanji known by Shift-clicking on the "Create Recognition/Production Card" buttons in the lookup browser.')#EDIT THIS TEXT LATER (REMOVE LATER)
        Mark_known_explanation.setWordWrap(True) #Above text wraps to match the window size.
        Layout.addWidget(Mark_known_explanation) ##Add explanation to window layout

        Layout.addWidget(QLabel('<hr>')) #draw a line for seperation.(html)

        self.ct_selector = CardTypeRadioButtons()
        Layout.addWidget(self.ct_selector)

        self.txt_box = QPlainTextEdit()
        self.txt_box.setPlaceholderText('Enter Kanji which should be marked known')
        Layout.addWidget(self.txt_box)

        hlyt = QHBoxLayout()
        Layout.addLayout(hlyt)

        preset_btn = QPushButton('Load Preset')
        preset_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        preset_btn.clicked.connect(self.on_load_preset)
        hlyt.addWidget(preset_btn)

        self.preset_box = QComboBox()
        self.preset_box.addItems(p[0] for p in self.presets)
        self.preset_box.currentIndexChanged.connect(self.on_preset_change)
        hlyt.addWidget(self.preset_box)

        self.min_box = QSpinBox()
        self.min_box.setMaximumWidth(75)
        hlyt.addWidget(self.min_box)

        to_lbl = QLabel('to')
        to_lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        hlyt.addWidget(to_lbl)

        self.max_box = QSpinBox()
        self.max_box.setMaximumWidth(75)
        hlyt.addWidget(self.max_box)

        self.on_preset_change() # init first preset min/max

        if initial_kanji:
            self.txt_box.setPlainText(
                ''.join(text_parser.filter_cjk(initial_kanji))
            )
        
        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(self.mark_known)
        btn_box.rejected.connect(self.reject)
        lyt.addWidget(btn_box)