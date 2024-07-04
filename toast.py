from PyQt6.QtCore import QTimer,Qt
from PyQt6.QtWidgets import QLabel

def toast_message(message,parent):
    #create a label to display the message
    toast = QLabel(message,parent)
    toast.setStyleSheet("background-color: white; color:blue;border:0px solid blue; border-radius:5px; padding:5px;")
    toast.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.ToolTip)
    toast.setAlignment(Qt.AlignmentFlag.AlignTop)

    #set the toast size and position
    toast.resize(toast.sizeHint())
    parent_rect = parent.frameGeometry()
    toast.move(parent_rect.center()-toast.rect().center())

    toast.show()

    #hide the toast message after 2 seconds (2000 ms)
    QTimer.singleShot(2000,toast.close)