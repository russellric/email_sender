import sys
from PyQt5 import QtWidgets
import email_login_attached

#needed to run the program
app = QtWidgets.QApplication(sys.argv)
email_login_win = QtWidgets.QMainWindow()
email_login_ui = email_login_attached.email_login_attached(email_login_win)
app.exec_()
