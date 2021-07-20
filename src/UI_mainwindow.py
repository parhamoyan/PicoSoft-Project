# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from CustomCalendar import CustomCalendar
from DonutChart import DonutChart
from ProgressCircularChart import ProgressCircularChart
from AvatarLabel import AvatarLabel
from ProfilesContainer import ProfilesContainer
from ProfileButton import ProfileButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1210, 715)
        MainWindow.setMinimumSize(QSize(700, 0))
        MainWindow.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #4c4d52;\n"
"    width: 4px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #4c4d52;\n"
"	min-height: 30px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #1f1f2b;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #1f1f2b;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: red;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal "
                        "{\n"
"    background: green;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #101018;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(220, 0))
        self.frame.setMaximumSize(QSize(200, 16777208))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setStyleSheet(u"border-right: 2 solid #1f1f2b;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"border-bottom: 2 solid #1f1f2b;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_31.setSpacing(15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(20, -1, -1, -1)
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(25, 25))
        self.label_32.setStyleSheet(u"border: none;")
        self.label_32.setPixmap(QPixmap(u"icons/Asset 3 1.png"))
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_32)

        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 25))
        self.label_39.setStyleSheet(u"border: none;")
        self.label_39.setPixmap(QPixmap(u"icons/Asset 4 1.png"))

        self.horizontalLayout_31.addWidget(self.label_39)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(9)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_4)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_34)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_34)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 55))
        font = QFont()
        font.setFamily(u"Poppins")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: #171611;\n"
"border: none;\n"
"color: #d1d3d2;\n"
"border-right: 2px solid #dd936d;\n"
"color: #dd936d;\n"
"background-image: url(icons/projects-icon-hover.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"border-left: 22px solid transparent;\n"
"text-align: left;\n"
"padding-left: 40px;")

        self.verticalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_34)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 55))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: #d1d3d2;\n"
"background-image: url(icons/projects-status-icon.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"border: 10px;\n"
"border: solid 0px; \n"
"border-left: 22px solid transparent;\n"
"color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"padding-left: 40px;")

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_34)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 55))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: #d1d3d2;\n"
"background-image: url(icons/analytics-icon.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"border: 10px;\n"
"border: solid 0px; \n"
"border-left: 22px solid transparent;\n"
"color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"padding-left: 40px;")

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_34)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 55))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: #d1d3d2;\n"
"background-image: url(icons/all-members.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"border: 10px;\n"
"border: solid 0px; \n"
"border-left: 22px solid transparent;\n"
"color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"padding-left: 40px;")

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_34)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 55))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: #d1d3d2;\n"
"background-image: url(icons/chat-icon.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"border: 10px;\n"
"border: solid 0px; \n"
"border-left: 22px solid transparent;\n"
"color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"padding-left: 40px;")

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_34)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 55))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: #d1d3d2;\n"
"background-image: url(icons/settings-icon.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"border: 10px;\n"
"border: solid 0px; \n"
"border-left: 22px solid transparent;\n"
"color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"padding-left: 40px;")

        self.verticalLayout_8.addWidget(self.pushButton_6)


        self.gridLayout_2.addWidget(self.frame_34, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_5)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 0))
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_52)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 30, 0, -1)
        self.frame_51 = QFrame(self.frame_52)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 30))
        self.frame_51.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(10)
        self.frame_51.setFont(font1)
        self.frame_51.setStyleSheet(u"border-bottom: 2 solid #1f1f2b;")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, 0, 20, 0)
        self.label_23 = QLabel(self.frame_51)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: #6e6f74;\n"
"border-right: none;")

        self.horizontalLayout_24.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_51)
        self.label_24.setObjectName(u"label_24")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: #6e6f74;\n"
