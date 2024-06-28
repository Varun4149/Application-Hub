import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class gui():
    def __init__(self):
        super().__init__()
        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.brower = QWebEngineView()
                self.brower.setUrl(QUrl("http://google.com"))
                self.setCentralWidget(self.brower)
                self.showMaximized()

                # Navbar
                navbar = QToolBar()
                self.addToolBar(navbar)

                back_btn = QAction("Back",self)
                back_btn.triggered.connect(self.brower.back)
                navbar.addAction(back_btn)

                forward_btn = QAction('Forward',self)
                forward_btn.triggered.connect(self.brower.forward)
                navbar.addAction(forward_btn)

                reload_btn = QAction("Reload",self)
                reload_btn.triggered.connect(self.brower.reload)
                navbar.addAction(reload_btn)

                home_btn = QAction("Home",self)
                home_btn.triggered.connect(self.navigate_home)
                navbar.addAction(home_btn)

                self.url_bar = QLineEdit()
                self.url_bar.returnPressed.connect(self.navigator)
                navbar.addWidget(self.url_bar)

                self.brower.urlChanged.connect(self.update_url)

            def navigate_home(self):
                self.brower.setUrl(QUrl("http://google.com"))

            def navigator(self):
                url = self.url_bar.text()
                self.brower.setUrl(QUrl(url))
                
            def update_url(self,q):
                self.url_bar.setText(q.toString())

        app = QApplication(sys.argv)
        QApplication.setApplicationName("MY BROWSER")
        windows = MainWindow()
        app.exec_()

if __name__=="__main__":
    gui()