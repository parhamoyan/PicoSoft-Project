import random
from datetime import datetime
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class ProgressCircularChart(QFrame):
    def __init__(
            self,
            parent=None,
            color = "#a72cf4",
            percentage = 45,
            penSize = 12,
            fontSize = 16,
            letterSpacing = .6
        ):
        QFrame.__init__(self, parent=parent)
        random.seed(datetime.now())
        self.resize(200, 200)
        self.penSize = penSize
        self.fontSize = fontSize
        self.percentage = percentage
        self.percentage = random.randint(0, 100)
        self.color = color
        self.letterSpacing = letterSpacing
    
    def initFont(self):
        self.font = QFont()
        self.font.setFamily(u"Poppins")
        self.font.setPointSize(self.width()*16/212)
        self.font.setWeight(QFont.DemiBold)
        self.font.setLetterSpacing(QFont.AbsoluteSpacing, self.letterSpacing)
    
    def setColor(self, newColor):
        self.color = newColor
    
    def setRayon(self, newRayon):
        self.rayon = newRayon
    
    def paintEvent(self, e):
        self.initFont()
        self.rayon = self.width()*.55
        self.painter = QPainter()
        self.painter.begin(self)
        self.pen = QPen()
        self.pen.setStyle(Qt.SolidLine)
        self.pen.setCapStyle(Qt.RoundCap)
        self.painter.setPen(self.pen)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.pen.setColor(QColor("#292c31"))
        self.pen.setWidth(self.width()*12/212)
        self.painter.setPen(self.pen)
        centerX = (self.width()-self.rayon)/2
        centerY = (self.height()-self.rayon)/2
        self.painter.drawArc(centerX, centerY, self.rayon, self.rayon, 0 * 16, 360 * 16)
        self.pen.setColor(QColor(self.color))
        self.painter.setPen(self.pen)
        self.painter.drawArc(centerX, centerY, self.rayon, self.rayon, 90 * 16, -self.percentage * 3.6 * 16)
        self.painter.setFont(self.font)
        self.painter.setPen(self.pen)
        self.pen.setColor(QColor(self.color))
        self.painter.setPen(self.pen)
        self.painter.drawText(0, 0, self.width(), self.height(), Qt.AlignVCenter|Qt.AlignHCenter, "{}%".format(str(self.percentage)))
        self.painter.end()