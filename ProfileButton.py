from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class ProfileButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(ProfileButton, self).__init__(*args, **kwargs)

    def initFont(
            self,
            fontName = u"Poppins",
            pointSize = 10
        ):
        self.font = QFont()
        self.font.setFamily(fontName)
        self.font.setPointSize(pointSize)

    def paintEvent(self, e):
        r = 40
        p = QPixmap("profiles/parham.jpg").scaled(  
            r, r, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter = QPainter()
        painter.begin(self)
        if QPainter.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addRoundedRect(
            0, 0, r, r, r/2, r/2)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        painter.end()

        painter = QPainter()
        painter.begin(self)
        self.initFont()
        painter.setFont(self.font)
        painter.setPen(QColor("#d1d3d2"))
        painter.drawText(r+10, 2, 100, 20, Qt.AlignLeft|Qt.AlignLeft, "Parham Oyan")
        self.initFont(pointSize=8)
        painter.setFont(self.font)
        painter.setPen(QColor("#6e6f74"))
        painter.drawText(r+10, 23, 100, 20, Qt.AlignLeft|Qt.AlignLeft, "Employer")
        p = QPixmap("icons/buttonBottom.png").scaled(  
            r, r, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter.drawPixmap(155, 18, 12, 8, p)
        painter.end()