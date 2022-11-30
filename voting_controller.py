from PyQt5.QtWidgets import *
from voting_view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.setupVote())
        self.description.setText('')
        self.votebutton_john.clicked.connect(lambda: self.voted('John'))
        self.votebutton_jane.clicked.connect(lambda: self.voted('Jane'))
        self.votebutton_jane.setHidden(True)
        self.votebutton_john.setHidden(True)
        self.heading.setHidden(True)

    def setupVote(self):
        self.votebutton_john.setEnabled(True)
        self.votebutton_jane.setEnabled(True)
        self.heading.setEnabled(True)
        self.pushButton.setHidden(True)
        self.votebutton_jane.setHidden(False)
        self.votebutton_john.setHidden(False)
        self.heading.setHidden(False)

    def voted(self, name):
        self.description.setText(f'YOU VOTED FOR {name}!')