"border-right: none;")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_24)


        self.verticalLayout_15.addWidget(self.frame_51)

        self.frame_55 = QFrame(self.frame_52)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 40))
        self.frame_55.setStyleSheet(u"")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(18, -1, 18, -1)
        self.label_27 = AvatarLabel(self.frame_55)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(30, 30))
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setStyleSheet(u"border: none;")

        self.horizontalLayout_26.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_55)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.horizontalLayout_26.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_55)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(10, 10))
        self.label_29.setMaximumSize(QSize(10, 10))
        self.label_29.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: #528e5b;")

        self.horizontalLayout_26.addWidget(self.label_29)


        self.verticalLayout_15.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_52)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 40))
        self.frame_56.setStyleSheet(u"")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(18, -1, 18, -1)
        self.label_33 = AvatarLabel(self.frame_56)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(30, 30))
        self.label_33.setMaximumSize(QSize(30, 30))
        self.label_33.setStyleSheet(u"border: none;")

        self.horizontalLayout_28.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_56)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.horizontalLayout_28.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_56)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(10, 10))
        self.label_35.setMaximumSize(QSize(10, 10))
        self.label_35.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: #528e5b;")

        self.horizontalLayout_28.addWidget(self.label_35)


        self.verticalLayout_15.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_52)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 40))
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(18, -1, 18, -1)
        self.label_36 = AvatarLabel(self.frame_57)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(30, 30))
        self.label_36.setMaximumSize(QSize(30, 30))
        self.label_36.setStyleSheet(u"border: none;")

        self.horizontalLayout_29.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_57)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.horizontalLayout_29.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_57)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(10, 10))
        self.label_38.setMaximumSize(QSize(10, 10))
        self.label_38.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: #a95860;")

        self.horizontalLayout_29.addWidget(self.label_38)


        self.verticalLayout_15.addWidget(self.frame_57)


        self.gridLayout_4.addWidget(self.frame_52, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 80))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(18, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_12)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setStyleSheet(u"background: transparent;\n"
"border: 2 solid #1f1f2b;\n"
"border-radius: 10px;\n"
"color: #6e6f74;")
        self.lineEdit.setCursorPosition(0)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(390, 16777215))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 19, -1, -1)
        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(16, 16))
        self.pushButton_10.setMaximumSize(QSize(16, 16))
        self.pushButton_10.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"icons/messages-box.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon)

        self.horizontalLayout_25.addWidget(self.pushButton_10)

        self.frame_54 = QFrame(self.frame_13)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(2, 20))
        self.frame_54.setStyleSheet(u"background-color: #1f1f2b;")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frame_54)

        self.pushButton_11 = QPushButton(self.frame_13)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(16, 16))
        self.pushButton_11.setMaximumSize(QSize(16, 16))
        self.pushButton_11.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u"icons/bell-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)

        self.horizontalLayout_25.addWidget(self.pushButton_11)

        self.frame_58 = QFrame(self.frame_13)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(2, 20))
        self.frame_58.setStyleSheet(u"background-color: #1f1f2b;")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frame_58)

        self.pushButton_12 = ProfileButton(self.frame_13)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setMaximumSize(QSize(180, 16777215))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"border: none;")

        self.horizontalLayout_25.addWidget(self.pushButton_12)


        self.horizontalLayout_23.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(700, 0))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_34.setSpacing(4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: #181b20;\n"
"border-radius: 20px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_11)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 18, -1, -1)
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_14)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 40))
        self.frame_35.setMaximumSize(QSize(16777215, 40))
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_35)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(4, 0, 4, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 0))
        self.frame_36.setMaximumSize(QSize(16777215, 20))
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_36)
        self.label_11.setObjectName(u"label_11")
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: #d1d3d2;")
        self.label_11.setFrameShape(QFrame.NoFrame)
        self.label_11.setTextFormat(Qt.AutoText)

        self.horizontalLayout_15.addWidget(self.label_11)

        self.pushButton_7 = QPushButton(self.frame_36)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(16, 16))
        self.pushButton_7.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon2 = QIcon()
        icon2.addFile(u"icons/buttonRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon2)

        self.horizontalLayout_15.addWidget(self.pushButton_7)


        self.verticalLayout_9.addWidget(self.frame_36)

        self.label_12 = QLabel(self.frame_35)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 15))
        font4 = QFont()
        font4.setFamily(u"Poppins")
        font4.setPointSize(8)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_9.addWidget(self.label_12)


        self.horizontalLayout_14.addWidget(self.frame_35)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_15 = ProgressCircularChart(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setMinimumSize(QSize(0, 140))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 30))
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 5, 0)
        self.frame_66 = ProfilesContainer(self.frame_16)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_66)

        self.pushButton_13 = QPushButton(self.frame_16)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(10, 10))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon3)

        self.horizontalLayout_30.addWidget(self.pushButton_13)


        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 30))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(4, 0, 4, 0)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 15))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: #6e6f74;")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 15))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color: #6e6f74;")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_14)


        self.verticalLayout_3.addWidget(self.frame_17)


        self.horizontalLayout_34.addWidget(self.frame_11)

        self.frame_37 = QFrame(self.frame_10)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: #181b20;")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_37)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 18, -1, -1)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 40))
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_39)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(4, 0, 4, 0)
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 0))
        self.frame_40.setMaximumSize(QSize(16777215, 20))
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_40)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"color: #d1d3d2;")
        self.label_15.setFrameShape(QFrame.NoFrame)
        self.label_15.setTextFormat(Qt.AutoText)

        self.horizontalLayout_18.addWidget(self.label_15)

        self.pushButton_8 = QPushButton(self.frame_40)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(16, 16))
        self.pushButton_8.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.pushButton_8.setIcon(icon2)

        self.horizontalLayout_18.addWidget(self.pushButton_8)


        self.verticalLayout_11.addWidget(self.frame_40)

        self.label_16 = QLabel(self.frame_39)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 15))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_11.addWidget(self.label_16)


        self.horizontalLayout_17.addWidget(self.frame_39)


        self.verticalLayout_10.addWidget(self.frame_38)

        self.frame_41 = ProgressCircularChart(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy2.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy2)
        self.frame_41.setMinimumSize(QSize(0, 140))
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_37)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 30))
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 5, 0)
        self.frame_67 = ProfilesContainer(self.frame_42)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 30))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32.addWidget(self.frame_67)

        self.pushButton_14 = QPushButton(self.frame_42)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(10, 10))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"border: none;")
        self.pushButton_14.setIcon(icon3)

        self.horizontalLayout_32.addWidget(self.pushButton_14)


        self.verticalLayout_10.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_37)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(16777215, 30))
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(4, 0, 4, 0)
        self.label_17 = QLabel(self.frame_43)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 15))
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"color: #6e6f74;")

        self.horizontalLayout_19.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_43)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 15))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: #6e6f74;")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_18)


        self.verticalLayout_10.addWidget(self.frame_43)


        self.horizontalLayout_34.addWidget(self.frame_37)

        self.frame_44 = QFrame(self.frame_10)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background-color: #181b20;\n"
