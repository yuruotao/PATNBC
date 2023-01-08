try:
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QMovie
    from PyQt5.QtWidgets import QApplication, QSplashScreen, QWidget, QTimer
except ImportError:
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QMovie
    from PySide2.QtWidgets import QApplication, QSplashScreen, QWidget

class GifSplashScreen(QSplashScreen):

    def __init__(self, *args, **kwargs):
        super(GifSplashScreen, self).__init__(*args, **kwargs)
        self.movie = QMovie('welcome.gif')
        self.movie.frameChanged.connect(self.onFrameChanged)
        self.movie.start()

    def onFrameChanged(self, _):
        self.setPixmap(self.movie.currentPixmap())

    def duration(self, app_name, gif_time):
        import time
        base_time = time.time()
        start_time_1 = time.time() - base_time
        while start_time_1 < gif_time:
            app_name.processEvents()
            start_time_1 = time.time() - base_time
            continue

    def finish(self, widget):
        self.movie.stop()
        super(GifSplashScreen, self).finish(widget)


if __name__ == '__main__':
    import sys
    import cgitb

    cgitb.enable(format='text')
    app = QApplication(sys.argv)


    #qss_file = open('style_file.qss').read()
    #app.your_line_edit_control.setStyleSheet(qss_file)

    global splash
    splash = GifSplashScreen()
    splash.show()

# debug done