import sys
import typing
from PyQt5.QtCore import QUrl
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimedia import QSoundEffect
import random


cwin = "haha I the computeri winsss!!!!!!\n"
pwin = "you just got lucky for once- ugh fine you win\n"
draw = "woah, its a tie\n"
p_score_log=[]
c_score_log=[]
ptextlog=['','','']
ctextlog=['','','']
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
        else:
            userBull = 2

        compBull = random.randint(0, 3)

        if userBull == compBull:
            self.output.setText(draw)
            c_score_log.append(1)
            p_score_log.append(1)
            ctextlog.append(draw)
            ptextlog.append(draw)
            self.p1.setText(ptextlog[-1])
            self.p2.setText(ptextlog[-2])
            self.p3.setText(ptextlog[-3])
            self.c1.setText(ctextlog[-1])
            self.c2.setText(ctextlog[-2])
            self.c3.setText(ctextlog[-3])
            # self.play_sound("tie")
        elif (
            (userBull == 0 and compBull == 2)
            or (userBull == 1 and compBull == 0)
            or (userBull == 2 and compBull == 1)
        ):
            self.output.setText(pwin)
            c_score_log.append(0)
            p_score_log.append(2)
            ctextlog.append(pwin)
            ptextlog.append(pwin)
            self.p1.setText(ptextlog[-1])
            self.p2.setText(ptextlog[-2])
            self.p3.setText(ptextlog[-3])
            self.c1.setText(ctextlog[-1])
            self.c2.setText(ctextlog[-2])
            self.c3.setText(ctextlog[-3])
            self.play_sound("user_win")
        else:
            self.output.setText(cwin)
            c_score_log.append(2)
            p_score_log.append(0)
            ctextlog.append(cwin)
            ptextlog.append(cwin)
            self.p1.setText(ptextlog[-1])
            self.p2.setText(ptextlog[-2])
            self.p3.setText(ptextlog[-3])
            self.c1.setText(ctextlog[-1])
            self.c2.setText(ctextlog[-2])
            self.c3.setText(ctextlog[-3])
            self.play_sound("computer_win")

        if len(c_score_log)==3:
            if sum(p_score_log)>sum(c_score_log):
                self.output.setText("Whoa, you won the best of 3!\n")
                c_score_log.clear()
                p_score_log.clear()
            elif sum(p_score_log)<sum(c_score_log):
                self.output.setText("haha I the computeri wins the best of 3!!!!!!\n")
                c_score_log.clear()
                p_score_log.clear()
            else:
                self.output.setText("Looks like its still a draw, lets do another best of 3 again.")
                c_score_log.clear()
                p_score_log.clear()
        
    

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
