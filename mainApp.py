import sys
from stylesheet.design import * 
from PyQt5.QtWidgets import QMainWindow, QApplication
from mhyt import yt_download


class Downloader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnDownload.clicked.connect(self.download)
        
    def download(self):
        file_name = self.input_save.text() 
        url       = self.input_url.text()
        if self.mp3_option.isChecked() == True:
            yt_download(url, file_name+'.mp3')
        if self.mp4_option.isChecked() == True:
            yt_download(url, file_name+'.mp4',ismusic=True)


if __name__ == '__main__':
    yt = QApplication(sys.argv)
    download = Downloader()
    download.show()
    yt.exec()
        
    