import random
from datetime import datetime
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class DonutChart(QFrame):
    def __init__(
            self,
            parent=None
            ):
        QFrame.__init__(self, parent=parent)
        self.resize(200, 200)
        self.rayon = 120
        self.penSize = 12
        self.fontSize = 16
        self.initFont()
    
    def initFont(self):
        self.font = QFont()
        self.font.setFamily(u"Poppins")
        self.font.setPointSize(self.fontSize)
        self.font.setWeight(QFont.DemiBold)
        self.font.setLetterSpacing(QFont.AbsoluteSpacing, .6)
    
    def paintEvent(self, e):
        self.painter = QPainter()
        self.painter.begin(self)
        self.pen = QPen()
        self.pen.setStyle(Qt.SolidLine)
        self.pen.setCapStyle(Qt.RoundCap)
        self.painter.setPen(self.pen)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.pen.setColor(QColor("#292c31"))
        self.pen.setWidth(self.penSize)
        self.painter.setPen(self.pen)
        centerX = (self.width()-self.rayon)/2
        centerY = ((self.height()-self.rayon)*.7)/2
        self.painter.drawArc(centerX, centerY, self.rayon, self.rayon, 0 * 16, 360 * 16)
        self.pen.setColor(QColor("#a72cf4"))
        self.painter.setPen(self.pen)
        self.painter.drawArc(centerX, centerY, self.rayon, self.rayon, 90 * 16, -160 * 16)
        self.pen.setColor(QColor("#2a9df0"))
        self.painter.setPen(self.pen)
        self.painter.drawArc(centerX, centerY, self.rayon, self.rayon, 90 * 16, -110 * 16)
        self.pen.setColor(QColor("#f11a44"))
        self.painter.setPen(self.pen)
        self.painter.drawArc(centerX, centerY, self.rayon, self.rayon, 90 * 16, -90 * 16)
        self.initFont()
        self.painter.setFont(self.font)
        self.painter.setPen(self.pen)
        self.pen.setColor(QColor("#bb6f56"))
        self.painter.setPen(self.pen)
        self.painter.drawText(0, 0, self.width(), self.height(), Qt.AlignVCenter|Qt.AlignHCenter, "45%")
        self.painter.end()