from PyQt6.QtWidgets import QMessageBox, QLineEdit

from toast import toast_message
from user_login_py import Ui_MainWindow
import sys
import mysql.connector
from PyQt6 import QtWidgets

class login(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_db()
        self.user_login_passwordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.user_login_loginButton.clicked.connect(self.handlelogin)
        self.user_login_exitButton.clicked.connect(self.handleExit)
        self.user_login_cancelButton.clicked.connect(self.handleCancel)
        self.user_login_registerButton.clicked.connect(self.handleregister)

    def connect_db(self):
        try:
            # MySQL database connection

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="outage"
            )
            return db
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error:{err}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error : {e}")


    def handlelogin(self):
        user = self.user_login_usernamelineEdit.text()
        passwd = self.user_login_passwordlineEdit.text()
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            if user and passwd:

                cursor.execute("SELECT * FROM users WHERE username = %s and password = %s",(user, passwd))
                result =cursor.fetchone()

                if result:

                    toast_message("login successful",self)
                    self.handleCancel()
                else:
                    self.handleCancel()
                    toast_message("Invalid username or password", self)

            else:
                toast_message("Please enter username and password to login",self)

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self,"Database Error",f"Error:{err}")
            print(f"Database error : {err}")
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error : {e}")
            print(f"Error : {e}")

    def handleCancel(self):
        self.user_login_usernamelineEdit.clear()
        self.user_login_passwordlineEdit.clear()

    def handleExit(self):
        self.close()

    def handleregister(self):
        from user_register_main import register
        self.reg = register()
        self.reg.show()
        self.hide()


'''app = QtWidgets.QApplication([])
login = login()
login.show()
sys.exit(app.exec())'''
