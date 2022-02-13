 
import sys
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2 import QtCore


# example event handler
def quit_app():
    global application
    print("Quit!")
    application.exit()


# base application object for our app
application = QApplication(sys.argv)

# Create a Window
window = QWidget()
window.setWindowTitle("View Image")

# button
button = QPushButton("Quit", window)

# on click handler
button.clicked.connect(quit_app)

# Load Pic
picture = QPixmap("pytronics00.png")

# set up the label widget to display the pic
label = QLabel(window)
label.setPixmap(picture)
label.setGeometry(QtCore.QRect(10, 40, picture.width(), picture.height()))

# embiggen the window to correctly fit the pic
window.resize(picture.width()+20, picture.height()+100)
window.show()

# Let QT do its thing
sys.exit(application.exec_())
