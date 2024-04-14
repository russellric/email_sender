from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from email_login import Ui_login_window
from email_setup_attached import email_setup_attached
import smtplib
import re

class email_login_attached(Ui_login_window, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

        #login button
        self.Login_button.clicked.connect(self.Login_button_clicked)


    def Login_button_clicked(self):
        HOST = "smtp-mail.outlook.com"
        PORT = 587

        from_email = self.enter_email.text()
        password = self.enter_pw.text()
        if bool(re.match(r".+@.+\..+", from_email)) == False:
            self.ERROR_message.setText("ERROR: invalid email")
        else:
            try:
                smtp = smtplib.SMTP(HOST, PORT)

                status_code, response = smtp.ehlo()
                print(f"[*] Echoingthe server: {status_code} {response}")

                status_code, response = smtp.starttls()
                print(f"[*] Starting TLS connection: {status_code} {response}")

                status_code, response = smtp.login(from_email, password)
                print(f"[*] Starting TLS connection: {status_code} {response}")
                
                self.hide()
                self.email_setup_win = QMainWindow()
                #print('line 41')
                self.email_setupUi = email_setup_attached(from_email, password, self.email_setup_win)
                #print('line 42')
                self.email_setupUi.show()
            except:
                self.ERROR_message.setText("ERROR: incorect password")


