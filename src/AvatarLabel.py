from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class AvatarLabel(QLabel):
    def __init__(self,
            *args,
            antialiasing=True,
            imagePath = "profiles/parham.jpg",
            **kwargs):
        super(AvatarLabel, self).__init__(*args, **kwargs)
        self.Antialiasing = antialiasing
        self.imagePath = imagePath
    
    def setImagePath(self, newPath):
        self.imagePath = newPath
        
    def paintEvent(self, e):
        p = QPixmap(self.imagePath).scaled(  
            self.width(), self.width(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter = QPainter()
        painter.begin(self)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.width(), self.width()/2, self.width()/2)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        painter.end()