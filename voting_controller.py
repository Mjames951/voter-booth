from PyQt5.QtWidgets import *
from voting_view import *
import csv

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.voterid_button_submit.clicked.connect(lambda: self.voterid_submit())
        self.vote_button_john.clicked.connect(lambda: self.voted('John'))
        self.vote_button_jane.clicked.connect(lambda: self.voted('Jane'))
        self.vote_button_confirm.clicked.connect(lambda: self.voted_submit())
        self.end_button_again.clicked.connect(lambda: self.vote_again())

        self.__vote = ''
        self.__voterid = 0

    def voterid_submit(self):
        '''
        voterid_submit will first set the text box as empty and store the id in self.__voterid
        the voterid has to be a 5 digit number and cannot start with 0, nor can it have a string
        '''
        self.__voterid = self.voterid_textbox_voterid.text()
        self.voterid_textbox_voterid.setText('')
        try:
            if self.__voterid[0] == '0':
                raise Exception
            self.__voterid = int(self.__voterid)
            if self.__voterid < 9999 or self.__voterid > 99999:
                raise Exception
        except:
            self.voterid_label_error.setText('Voter ID must be a 5 digit number,\nand cannot start with 0')
        else:

            #TAKES AWAY VOTER ID GUI
            self.voterid_label_error.setText('')
            self.voterid_textbox_voterid.setHidden(True)
            self.voterid_textbox_voterid.setEnabled(False)
            self.voterid_button_submit.setHidden(True)
            self.voterid_button_submit.setEnabled(False)
            self.voterid_label_error.setHidden(True)
            self.voterid_label_entertext.setHidden(True)
            self.voterid_label_entertext.setEnabled(False)
            self.voteid_label_topdescription.setHidden(True)

            #ADDS IN VOTING GUI
            self.vote_picture_john.setHidden(False)
            self.vote_picture_john.setEnabled(True)
            self.vote_picture_jane.setHidden(False)
            self.vote_picture_jane.setEnabled(True)
            self.vote_button_jane.setHidden(False)
            self.vote_button_jane.setEnabled(True)
            self.vote_button_john.setHidden(False)
            self.vote_button_john.setEnabled(True)
            self.vote_label_selecttext.setHidden(False)
            self.vote_label_selecttext.setEnabled(True)


    def voted(self, selection: str):
        '''
        :param selection: which candidate was selected based off the 2 selection buttons
        Then adds in the Voting confirmation GUI
        '''
        self.vote_button_confirm.setHidden(False)
        self.vote_button_confirm.setEnabled(True)
        self.vote_label_sure.setEnabled(True)
        self.vote_label_sure.setHidden(False)
        self.vote_label_sure.setText(f'Are you sure you want to vote for {selection}?')
        self.__vote = selection

    '''
    vote_submit will first try to open the Votes file if it already exists
    if it doesn't exist it will create is and add the tally
    '''
    def voted_submit(self):
        do_heading = False
        try:
            open('Votes.csv')
        except FileNotFoundError:
            do_heading = True
        finally:
            with open('Votes.csv', 'a', newline='') as cfile:
                fieldnames = ['John', 'Jane', 'Voter ID']
                writer = csv.DictWriter(cfile, fieldnames=fieldnames)
                if do_heading == True:
                    writer.writeheader()
                if self.__vote == 'John':
                    writer.writerow({'John': '|', 'Jane': '', 'Voter ID': self.__voterid})
                else:
                    writer.writerow({'John': '', 'Jane': '|', 'Voter ID': self.__voterid})
                cfile.close()

        #TAKES AWAY VOTING SCREEN GUI
        self.vote_picture_john.setHidden(True)
        self.vote_picture_john.setEnabled(False)
        self.vote_picture_jane.setHidden(True)
        self.vote_picture_jane.setEnabled(False)
        self.vote_button_jane.setHidden(True)
        self.vote_button_jane.setEnabled(False)
        self.vote_button_john.setHidden(True)
        self.vote_button_john.setEnabled(False)
        self.vote_label_selecttext.setHidden(True)
        self.vote_label_selecttext.setEnabled(False)
        self.vote_button_confirm.setHidden(True)
        self.vote_button_confirm.setEnabled(False)
        self.vote_label_sure.setHidden(True)
        self.vote_label_sure.setEnabled(False)

        #BRINGS IN END SCREEN GUI
        self.end_label_thanks.setHidden(False)
        self.end_label_thanks.setEnabled(True)
        self.end_button_again.setHidden(False)
        self.end_button_again.setEnabled(True)
    def vote_again(self):
        #GETS RID OF THE END SCREEN GUI
        self.end_label_thanks.setHidden(True)
        self.end_label_thanks.setEnabled(False)
        self.end_button_again.setHidden(True)
        self.end_button_again.setEnabled(False)

        #BRINGS BACK START SCREEN GUI
        self.voterid_label_error.setText('')
        self.voterid_textbox_voterid.setHidden(False)
        self.voterid_textbox_voterid.setEnabled(True)
        self.voterid_button_submit.setHidden(False)
        self.voterid_button_submit.setEnabled(True)
        self.voterid_label_error.setHidden(False)
        self.voterid_label_entertext.setHidden(False)
        self.voterid_label_entertext.setEnabled(True)
        self.voteid_label_topdescription.setHidden(False)

