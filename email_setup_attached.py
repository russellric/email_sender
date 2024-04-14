from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from email_setup import Ui_main_window
#from email_login_attached import email_login_attached
import smtplib
import re

class email_setup_attached(Ui_main_window, QMainWindow):

    def __init__(self, from_email, password, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
        self.from_email = from_email
        self.password = password

        self.clear_all_button.clicked.connect(self.clear_all_clicked)

        self.send_button.clicked.connect(self.send_clicked)

        self.logout_button.clicked.connect(self.logout_clicked)

    def clear_all_clicked(self):
        self.ERROR_message.setText("")
        self.enter_to_email.setText("")
        self.enter_subject.setText("")
        self.enter_message.setText("")

    def send_clicked(self):
        HOST = "smtp-mail.outlook.com"
        PORT = 587
        to_email = self.enter_to_email.text()
        if bool(re.match(r".+@.+\..+", to_email)) == False:
            self.ERROR_message.setText("ERROR: invalid email")
        else:
            smtp = smtplib.SMTP(HOST, PORT)
            smtp.starttls()
            smtp.login(self.from_email, self.password)

            message = f"""Subject: {self.enter_subject.text()}\n\n{self.enter_message.text()}"""

            smtp.sendmail(self.from_email, to_email, message)
            smtp.quit()
            self.ERROR_message.setText("Email Sent")
        
    def logout_clicked(self):
        self.close()
        #self.email_login_win = QMainWindow()
        #self.email_loginUi = email_login_attached(self.email_login_win)
        #self.email_loginUi.show()