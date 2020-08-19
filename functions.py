from sys import argv
from PyQt5 import QtWidgets, QtCore, QtGui
from tkinter import Tk
from PIL import ImageGrab
from requests import post


class Snipping(QtWidgets.QWidget):                          # this is where the visual stuff for the snipping is created
    def __init__(self):
        super().__init__()
        root = Tk("assssssssdddddddd")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.15)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.show()
        root.destroy()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(116, 120, 128, 200))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('image.png')


def takeSnip():
    app = QtWidgets.QApplication(argv)                          # this function prompts the user to take a snip
    window = Snipping()
    window.show()
    app.exec_()


def searchImage(path):                                              # this function reverse searches the image with
    searchUrl = 'http://www.google.com/searchbyimage/upload'        # given path and returns link
    multipart = {'encoded_image': (path, open(path, 'rb')), 'image_content': ''}
    response = post(searchUrl, files=multipart, allow_redirects=False)

    return response.headers['Location']
