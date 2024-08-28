import sys, discordrpc, ctypes, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('flaviogeneroso.lichess.desktop.1')

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

rpc = discordrpc.RPC(app_id=1278135161267032094)

rpc.set_activity(ts_start=discordrpc.utils.timestamp)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.lichess.org"))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Lichess")
        self.setWindowIcon(QtGui.QIcon(get_resource_path("icon.png")))
        QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.on_esc)

    def keyPressEvent(self, event):
        if event.key() == 16777274:
            self.showFullScreen()

    def on_esc(self):
        self.close() if not self.isFullScreen() else self.showMaximized()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    rpc.run()