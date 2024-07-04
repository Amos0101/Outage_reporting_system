import sys

import mysql
from PyQt6.QtWidgets import QMessageBox, QApplication

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