"border-radius: 20px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_44)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 18, -1, -1)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(16777215, 40))
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_46)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 0, 4, 0)
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 0))
        self.frame_47.setMaximumSize(QSize(16777215, 20))
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_47)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: #d1d3d2;")
        self.label_19.setFrameShape(QFrame.NoFrame)
        self.label_19.setTextFormat(Qt.AutoText)

        self.horizontalLayout_21.addWidget(self.label_19)

        self.pushButton_9 = QPushButton(self.frame_47)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(16, 16))
        self.pushButton_9.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.pushButton_9.setIcon(icon2)

        self.horizontalLayout_21.addWidget(self.pushButton_9)


        self.verticalLayout_13.addWidget(self.frame_47)

        self.label_20 = QLabel(self.frame_46)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 15))
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_13.addWidget(self.label_20)


        self.horizontalLayout_20.addWidget(self.frame_46)


        self.verticalLayout_12.addWidget(self.frame_45)

        self.frame_48 = ProgressCircularChart(self.frame_44)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy2.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy2)
        self.frame_48.setMinimumSize(QSize(0, 140))
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_48)

        self.frame_49 = ProfilesContainer(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(16777215, 30))
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 5, 0)
        self.frame_69 = ProfilesContainer(self.frame_49)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 30))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_69)

        self.pushButton_15 = QPushButton(self.frame_49)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMaximumSize(QSize(10, 10))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"border: none;")
        self.pushButton_15.setIcon(icon3)

        self.horizontalLayout_33.addWidget(self.pushButton_15)


        self.verticalLayout_12.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_44)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 30))
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(4, 0, 4, 0)
        self.label_21 = QLabel(self.frame_50)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 15))
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"color: #6e6f74;")

        self.horizontalLayout_22.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_50)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 15))
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: #6e6f74;")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_22)


        self.verticalLayout_12.addWidget(self.frame_50)


        self.horizontalLayout_34.addWidget(self.frame_44)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.frame_24 = CustomCalendar(self.frame_9)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setMaximumSize(QSize(400, 16777215))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_24)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 317))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.frame_18 = QFrame(self.frame_8)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setMinimumSize(QSize(500, 0))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_18)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_18)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 60))
        self.frame_30.setStyleSheet(u"background-color: #181b20;\n"
"border-radius: 20px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.label_9 = QLabel(self.frame_32)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setFamily(u"Poppins")
        font5.setBold(False)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: #d1d3d2;")
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setTextFormat(Qt.AutoText)

        self.horizontalLayout_12.addWidget(self.label_9)


        self.horizontalLayout_11.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 20, -1)
        self.label_10 = QLabel(self.frame_33)
        self.label_10.setObjectName(u"label_10")
        font6 = QFont()
        font6.setFamily(u"Poppins")
        font6.setPointSize(9)
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"color: #6e6f74;")

        self.horizontalLayout_13.addWidget(self.label_10)


        self.horizontalLayout_11.addWidget(self.frame_33, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_18)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"background-color: #181b20;\n"
