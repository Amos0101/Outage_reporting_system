from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QCalendarWidget, QDateEdit, QDateTimeEdit, \
    QLabel, QLineEdit, QHBoxLayout

class timewidgets(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calender widget")
        self.setFixedSize(300,300)
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        self.layout = QHBoxLayout()
        centralwidget.setLayout(self.layout)
        self.setLayout(self.layout)

        #self.qcalender()
        self.qdateedit()

    def qcalender(self):
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("select date")
        self.layout.addWidget(self.lineedit)

        #set up the calender widget
        self.calender = QCalendarWidget()
        self.calender.setGridVisible(True)
        self.layout.addWidget(self.calender)
        self.calender.selectionChanged.connect(self.update_lineedit)

    def update_lineedit(self):
        selected_date = self.calender.selectedDate()
        self.lineedit.setText(selected_date.toString("yyyy-mm-dd"))

    def qdateedit(self):
        #create the dateEdit widget
        self.dateedit = QDateEdit()
        self.dateedit.setCalendarPopup(True)
        self.dateedit.setDate(QDate.currentDate())
        self.layout.addWidget(self.dateedit)


app = QApplication([])
window = timewidgets()
window.show()
app.exec()