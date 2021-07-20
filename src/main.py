import sys
from UI_mainwindow import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ATTRIBUTES
        self.menuIcons = [
            "projects-icon",
            "projects-status-icon",
            "analytics-icon",
            "all-members",
            "chat-icon",
            "settings-icon"
        ]

        self.initProfileLabels()
        self.initProfileContainers()
        self.connectAllMenuButtons()
        self.setProgressCircularChartsColor()
        self.addLineEditActions()
    
    def addLineEditActions(self):
        self.ui.lineEdit.addAction(QIcon(QPixmap("icons/magnifier.png")), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.lineEdit.addAction(QIcon(QPixmap("icons/record-icon.png")), QLineEdit.ActionPosition.TrailingPosition)

    def setProgressCircularChartsColor(self):
        self.ui.frame_15.setColor("#ae2b3f")
        self.ui.frame_41.setColor("#2991e2")

    def connectAllMenuButtons(self):
        self.buttons = self.ui.frame_34.findChildren(QPushButton)
        for i in range(len(self.buttons)):
            btn = self.buttons[i]
            self.connectButton(btn, i)

    def initProfileLabels(self):
        self.ui.label_27.setImagePath("profiles/amanda.jpg")
        self.ui.label_33.setImagePath("profiles/eric.jpg")
        self.ui.label_36.setImagePath("profiles/arkel.jpg")
        self.ui.label_26.setImagePath("profiles/justin-timberlake.jpg")
        self.ui.label_60.setImagePath("profiles/stephen-amell.jpg")
        self.ui.label_67.setImagePath("profiles/bebe-rexha.jpg")
    
    def initProfileContainers(self):
        self.ui.frame_66.paths = [
            "profiles/taylor-swift.jpg",
            "profiles/chris-hemsworth.jpg"
        ]

        self.ui.frame_67.paths = [
            "profiles/dua-lipa.jpg",
            "profiles/kevin-hart.jpg",
            "profiles/robert-downey.jpg"
        ]
        self.ui.frame_67.borderColor = "#2991e2"

        self.ui.frame_69.paths = [
            "profiles/tom-hardy.jpg",
            "profiles/ryan-reynolds.jpg"
        ]
        self.ui.frame_69.borderColor = "#a72cf4"
            
    
    def connectButton(self, btn : QPushButton, index):
        btn.clicked.connect(lambda: self.updateStylesheets(index))

    def updateStylesheets(self, index):
        for i in range(len(self.buttons)):
            iconName = self.menuIcons[i]
            if (i == index):
                iconName += "-hover"
            if (i != index):
                self.buttons[i].setStyleSheet("""
                    background: transparent;
                    border: none;
                    color: #d1d3d2;
                    background-image: url(icons/{}.png);
                    background-position: left;
                    background-repeat: no-repeat;
                    border: 10px;
                    border: solid 0px;
                    border-left: 22px solid transparent;
                    color: rgb(215, 215, 215);
                    text-align: left;
                    padding-left: 40px;
                """.format(iconName))
            else:
                self.buttons[i].setStyleSheet("""
                    background-color: #171611;
                    border: none;
                    color: #d1d3d2;
                    border-right: 2px solid #dd936d;
                    color: #dd936d;
                    background-image: url(icons/{}.png);
                    background-position: left;
                    background-repeat: no-repeat;
                    border-left: 22px solid transparent;
                    text-align: left;
                    padding-left: 40px;
                """.format(iconName))
            
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())