"border-radius: 20px;\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_31)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.frame_31)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background-color: #1f1f2b;\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 478, 408))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_53 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 60))
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_27.setSpacing(20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.label_25 = QLabel(self.frame_53)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(30, 20))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: #d1d3d2;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_25)

        self.frame_70 = QFrame(self.frame_53)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMaximumSize(QSize(2, 30))
        self.frame_70.setStyleSheet(u"background-color: #1f1f2b;\n"
"border-radius: 0px;")
        self.frame_70.setFrameShape(QFrame.NoFrame)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_70)

        self.label_26 = AvatarLabel(self.frame_53)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(40, 40))
        self.label_26.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_27.addWidget(self.label_26)

        self.frame_63 = QFrame(self.frame_53)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(16777215, 35))
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_63)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_63)
        self.label_30.setObjectName(u"label_30")
        font7 = QFont()
        font7.setFamily(u"Poppins")
        font7.setPointSize(7)
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_16.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_63)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font4)
        self.label_31.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.verticalLayout_16.addWidget(self.label_31)


        self.horizontalLayout_27.addWidget(self.frame_63)

        self.frame_86 = QFrame(self.frame_53)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMaximumSize(QSize(2, 30))
        self.frame_86.setStyleSheet(u"background-color: #1f1f2b;\n"
"border-radius: 0px;")
        self.frame_86.setFrameShape(QFrame.NoFrame)
        self.frame_86.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_86)

        self.frame_64 = QFrame(self.frame_53)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(100, 0))
        self.frame_64.setMaximumSize(QSize(16777215, 30))
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_64)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_64)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font7)
        self.label_56.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_22.addWidget(self.label_56)

        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_37.setSpacing(6)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_65)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(10, 10))
        self.label_57.setMaximumSize(QSize(10, 10))
        self.label_57.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: #528e5b;")

        self.horizontalLayout_37.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_65)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font4)
        self.label_58.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.horizontalLayout_37.addWidget(self.label_58)


        self.verticalLayout_22.addWidget(self.frame_65)


        self.horizontalLayout_27.addWidget(self.frame_64)


        self.verticalLayout_14.addWidget(self.frame_53)

        self.frame_59 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 60))
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_40.setSpacing(20)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(-1, 0, -1, 0)
        self.label_66 = QLabel(self.frame_59)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(30, 20))
        self.label_66.setFont(font)
        self.label_66.setStyleSheet(u"color: #d1d3d2;")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_66)

        self.frame_93 = QFrame(self.frame_59)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMaximumSize(QSize(2, 30))
        self.frame_93.setStyleSheet(u"background-color: #1f1f2b;\n"
"border-radius: 0px;")
        self.frame_93.setFrameShape(QFrame.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_40.addWidget(self.frame_93)

        self.label_67 = AvatarLabel(self.frame_59)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(40, 40))
        self.label_67.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_40.addWidget(self.label_67)

        self.frame_94 = QFrame(self.frame_59)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMaximumSize(QSize(16777215, 35))
        self.frame_94.setFrameShape(QFrame.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_94)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_94)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font7)
        self.label_68.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_25.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_94)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font4)
        self.label_69.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.verticalLayout_25.addWidget(self.label_69)


        self.horizontalLayout_40.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_59)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMaximumSize(QSize(2, 30))
        self.frame_95.setStyleSheet(u"background-color: #1f1f2b;\n"
"border-radius: 0px;")
        self.frame_95.setFrameShape(QFrame.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_40.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.frame_59)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(100, 0))
        self.frame_96.setMaximumSize(QSize(16777215, 30))
        self.frame_96.setFrameShape(QFrame.NoFrame)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_96)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.frame_96)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font7)
        self.label_70.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_26.addWidget(self.label_70)

        self.frame_98 = QFrame(self.frame_96)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.NoFrame)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_42.setSpacing(6)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.frame_98)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(10, 10))
        self.label_73.setMaximumSize(QSize(10, 10))
        self.label_73.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: #528e5b;")

        self.horizontalLayout_42.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_98)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font4)
        self.label_74.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.horizontalLayout_42.addWidget(self.label_74)


        self.verticalLayout_26.addWidget(self.frame_98)


        self.horizontalLayout_40.addWidget(self.frame_96)


        self.verticalLayout_14.addWidget(self.frame_59)

        self.frame_87 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(0, 60))
        self.frame_87.setFrameShape(QFrame.NoFrame)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_38.setSpacing(20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.label_59 = QLabel(self.frame_87)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(30, 20))
        self.label_59.setFont(font)
        self.label_59.setStyleSheet(u"color: #d1d3d2;")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_59)

        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(2, 30))
        self.frame_88.setStyleSheet(u"background-color: #1f1f2b;\n"
"border-radius: 0px;")
        self.frame_88.setFrameShape(QFrame.NoFrame)
        self.frame_88.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_88)

        self.label_60 = AvatarLabel(self.frame_87)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(40, 40))
        self.label_60.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_38.addWidget(self.label_60)

        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 35))
        self.frame_89.setFrameShape(QFrame.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_89)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.frame_89)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font7)
        self.label_61.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_23.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_89)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font4)
        self.label_62.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.verticalLayout_23.addWidget(self.label_62)


        self.horizontalLayout_38.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_87)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(2, 30))
        self.frame_90.setStyleSheet(u"background-color: #1f1f2b;\n"
"border-radius: 0px;")
        self.frame_90.setFrameShape(QFrame.NoFrame)
        self.frame_90.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.frame_87)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(100, 0))
        self.frame_91.setMaximumSize(QSize(16777215, 30))
        self.frame_91.setFrameShape(QFrame.NoFrame)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_91)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_91)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font7)
        self.label_63.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_24.addWidget(self.label_63)

        self.frame_99 = QFrame(self.frame_91)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.NoFrame)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_43.setSpacing(6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.frame_99)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(10, 10))
        self.label_75.setMaximumSize(QSize(10, 10))
        self.label_75.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: #a95860;")

        self.horizontalLayout_43.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_99)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font4)
        self.label_76.setStyleSheet(u"border: none;\n"
"color: #d1d3d2;")

        self.horizontalLayout_43.addWidget(self.label_76)


        self.verticalLayout_24.addWidget(self.frame_99)


        self.horizontalLayout_38.addWidget(self.frame_91)


        self.verticalLayout_14.addWidget(self.frame_87)

        self.frame_60 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 60))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 60))
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 60))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_62)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_31)


        self.horizontalLayout_4.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(430, 0))
        self.frame_19.setMaximumSize(QSize(16777215, 16777215))
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_19)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setStyleSheet(u"background-color: #181b20;\n"
"border-radius: 20px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.label = QLabel(self.frame_22)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: #d1d3d2;")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout_6.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_23)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.frame_23)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: #6e6f74;")

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_5.addWidget(self.frame_23, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: #181b20;\n"
"border-radius: 20px;\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_21)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_25 = DonutChart(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 30))
        self.frame_26.setStyleSheet(u"background-color: #202225;\n"
"border-radius: 15px;")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_27)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16, 16))
        self.label_3.setPixmap(QPixmap(u"icons/clock.png"))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_27)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamily(u"Poppins")
        font8.setPointSize(9)
        font8.setBold(False)
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"color: #f11a44;")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_7.addWidget(self.frame_27, 0, Qt.AlignHCenter)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_28)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16, 16))
        self.label_5.setPixmap(QPixmap(u"icons/clock.png"))

        self.horizontalLayout_9.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_28)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: #2a9df0;")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_6)


        self.horizontalLayout_7.addWidget(self.frame_28, 0, Qt.AlignHCenter)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setSpacing(8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_29)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16, 16))
        self.label_7.setPixmap(QPixmap(u"icons/clock.png"))

        self.horizontalLayout_10.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_29)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: #a72cf4;")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_8)


        self.horizontalLayout_7.addWidget(self.frame_29, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_26)


        self.verticalLayout_4.addWidget(self.frame_21)


        self.horizontalLayout_4.addWidget(self.frame_19)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_32.setText("")
        self.label_39.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Projects Status", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"All members", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Managers", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Amanda Lee", None))
        self.label_29.setText("")
        self.label_33.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Eric Hunt", None))
        self.label_35.setText("")
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Arkel Henderson", None))
        self.label_38.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"         Type to search...", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"UI/UX Design", None))
        self.pushButton_7.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Th, Aprill 8, 2021", None))
        self.pushButton_13.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"1 member online", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total: 3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Web Development", None))
        self.pushButton_8.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Mo, April 5, 2021", None))
        self.pushButton_14.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"3 member online", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total: 4", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Mobile Development", None))
        self.pushButton_9.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"We, April 7, 2021", None))
        self.pushButton_15.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"3 member online", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Total: 3", None))
#if QT_CONFIG(accessibility)
        self.frame_8.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Activity status", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"55 percent left", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_26.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Justin Timberlake", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_57.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Works on Web", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_67.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Bebe Rexha", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_73.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Works on Web", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_60.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Stephen Amell", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_75.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"AFK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Overall progress", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"55 percent left", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1 Week left", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"3 Week left", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"2 Week left", None))
    # retranslateUi

