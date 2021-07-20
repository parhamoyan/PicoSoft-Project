from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class ProfilesContainer(QFrame):
    def __init__(self,
            *args,
            antialiasing=True,
            borderColor="#ae2b3f",
            borderSize=1,
            **kwargs):
        super(ProfilesContainer, self).__init__(*args, **kwargs)
        self.Antialiasing = antialiasing

        self.paths = list()
        self.paths.append("profiles/bebe-rexha.jpg")
        self.paths.append("profiles/justin-timberlake.jpg")
        
        self.borderColor = borderColor
        self.borderSize = borderSize

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)

        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

            
        for i in range(len(self.paths)-1, -1, -1):
            x = self.height()*.8*i

            # DRAW BORDER
            painter2 = QPainter()
            painter2.begin(self)
            painter2.setPen(Qt.NoPen)

            if self.Antialiasing:
                painter2.setRenderHint(QPainter.Antialiasing, True)
                painter2.setRenderHint(QPainter.SmoothPixmapTransform, True)
            painter2.setBrush(QColor(self.borderColor))
            painter2.drawEllipse(x, 0, self.height(), self.height())

            p = QPixmap(self.paths[i]).scaled(
                self.height(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            path = QPainterPath()
            d = self.height()-self.borderSize*2
            path.addRoundedRect(
                x+self.borderSize, self.borderSize, d, d, d/2, d/2)
            painter.setClipPath(path)
            painter.drawPixmap(x, 0, p)

        painter.end()
        painter2.end()


    