from PyQt5.QtWidgets import QApplication
import sys
from View.main_window import MainWindow
from Controller.controller import Controller

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    controller = Controller(main_window)
    main_window.set_controller(controller)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()