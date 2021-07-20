# The idea is taken from : https://www.instagram.com/p/CQNDwlNj6cp/?utm_medium=share_sheet

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CustomCalendar(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)

        # PREVENT RESIZE AND SET POINTING HAND CURSOR
        self.resize(230, 280)
        self.setCursor(Qt.PointingHandCursor)

        buttonTop = QPushButton(self)
        buttonTop.move(180, 18)
        buttonTop.resize(12, 8)
        buttonTop.setStyleSheet("""
            background-color: transparent;
            border-image: url(icons/buttonTop.png) 0 0 0 0 stretch stretch;;
            border: none;
        """)

        buttonBottom = QPushButton(self)
        buttonBottom.move(200, 18)
        buttonBottom.resize(12, 8)
        buttonBottom.setStyleSheet("""
            background-color: transparent;
            border-image: url(icons/buttonBottom.png) 0 0 0 0 stretch stretch;;
            border: none;
        """)

    def initFont(self,
            fontName = u"Poppins",
            pointSize = 10,
            wordSpacing = 10,
            weight = QFont.DemiBold
        ):
        self.font = QFont()
        self.font.setFamily(fontName)
        self.font.setPointSize(pointSize)
        self.font.setWordSpacing(wordSpacing)
        self.font.setWeight(weight)
    
    def initializePainter(self):
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setBrush(QBrush(QColor("#181b20"), Qt.SolidPattern))
        self.painter.setFont(self.font)

    def initMatrix(self):
        self.matrix = [[] for i in range(6)]
        self.dict = dict()
        d = 28
        i, j = 0, 0
        ok = True
        while (i < 6):
            while (j < 7):
                if d > 31:
                    d = 1
                    ok = False
                    break
                self.matrix[i].append((False, d))
                d += 1
                j += 1
            if not ok:
                break
            j = 0
            i += 1

        ok = True
        while (i < 6):
            while (j < 7):
                if d > 30:
                    d = 1
                    ok = False
                    break
                self.matrix[i].append((True, d))
                d += 1
                j += 1
            if not ok:
                break
            j = 0
            i += 1

        ok = True
        while (i < 6):
            while (j < 7):
                if d > 30:
                    d = 1
                    ok = False
                    break
                self.matrix[i].append((False, d))
                d += 1
                j += 1
            if not ok:
                break
            j = 0
            i += 1

    def paintEvent(self, e) -> None:
        self.initFont(pointSize=12)
        self.initializePainter()   
        self.painter.setPen(Qt.NoPen)
        self.painter.drawRoundedRect(0, 0, self.width(), self.height(), 20, 20)
        self.painter.setPen(QColor("#d1d3d2"))
        rect = QRect(15, 10, 100, 40)
        self.painter.drawText(rect, Qt.AlignLeft|Qt.AlignAbsolute, "April 2021")
        self.font.setPointSize(10)
        self.painter.setFont(self.font)
        self.painter.setPen(QColor("#999a9d"))
        days = ["Su", "Mo", "Tu", "We", "Th", "Fri", "Sa"]
        for i in range(7):
            rect = QRect(15+i*30, 40, 30, 30)
            self.painter.drawText(rect, Qt.AlignLeft|Qt.AlignAbsolute, days[i])
        self.initMatrix()
        self.painter.setPen(Qt.NoPen)
        self.painter.setBrush(QColor("#192f44"))
        self.painter.drawRect(10+15+2*30, 70+4*30, 30*3, 30)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                rect = QRect(10+j*30, 70+i*30, 30, 30)
                value = self.matrix[i][j][1]
                colorBool = self.matrix[i][j][0]
                if value == 13:
                    self.painter.setPen(Qt.NoPen)
                    self.painter.setBrush(QColor("#ea6c1e"))
                    self.painter.drawEllipse(10+j*30, 70+i*30, 30, 30)
                if value in [27, 30] and colorBool:
                    self.painter.setPen(Qt.NoPen)
                    self.painter.setBrush(QColor("#2695dd"))
                    self.painter.drawEllipse(10+j*30, 70+i*30, 30, 30)
                self.painter.setPen(QColor(["#7c7d82", "#d1d3d2"][self.matrix[i][j][0]]))
                self.painter.drawText(rect, Qt.AlignHCenter|Qt.AlignVCenter, str(self.matrix[i][j][1]))
        self.painter.end()
