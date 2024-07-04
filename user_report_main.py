from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QMessageBox, QLineEdit
from toast import toast_message
from user_report_py import Ui_MainWindow
import sys
import mysql.connector
from PyQt6 import QtWidgets

class report(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.provinces_and_cities = {
            'Nairobi': ['Nairobi'],
            'Central': ['Nyeri', 'Murang\'a', 'Kiambu', 'Kirinyaga'],
            'Coast': ['Mombasa', 'Kwale', 'Kilifi', 'Tana River', 'Lamu', 'Taita-Taveta'],
            'Eastern': ['Meru', 'Embu', 'Kitui', 'Machakos', 'Makueni', 'Tharaka-Nithi'],
            'North Eastern': ['Garissa', 'Mandera', 'Wajir'],
            'Nyanza': ['Kisumu', 'Siaya', 'Homa Bay', 'Migori', 'Kisii', 'Nyamira'],
            'Rift Valley': ['Nakuru', 'Eldoret', 'Kericho', 'Narok', 'Baringo', 'Kajiado'],
            'Western': ['Kakamega', 'Bungoma', 'Busia', 'Vihiga']
        }
        self.user_report_provincecomboBox.setPlaceholderText("Select your province")
        self.user_report_citycomboBox.setPlaceholderText("Select your city")

        self.user_report_provincecomboBox.addItems(self.provinces_and_cities.keys())
        self.user_report_provincecomboBox.currentTextChanged.connect(self.update_cities)


        self.outage_type = {
            'Water':'0798477794',
            'Power':'0123456789',
            'Internet':'012555555',
            'Gas':'0100022233'
        }
        self.user_report_outTypecomboBox.setPlaceholderText("Select outage type")
        self.user_repo_companyphonelineEdit.setReadOnly(True)

        self.user_report_outTypecomboBox.addItems(self.outage_type.keys())
        self.user_report_outTypecomboBox.currentTextChanged.connect(self.update_companyPhone)

        self.user_report_outTimedateTimeEdit.setCalendarPopup(True)
        self.user_report_outTimedateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        self.user_report_reportTimedateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.user_report_reportTimedateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.user_report_reportTimedateTimeEdit.setReadOnly(True)

    def update_cities(self):
        province = self.user_report_provincecomboBox.currentText()
        cities = self.provinces_and_cities.get(province,[])

        self.user_report_citycomboBox.clear()
        self.user_report_citycomboBox.addItems(cities)

    def update_companyPhone(self):
        outage_type = self.user_report_outTypecomboBox.currentText()
        number = self.outage_type.get(outage_type,"")
        self.user_repo_companyphonelineEdit.setText(number)

app = QtWidgets.QApplication([])
rep = report()
rep.show()
sys.exit(app.exec())