import sys
import typing
from PyQt5.QtCore import QUrl
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimedia import QSoundEffect
import random


# while(True):
#     userBull = int (input("heyy, hi! so umm\n'0' - Rock\n'1' - Paper\n'2' - Scissors\nChoose onee!! : "))
#     compBull= random.randint(0,3)
#     if (userBull == compBull):
#         print("woah, its a tie\n")
#     elif ((userBull == 0 and compBull == 2) or (userBull == 1 and compBull == 0) or (userBull == 2 and compBull == 1)):
#         print("you just got lucky for once- ugh fine you win\n")
#     else :
#         print("haha I the computeri winsss!!!!!!\n")
class rockpaperscissors(QMainWindow):
    def __init__(self):
        super(rockpaperscissors, self).__init__()
        loadUi("rps.ui", self)
        self.setWindowTitle("ROCK-PAPER-SCISSORS")
        self.shoot.clicked.connect(self.shooted)
        self.counter = 1
        self.heading.setText(
            "heyy, hi! so umm\n'0' - Rock\n'1' - Paper\n'2' - Scissors\nChoose onee!! : "
        )

        self.computer_win_sound = QSoundEffect()
        self.computer_win_sound.setSource(QUrl.fromLocalFile("youLose.wav"))

        self.user_win_sound = QSoundEffect()
        self.user_win_sound.setSource(QUrl.fromLocalFile("youWin.wav"))

    def play_sound(self, outcome):
        if outcome == "computer_win":
            self.computer_win_sound.play()
        elif outcome == "user_win":
            self.user_win_sound.play()
        # elif outcome == "tie":
        #     self.tie_sound.play()

    def shooted(self):
        if self.rock.isChecked():
            userBull = 0
        elif self.paper.isChecked():
            userBull = 1
        elif self.scissors.isChecked():
            userBull = 2
        else:
            self.output.setText(">_< input your move\n")
            return

        compBull = random.randint(0, 3)

        if userBull == compBull:
            self.output.setText("woah, its a tie\n")
            # self.play_sound("tie")
        elif (
            (userBull == 0 and compBull == 2)
            or (userBull == 1 and compBull == 0)
            or (userBull == 2 and compBull == 1)
        ):
            self.output.setText("you just got lucky for once- ugh fine you win\n")
            self.play_sound("user_win")
        else:
            self.output.setText("haha I the computeri winsss!!!!!!\n")
            self.play_sound("computer_win")


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setMaximumHeight(600)
widget.setMaximumWidth(910)
widget.setMinimumHeight(600)
widget.setMinimumWidth(910)
rockpaperscissors = rockpaperscissors()
widget.addWidget(rockpaperscissors)

widget.show()

try:
    sys.exit(app.exec_())

except:
    print("bye-bye")
