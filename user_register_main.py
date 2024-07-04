from PyQt6.QtWidgets import QMessageBox, QLineEdit, QApplication

from toast import toast_message
from user_Register_py import Ui_MainWindow
import sys
import mysql.connector
from PyQt6 import QtWidgets

class register(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_db()
        self.user_regiser_conpasswordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_regiser_passwordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.user_regiser_cancelbutton.clicked.connect(self.handlecancel)
        self.user_regiser_registerbutton.clicked.connect(self.handleregister)
        self.user_regiser_backbutton.clicked.connect(self.gobacklogin)

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

    def handleregister(self):
        user = self.user_regiser_usernamelineEdit.text()
        passwd = self.user_regiser_passwordlineEdit.text()
        conpasswd = self.user_regiser_conpasswordlineEdit.text()
        email = self.user_regiser_emaillineEdit.text()
        phone = self.user_regiser_phonelineEdit.text()

        if user and passwd and conpasswd and email and phone:
            if passwd == conpasswd:
                try:
                    conn = self.connect_db()
                    cursor = conn.cursor()

                    cursor.execute("insert into users(username,password,phone_no,email)"
                                   "values(%s,%s,%s,%s)",(user,passwd,phone,email))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    toast_message("Registered successfully!!",self)
                    self.handlecancel()
                    self.gobacklogin()
                except mysql.connector.Error as err:
                    QMessageBox.critical(self, "Database Error", f"Error:{err}")
                    print(f"Database error : {err}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error : {e}")
                    print(f"Error : {e}")

            else:
                toast_message("Password does not match!!",self)
                self.user_regiser_passwordlineEdit.clear()
                self.user_regiser_conpasswordlineEdit.clear()

        else:
            toast_message("Please fill in all the fields",self)



    def handlecancel(self):
        self.user_regiser_usernamelineEdit.clear()
        self.user_regiser_passwordlineEdit.clear()
        self.user_regiser_conpasswordlineEdit.clear()
        self.user_regiser_phonelineEdit.clear()
        self.user_regiser_emaillineEdit.clear()

    def gobacklogin(self):
        from user_login_main import login
        self.login = login()
        self.login.show()
        self.hide()

'''app = QApplication([])
reg = register()
reg.show()
sys.exit(app.exec())'''