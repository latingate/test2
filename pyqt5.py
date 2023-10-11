# Import sys for handle the
# exit status of the application.
import sys

# Importing required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# To create an instance of QApplication
# sys.argv contains the list of
# command-line argument
app = QApplication(sys.argv)

# To create an instance of application GUI
# root is an instance of QWidget,
# it provides all the features to
# create the application's window
root = QWidget()

# adding title to window
root.setWindowTitle('גל שריג')

# to place txt at the coordinates
root.move(500, 100)

# to display text
txt = QLabel('ברוכים הבאים!', parent=root)
txt.move(200, 150)
txt2 = QLabel('לחלון של גל שריג', parent=root)
txt2.move(200, 180)

# Show application's GUI
root.show()

# Run application's main loop
sys.exit(app.exec_())


