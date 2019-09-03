from PyQt5 import QtWidgets
import sys

from core.MainUI.ui import main_ui


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main_ui()
    window.show()
    app.exec_()