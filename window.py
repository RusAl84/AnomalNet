import sys
from scan_detector import start
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.path_2_pcap = str()
        self.text = list()

        uic.loadUi('untitled.ui', self)

        self.pushButton.clicked.connect(self.btn_on_click)


    def flex(self):
        self.textBrowser.setHtml(f'{self.text}')

    def motor(self):
        self.text = start(self.path_2_pcap)
        self.flex()

    def btn_on_click(self):
        self.textBrowser.clear()
        self.path_2_pcap = QFileDialog.getOpenFileName(self, 'Open File', './')[0]
        self.motor()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())