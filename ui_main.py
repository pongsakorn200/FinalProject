# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 702)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 2px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.layout_centralwidget = QtWidgets.QHBoxLayout(self.centralwidget)
        self.layout_centralwidget.setContentsMargins(0, 0, 0, 0)
        self.layout_centralwidget.setSpacing(0)
        self.layout_centralwidget.setObjectName("layout_centralwidget")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("/* LINE EDIT */\n"
"QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(:/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/16x16/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);    \n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.layout_frame_main = QtWidgets.QHBoxLayout(self.frame_main)
        self.layout_frame_main.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_main.setSpacing(0)
        self.layout_frame_main.setObjectName("layout_frame_main")
        self.frame_container_left = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_container_left.sizePolicy().hasHeightForWidth())
        self.frame_container_left.setSizePolicy(sizePolicy)
        self.frame_container_left.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_container_left.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_container_left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_container_left.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_container_left.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame_container_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_container_left.setObjectName("frame_container_left")
        self.layout_frame_container_left = QtWidgets.QVBoxLayout(self.frame_container_left)
        self.layout_frame_container_left.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_container_left.setSpacing(0)
        self.layout_frame_container_left.setObjectName("layout_frame_container_left")
        self.frame_menu = QtWidgets.QFrame(self.frame_container_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_menu.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.layout_frame_menu = QtWidgets.QVBoxLayout(self.frame_menu)
        self.layout_frame_menu.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_menu.setSpacing(0)
        self.layout_frame_menu.setObjectName("layout_frame_menu")
        self.btn_toggle_menu = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setMinimumSize(QtCore.QSize(0, 70))
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/24x24/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_toggle_menu.setIcon(icon)
        self.btn_toggle_menu.setIconSize(QtCore.QSize(24, 24))
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        self.layout_frame_menu.addWidget(self.btn_toggle_menu)
        self.layout_frame_container_left.addWidget(self.frame_menu)
        self.frame_blank = QtWidgets.QFrame(self.frame_container_left)
        self.frame_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blank.setObjectName("frame_blank")
        self.layout_frame_container_left.addWidget(self.frame_blank)
        self.frame_extra_menu = QtWidgets.QFrame(self.frame_container_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menu.sizePolicy().hasHeightForWidth())
        self.frame_extra_menu.setSizePolicy(sizePolicy)
        self.frame_extra_menu.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame_extra_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra_menu.setObjectName("frame_extra_menu")
        self.layout_frame_extra_menu = QtWidgets.QVBoxLayout(self.frame_extra_menu)
        self.layout_frame_extra_menu.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_extra_menu.setSpacing(0)
        self.layout_frame_extra_menu.setObjectName("layout_frame_extra_menu")
        self.layout_frame_container_left.addWidget(self.frame_extra_menu)
        self.layout_frame_main.addWidget(self.frame_container_left)
        self.frame_container_right = QtWidgets.QFrame(self.frame_main)
        self.frame_container_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_container_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_container_right.setObjectName("frame_container_right")
        self.layout_frame_container_right = QtWidgets.QVBoxLayout(self.frame_container_right)
        self.layout_frame_container_right.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_container_right.setSpacing(0)
        self.layout_frame_container_right.setObjectName("layout_frame_container_right")
        self.frame_top = QtWidgets.QFrame(self.frame_container_right)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top.setStyleSheet("background-color: transparent;\n"
"")
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.layout_frame_top = QtWidgets.QVBoxLayout(self.frame_top)
        self.layout_frame_top.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_top.setSpacing(0)
        self.layout_frame_top.setObjectName("layout_frame_top")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.layout_frame_top_btns = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.layout_frame_top_btns.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_top_btns.setSpacing(0)
        self.layout_frame_top_btns.setObjectName("layout_frame_top_btns")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.layout_frame_label_top_btns = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.layout_frame_label_top_btns.setContentsMargins(10, -1, 0, 0)
        self.layout_frame_label_top_btns.setSpacing(0)
        self.layout_frame_label_top_btns.setObjectName("layout_frame_label_top_btns")
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"background-image: url(:/icons/24x24/cil-screen-desktop.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.layout_frame_label_top_btns.addWidget(self.frame_icon_top_bar)
        self.label_title_top_bar = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_top_bar.setFont(font)
        self.label_title_top_bar.setStyleSheet("background: transparent;\n"
"")
        self.label_title_top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_title_top_bar.setObjectName("label_title_top_bar")
        self.layout_frame_label_top_btns.addWidget(self.label_title_top_bar)
        self.layout_frame_top_btns.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.layout_frame_btns_right = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.layout_frame_btns_right.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_btns_right.setSpacing(0)
        self.layout_frame_btns_right.setObjectName("layout_frame_btns_right")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/16x16/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setObjectName("btn_minimize")
        self.layout_frame_btns_right.addWidget(self.btn_minimize)
        self.btn_maximization = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximization.sizePolicy().hasHeightForWidth())
        self.btn_maximization.setSizePolicy(sizePolicy)
        self.btn_maximization.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_maximization.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximization.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximization.setIcon(icon2)
        self.btn_maximization.setObjectName("btn_maximization")
        self.layout_frame_btns_right.addWidget(self.btn_maximization)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setObjectName("btn_close")
        self.layout_frame_btns_right.addWidget(self.btn_close)
        self.layout_frame_top_btns.addWidget(self.frame_btns_right)
        self.layout_frame_top.addWidget(self.frame_top_btns)
        self.frame_top_info = QtWidgets.QFrame(self.frame_top)
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.layout_frame_top_info = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.layout_frame_top_info.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_top_info.setSpacing(0)
        self.layout_frame_top_info.setObjectName("layout_frame_top_info")
        self.label_top_info_1 = QtWidgets.QLabel(self.frame_top_info)
        self.label_top_info_1.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setText("")
        self.label_top_info_1.setObjectName("label_top_info_1")
        self.layout_frame_top_info.addWidget(self.label_top_info_1)
        self.label_top_info_2 = QtWidgets.QLabel(self.frame_top_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_top_info_2.sizePolicy().hasHeightForWidth())
        self.label_top_info_2.setSizePolicy(sizePolicy)
        self.label_top_info_2.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_top_info_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_top_info_2.setObjectName("label_top_info_2")
        self.layout_frame_top_info.addWidget(self.label_top_info_2)
        self.layout_frame_top.addWidget(self.frame_top_info)
        self.layout_frame_container_right.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_container_right)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.layout_frame_center = QtWidgets.QHBoxLayout(self.frame_center)
        self.layout_frame_center.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_center.setSpacing(0)
        self.layout_frame_center.setObjectName("layout_frame_center")
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.layout_frame_content_right = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.layout_frame_content_right.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_content_right.setSpacing(0)
        self.layout_frame_content_right.setObjectName("layout_frame_content_right")
        self.frame_content = QtWidgets.QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.layout_frame_content = QtWidgets.QVBoxLayout(self.frame_content)
        self.layout_frame_content.setContentsMargins(5, 5, 5, 5)
        self.layout_frame_content.setSpacing(0)
        self.layout_frame_content.setObjectName("layout_frame_content")
        self.stackedWidget_menu = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget_menu.setObjectName("stackedWidget_menu")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_home_top = QtWidgets.QFrame(self.page_home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_home_top.sizePolicy().hasHeightForWidth())
        self.frame_home_top.setSizePolicy(sizePolicy)
        self.frame_home_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_home_top.setObjectName("frame_home_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_home_top)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_home_mini_map = QtWidgets.QLabel(self.frame_home_top)
        self.label_home_mini_map.setMinimumSize(QtCore.QSize(250, 0))
        self.label_home_mini_map.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_home_mini_map.setStyleSheet("QLabel{\n"
"    background-color: rgb(218, 218, 218);\n"
"    border-radius: 5px;\n"
"}")
        self.label_home_mini_map.setFrameShape(QtWidgets.QFrame.Box)
        self.label_home_mini_map.setLineWidth(2)
        self.label_home_mini_map.setScaledContents(True)
        self.label_home_mini_map.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home_mini_map.setObjectName("label_home_mini_map")
        self.horizontalLayout.addWidget(self.label_home_mini_map)
        self.label_home_display = QtWidgets.QLabel(self.frame_home_top)
        self.label_home_display.setMinimumSize(QtCore.QSize(645, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_home_display.setFont(font)
        self.label_home_display.setStyleSheet("QLabel{\n"
"    color: rgb(195, 195, 195);\n"
"    background-color: rgb(218, 218, 218);\n"
"    border-radius: 5px;\n"
"}")
        self.label_home_display.setFrameShape(QtWidgets.QFrame.Box)
        self.label_home_display.setLineWidth(2)
        self.label_home_display.setScaledContents(True)
        self.label_home_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home_display.setIndent(-1)
        self.label_home_display.setObjectName("label_home_display")
        self.horizontalLayout.addWidget(self.label_home_display)
        self.verticalLayout.addWidget(self.frame_home_top)
        self.frame_home_bot = QtWidgets.QFrame(self.page_home)
        self.frame_home_bot.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_home_bot.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_home_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_home_bot.setObjectName("frame_home_bot")
        self.layout_frame_home_blank = QtWidgets.QHBoxLayout(self.frame_home_bot)
        self.layout_frame_home_blank.setContentsMargins(5, 0, 5, 0)
        self.layout_frame_home_blank.setSpacing(20)
        self.layout_frame_home_blank.setObjectName("layout_frame_home_blank")
        self.btn_home_end_alert = QtWidgets.QPushButton(self.frame_home_bot)
        self.btn_home_end_alert.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home_end_alert.setFont(font)
        self.btn_home_end_alert.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_home_end_alert.setObjectName("btn_home_end_alert")
        self.layout_frame_home_blank.addWidget(self.btn_home_end_alert)
        self.verticalLayout.addWidget(self.frame_home_bot)
        self.stackedWidget_menu.addWidget(self.page_home)
        self.page_alert_setting = QtWidgets.QWidget()
        self.page_alert_setting.setObjectName("page_alert_setting")
        self.layout_page_alert_setting = QtWidgets.QHBoxLayout(self.page_alert_setting)
        self.layout_page_alert_setting.setContentsMargins(0, 0, 0, 0)
        self.layout_page_alert_setting.setSpacing(0)
        self.layout_page_alert_setting.setObjectName("layout_page_alert_setting")
        self.frame_alert_setting_left = QtWidgets.QFrame(self.page_alert_setting)
        self.frame_alert_setting_left.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_alert_setting_left.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_alert_setting_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_left.setObjectName("frame_alert_setting_left")
        self.layout_frame_alert_setting_left = QtWidgets.QVBoxLayout(self.frame_alert_setting_left)
        self.layout_frame_alert_setting_left.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_alert_setting_left.setSpacing(0)
        self.layout_frame_alert_setting_left.setObjectName("layout_frame_alert_setting_left")
        self.tableWidget_cam_list = QtWidgets.QTableWidget(self.frame_alert_setting_left)
        self.tableWidget_cam_list.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget_cam_list.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_cam_list.setFont(font)
        self.tableWidget_cam_list.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_cam_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_cam_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_cam_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_cam_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_cam_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_cam_list.setObjectName("tableWidget_cam_list")
        self.tableWidget_cam_list.setColumnCount(2)
        self.tableWidget_cam_list.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cam_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cam_list.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_cam_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_cam_list.setHorizontalHeaderItem(1, item)
        self.tableWidget_cam_list.horizontalHeader().setVisible(False)
        self.tableWidget_cam_list.horizontalHeader().setDefaultSectionSize(45)
        self.tableWidget_cam_list.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_cam_list.verticalHeader().setVisible(False)
        self.layout_frame_alert_setting_left.addWidget(self.tableWidget_cam_list)
        self.btn_show_cam = QtWidgets.QPushButton(self.frame_alert_setting_left)
        self.btn_show_cam.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_show_cam.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_show_cam.setFont(font)
        self.btn_show_cam.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_show_cam.setObjectName("btn_show_cam")
        self.layout_frame_alert_setting_left.addWidget(self.btn_show_cam)
        self.layout_page_alert_setting.addWidget(self.frame_alert_setting_left)
        self.frame_alert_setting_right = QtWidgets.QFrame(self.page_alert_setting)
        self.frame_alert_setting_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_right.setObjectName("frame_alert_setting_right")
        self.layout_frame_alert_setting_right = QtWidgets.QVBoxLayout(self.frame_alert_setting_right)
        self.layout_frame_alert_setting_right.setContentsMargins(10, 5, 10, 5)
        self.layout_frame_alert_setting_right.setSpacing(0)
        self.layout_frame_alert_setting_right.setObjectName("layout_frame_alert_setting_right")
        self.label_alert_setting_show_cam = QtWidgets.QLabel(self.frame_alert_setting_right)
        self.label_alert_setting_show_cam.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label_alert_setting_show_cam.setFont(font)
        self.label_alert_setting_show_cam.setStyleSheet("QLabel{\n"
"    color: rgb(195, 195, 195);\n"
"    background-color: rgb(218, 218, 218);\n"
"    border-radius: 5px;\n"
"}")
        self.label_alert_setting_show_cam.setScaledContents(True)
        self.label_alert_setting_show_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.label_alert_setting_show_cam.setObjectName("label_alert_setting_show_cam")
        self.layout_frame_alert_setting_right.addWidget(self.label_alert_setting_show_cam)
        self.frame_alert_setting_cam_info = QtWidgets.QFrame(self.frame_alert_setting_right)
        self.frame_alert_setting_cam_info.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_alert_setting_cam_info.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_alert_setting_cam_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_cam_info.setObjectName("frame_alert_setting_cam_info")
        self.layout_frame_alert_setting_cam_info = QtWidgets.QVBoxLayout(self.frame_alert_setting_cam_info)
        self.layout_frame_alert_setting_cam_info.setContentsMargins(10, 10, 10, 10)
        self.layout_frame_alert_setting_cam_info.setSpacing(0)
        self.layout_frame_alert_setting_cam_info.setObjectName("layout_frame_alert_setting_cam_info")
        self.label_alert_setting_device_name = QtWidgets.QLabel(self.frame_alert_setting_cam_info)
        self.label_alert_setting_device_name.setMinimumSize(QtCore.QSize(300, 30))
        self.label_alert_setting_device_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_alert_setting_device_name.setFont(font)
        self.label_alert_setting_device_name.setObjectName("label_alert_setting_device_name")
        self.layout_frame_alert_setting_cam_info.addWidget(self.label_alert_setting_device_name)
        self.label_alert_setting_device_address = QtWidgets.QLabel(self.frame_alert_setting_cam_info)
        self.label_alert_setting_device_address.setMinimumSize(QtCore.QSize(300, 30))
        self.label_alert_setting_device_address.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_alert_setting_device_address.setFont(font)
        self.label_alert_setting_device_address.setObjectName("label_alert_setting_device_address")
        self.layout_frame_alert_setting_cam_info.addWidget(self.label_alert_setting_device_address)
        self.label_alert_setting_device_description = QtWidgets.QLabel(self.frame_alert_setting_cam_info)
        self.label_alert_setting_device_description.setMinimumSize(QtCore.QSize(300, 30))
        self.label_alert_setting_device_description.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_alert_setting_device_description.setFont(font)
        self.label_alert_setting_device_description.setObjectName("label_alert_setting_device_description")
        self.layout_frame_alert_setting_cam_info.addWidget(self.label_alert_setting_device_description)
        self.frame_alert_setting_notification = QtWidgets.QFrame(self.frame_alert_setting_cam_info)
        self.frame_alert_setting_notification.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_notification.setObjectName("frame_alert_setting_notification")
        self.layout_frame_alert_setting_notification = QtWidgets.QHBoxLayout(self.frame_alert_setting_notification)
        self.layout_frame_alert_setting_notification.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_alert_setting_notification.setSpacing(0)
        self.layout_frame_alert_setting_notification.setObjectName("layout_frame_alert_setting_notification")
        self.label_notification_status = QtWidgets.QLabel(self.frame_alert_setting_notification)
        self.label_notification_status.setMinimumSize(QtCore.QSize(350, 30))
        self.label_notification_status.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_notification_status.setFont(font)
        self.label_notification_status.setObjectName("label_notification_status")
        self.layout_frame_alert_setting_notification.addWidget(self.label_notification_status)
        self.btn_enable_disable_notification = QtWidgets.QPushButton(self.frame_alert_setting_notification)
        self.btn_enable_disable_notification.setMinimumSize(QtCore.QSize(160, 30))
        self.btn_enable_disable_notification.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_enable_disable_notification.setFont(font)
        self.btn_enable_disable_notification.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_enable_disable_notification.setObjectName("btn_enable_disable_notification")
        self.layout_frame_alert_setting_notification.addWidget(self.btn_enable_disable_notification)
        self.frame_alert_setting_blank = QtWidgets.QFrame(self.frame_alert_setting_notification)
        self.frame_alert_setting_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_blank.setObjectName("frame_alert_setting_blank")
        self.layout_frame_alert_setting_notification.addWidget(self.frame_alert_setting_blank)
        self.layout_frame_alert_setting_cam_info.addWidget(self.frame_alert_setting_notification)
        self.frame_alert_setting_notification_2 = QtWidgets.QFrame(self.frame_alert_setting_cam_info)
        self.frame_alert_setting_notification_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_notification_2.setObjectName("frame_alert_setting_notification_2")
        self.layout_frame_alert_setting_notification_2 = QtWidgets.QHBoxLayout(self.frame_alert_setting_notification_2)
        self.layout_frame_alert_setting_notification_2.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_alert_setting_notification_2.setSpacing(0)
        self.layout_frame_alert_setting_notification_2.setObjectName("layout_frame_alert_setting_notification_2")
        self.label_selec_line = QtWidgets.QLabel(self.frame_alert_setting_notification_2)
        self.label_selec_line.setMinimumSize(QtCore.QSize(350, 30))
        self.label_selec_line.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_selec_line.setFont(font)
        self.label_selec_line.setObjectName("label_selec_line")
        self.layout_frame_alert_setting_notification_2.addWidget(self.label_selec_line)
        self.btn_select_line = QtWidgets.QPushButton(self.frame_alert_setting_notification_2)
        self.btn_select_line.setMinimumSize(QtCore.QSize(160, 30))
        self.btn_select_line.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select_line.setFont(font)
        self.btn_select_line.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_select_line.setObjectName("btn_select_line")
        self.layout_frame_alert_setting_notification_2.addWidget(self.btn_select_line)
        self.frame_alert_setting_blank_2 = QtWidgets.QFrame(self.frame_alert_setting_notification_2)
        self.frame_alert_setting_blank_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_blank_2.setObjectName("frame_alert_setting_blank_2")
        self.layout_frame_alert_setting_notification_2.addWidget(self.frame_alert_setting_blank_2)
        self.layout_frame_alert_setting_cam_info.addWidget(self.frame_alert_setting_notification_2)
        self.frame_alert_setting_notification_3 = QtWidgets.QFrame(self.frame_alert_setting_cam_info)
        self.frame_alert_setting_notification_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_alert_setting_notification_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alert_setting_notification_3.setObjectName("frame_alert_setting_notification_3")
        self.layout_frame_alert_setting_notification_3 = QtWidgets.QHBoxLayout(self.frame_alert_setting_notification_3)
        self.layout_frame_alert_setting_notification_3.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_alert_setting_notification_3.setSpacing(0)
        self.layout_frame_alert_setting_notification_3.setObjectName("layout_frame_alert_setting_notification_3")
        self.label_select_line = QtWidgets.QLabel(self.frame_alert_setting_notification_3)
        self.label_select_line.setMinimumSize(QtCore.QSize(500, 25))
        self.label_select_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_select_line.setFont(font)
        self.label_select_line.setText("")
        self.label_select_line.setObjectName("label_select_line")
        self.layout_frame_alert_setting_notification_3.addWidget(self.label_select_line)
        self.layout_frame_alert_setting_cam_info.addWidget(self.frame_alert_setting_notification_3)
        self.layout_frame_alert_setting_right.addWidget(self.frame_alert_setting_cam_info)
        self.layout_page_alert_setting.addWidget(self.frame_alert_setting_right)
        self.stackedWidget_menu.addWidget(self.page_alert_setting)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.layout_page_setting = QtWidgets.QVBoxLayout(self.page_setting)
        self.layout_page_setting.setContentsMargins(0, 0, 0, 0)
        self.layout_page_setting.setSpacing(0)
        self.layout_page_setting.setObjectName("layout_page_setting")
        self.frame_setting_top = QtWidgets.QFrame(self.page_setting)
        self.frame_setting_top.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_setting_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setting_top.setObjectName("frame_setting_top")
        self.layout_frame_setting_top = QtWidgets.QHBoxLayout(self.frame_setting_top)
        self.layout_frame_setting_top.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_setting_top.setSpacing(2)
        self.layout_frame_setting_top.setObjectName("layout_frame_setting_top")
        self.btn_setting_camera = QtWidgets.QPushButton(self.frame_setting_top)
        self.btn_setting_camera.setMinimumSize(QtCore.QSize(110, 45))
        self.btn_setting_camera.setMaximumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_setting_camera.setFont(font)
        self.btn_setting_camera.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_setting_camera.setObjectName("btn_setting_camera")
        self.layout_frame_setting_top.addWidget(self.btn_setting_camera)
        self.btn_setting_line_token = QtWidgets.QPushButton(self.frame_setting_top)
        self.btn_setting_line_token.setMinimumSize(QtCore.QSize(115, 45))
        self.btn_setting_line_token.setMaximumSize(QtCore.QSize(115, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_setting_line_token.setFont(font)
        self.btn_setting_line_token.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_setting_line_token.setObjectName("btn_setting_line_token")
        self.layout_frame_setting_top.addWidget(self.btn_setting_line_token)
        self.btn_setting_address = QtWidgets.QPushButton(self.frame_setting_top)
        self.btn_setting_address.setMinimumSize(QtCore.QSize(120, 45))
        self.btn_setting_address.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_setting_address.setFont(font)
        self.btn_setting_address.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_setting_address.setObjectName("btn_setting_address")
        self.layout_frame_setting_top.addWidget(self.btn_setting_address)
        self.btn_setting_system_info = QtWidgets.QPushButton(self.frame_setting_top)
        self.btn_setting_system_info.setMinimumSize(QtCore.QSize(120, 45))
        self.btn_setting_system_info.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_setting_system_info.setFont(font)
        self.btn_setting_system_info.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_setting_system_info.setObjectName("btn_setting_system_info")
        self.layout_frame_setting_top.addWidget(self.btn_setting_system_info)
        self.frame_blank_setting = QtWidgets.QFrame(self.frame_setting_top)
        self.frame_blank_setting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blank_setting.setObjectName("frame_blank_setting")
        self.layout_frame_setting_top.addWidget(self.frame_blank_setting)
        self.layout_page_setting.addWidget(self.frame_setting_top)
        self.frame_setting_mid = QtWidgets.QFrame(self.page_setting)
        self.frame_setting_mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setting_mid.setObjectName("frame_setting_mid")
        self.layout_frame_setting_mid = QtWidgets.QHBoxLayout(self.frame_setting_mid)
        self.layout_frame_setting_mid.setContentsMargins(0, 10, 0, 10)
        self.layout_frame_setting_mid.setSpacing(0)
        self.layout_frame_setting_mid.setObjectName("layout_frame_setting_mid")
        self.stackedWidget_setting = QtWidgets.QStackedWidget(self.frame_setting_mid)
        self.stackedWidget_setting.setObjectName("stackedWidget_setting")
        self.page_setting_camera = QtWidgets.QWidget()
        self.page_setting_camera.setObjectName("page_setting_camera")
        self.layout_page_setting_camera = QtWidgets.QVBoxLayout(self.page_setting_camera)
        self.layout_page_setting_camera.setContentsMargins(0, 0, 0, 0)
        self.layout_page_setting_camera.setSpacing(0)
        self.layout_page_setting_camera.setObjectName("layout_page_setting_camera")
        self.frame_add_cam = QtWidgets.QFrame(self.page_setting_camera)
        self.frame_add_cam.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_add_cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_cam.setObjectName("frame_add_cam")
        self.layout_frame_add_cam = QtWidgets.QVBoxLayout(self.frame_add_cam)
        self.layout_frame_add_cam.setContentsMargins(0, 0, 0, 0)
        self.layout_frame_add_cam.setSpacing(20)
        self.layout_frame_add_cam.setObjectName("layout_frame_add_cam")
        self.frame_top_add_cam = QtWidgets.QFrame(self.frame_add_cam)
        self.frame_top_add_cam.setMinimumSize(QtCore.QSize(0, 175))
        self.frame_top_add_cam.setMaximumSize(QtCore.QSize(16777215, 175))
        self.frame_top_add_cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_cam.setObjectName("frame_top_add_cam")
        self.layout_frame_top_add_cam = QtWidgets.QVBoxLayout(self.frame_top_add_cam)
        self.layout_frame_top_add_cam.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_top_add_cam.setSpacing(0)
        self.layout_frame_top_add_cam.setObjectName("layout_frame_top_add_cam")
        self.label_top_add_cam = QtWidgets.QLabel(self.frame_top_add_cam)
        self.label_top_add_cam.setEnabled(True)
        self.label_top_add_cam.setMinimumSize(QtCore.QSize(0, 30))
        self.label_top_add_cam.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_add_cam.setFont(font)
        self.label_top_add_cam.setObjectName("label_top_add_cam")
        self.layout_frame_top_add_cam.addWidget(self.label_top_add_cam)
        self.frame_top_add_cam_4 = QtWidgets.QFrame(self.frame_top_add_cam)
        self.frame_top_add_cam_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_cam_4.setObjectName("frame_top_add_cam_4")
        self.layout_frame_top_add_cam_9 = QtWidgets.QHBoxLayout(self.frame_top_add_cam_4)
        self.layout_frame_top_add_cam_9.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_cam_9.setSpacing(10)
        self.layout_frame_top_add_cam_9.setObjectName("layout_frame_top_add_cam_9")
        self.label_add_cam_name = QtWidgets.QLabel(self.frame_top_add_cam_4)
        self.label_add_cam_name.setMinimumSize(QtCore.QSize(85, 0))
        self.label_add_cam_name.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_cam_name.setFont(font)
        self.label_add_cam_name.setObjectName("label_add_cam_name")
        self.layout_frame_top_add_cam_9.addWidget(self.label_add_cam_name)
        self.lineEdit_add_cam_name = QtWidgets.QLineEdit(self.frame_top_add_cam_4)
        self.lineEdit_add_cam_name.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_add_cam_name.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_add_cam_name.setFont(font)
        self.lineEdit_add_cam_name.setObjectName("lineEdit_add_cam_name")
        self.layout_frame_top_add_cam_9.addWidget(self.lineEdit_add_cam_name)
        self.label_add_cam_ip = QtWidgets.QLabel(self.frame_top_add_cam_4)
        self.label_add_cam_ip.setMinimumSize(QtCore.QSize(90, 0))
        self.label_add_cam_ip.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_cam_ip.setFont(font)
        self.label_add_cam_ip.setObjectName("label_add_cam_ip")
        self.layout_frame_top_add_cam_9.addWidget(self.label_add_cam_ip)
        self.lineEdit_add_cam_ip = QtWidgets.QLineEdit(self.frame_top_add_cam_4)
        self.lineEdit_add_cam_ip.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_add_cam_ip.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_add_cam_ip.setFont(font)
        self.lineEdit_add_cam_ip.setText("")
        self.lineEdit_add_cam_ip.setObjectName("lineEdit_add_cam_ip")
        self.layout_frame_top_add_cam_9.addWidget(self.lineEdit_add_cam_ip)
        self.label_add_cam_port = QtWidgets.QLabel(self.frame_top_add_cam_4)
        self.label_add_cam_port.setMinimumSize(QtCore.QSize(50, 0))
        self.label_add_cam_port.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_cam_port.setFont(font)
        self.label_add_cam_port.setObjectName("label_add_cam_port")
        self.layout_frame_top_add_cam_9.addWidget(self.label_add_cam_port)
        self.lineEdit_add_cam_port = QtWidgets.QLineEdit(self.frame_top_add_cam_4)
        self.lineEdit_add_cam_port.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_add_cam_port.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_add_cam_port.setFont(font)
        self.lineEdit_add_cam_port.setObjectName("lineEdit_add_cam_port")
        self.layout_frame_top_add_cam_9.addWidget(self.lineEdit_add_cam_port)
        self.layout_frame_top_add_cam.addWidget(self.frame_top_add_cam_4)
        self.frame_top_add_cam_2 = QtWidgets.QFrame(self.frame_top_add_cam)
        self.frame_top_add_cam_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_cam_2.setObjectName("frame_top_add_cam_2")
        self.layout_frame_top_add_cam_2 = QtWidgets.QHBoxLayout(self.frame_top_add_cam_2)
        self.layout_frame_top_add_cam_2.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_cam_2.setSpacing(10)
        self.layout_frame_top_add_cam_2.setObjectName("layout_frame_top_add_cam_2")
        self.label_add_cam_position = QtWidgets.QLabel(self.frame_top_add_cam_2)
        self.label_add_cam_position.setMinimumSize(QtCore.QSize(85, 0))
        self.label_add_cam_position.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_cam_position.setFont(font)
        self.label_add_cam_position.setObjectName("label_add_cam_position")
        self.layout_frame_top_add_cam_2.addWidget(self.label_add_cam_position)
        self.btn_select_address = QtWidgets.QPushButton(self.frame_top_add_cam_2)
        self.btn_select_address.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_select_address.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select_address.setFont(font)
        self.btn_select_address.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_select_address.setObjectName("btn_select_address")
        self.layout_frame_top_add_cam_2.addWidget(self.btn_select_address)
        self.lineEdit_add_cam_position = QtWidgets.QLineEdit(self.frame_top_add_cam_2)
        self.lineEdit_add_cam_position.setEnabled(False)
        self.lineEdit_add_cam_position.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_add_cam_position.setFont(font)
        self.lineEdit_add_cam_position.setObjectName("lineEdit_add_cam_position")
        self.layout_frame_top_add_cam_2.addWidget(self.lineEdit_add_cam_position)
        self.layout_frame_top_add_cam.addWidget(self.frame_top_add_cam_2)
        self.frame_top_add_cam_3 = QtWidgets.QFrame(self.frame_top_add_cam)
        self.frame_top_add_cam_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_top_add_cam_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_top_add_cam_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_cam_3.setObjectName("frame_top_add_cam_3")
        self.layout_frame_top_add_cam_3 = QtWidgets.QHBoxLayout(self.frame_top_add_cam_3)
        self.layout_frame_top_add_cam_3.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_cam_3.setSpacing(10)
        self.layout_frame_top_add_cam_3.setObjectName("layout_frame_top_add_cam_3")
        self.label_add_cam_username = QtWidgets.QLabel(self.frame_top_add_cam_3)
        self.label_add_cam_username.setMinimumSize(QtCore.QSize(85, 0))
        self.label_add_cam_username.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_cam_username.setFont(font)
        self.label_add_cam_username.setObjectName("label_add_cam_username")
        self.layout_frame_top_add_cam_3.addWidget(self.label_add_cam_username)
        self.lineEdit_add_cam_username = QtWidgets.QLineEdit(self.frame_top_add_cam_3)
        self.lineEdit_add_cam_username.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_add_cam_username.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_add_cam_username.setFont(font)
        self.lineEdit_add_cam_username.setObjectName("lineEdit_add_cam_username")
        self.layout_frame_top_add_cam_3.addWidget(self.lineEdit_add_cam_username)
        self.label_add_cam_password = QtWidgets.QLabel(self.frame_top_add_cam_3)
        self.label_add_cam_password.setMinimumSize(QtCore.QSize(90, 0))
        self.label_add_cam_password.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_cam_password.setFont(font)
        self.label_add_cam_password.setObjectName("label_add_cam_password")
        self.layout_frame_top_add_cam_3.addWidget(self.label_add_cam_password)
        self.lineEdit_add_cam_password = QtWidgets.QLineEdit(self.frame_top_add_cam_3)
        self.lineEdit_add_cam_password.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_add_cam_password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_add_cam_password.setFont(font)
        self.lineEdit_add_cam_password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_add_cam_password.setObjectName("lineEdit_add_cam_password")
        self.layout_frame_top_add_cam_3.addWidget(self.lineEdit_add_cam_password)
        self.btn_add_cam_reset = QtWidgets.QPushButton(self.frame_top_add_cam_3)
        self.btn_add_cam_reset.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_cam_reset.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_cam_reset.setFont(font)
        self.btn_add_cam_reset.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_add_cam_reset.setObjectName("btn_add_cam_reset")
        self.layout_frame_top_add_cam_3.addWidget(self.btn_add_cam_reset)
        self.btn_add_cam = QtWidgets.QPushButton(self.frame_top_add_cam_3)
        self.btn_add_cam.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_cam.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_cam.setFont(font)
        self.btn_add_cam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_add_cam.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_add_cam.setObjectName("btn_add_cam")
        self.layout_frame_top_add_cam_3.addWidget(self.btn_add_cam)
        self.layout_frame_top_add_cam.addWidget(self.frame_top_add_cam_3)
        self.layout_frame_add_cam.addWidget(self.frame_top_add_cam)
        self.frame_bot_cam_added = QtWidgets.QFrame(self.frame_add_cam)
        self.frame_bot_cam_added.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_bot_cam_added.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_bot_cam_added.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot_cam_added.setObjectName("frame_bot_cam_added")
        self.layout_frame_bot_cam_added = QtWidgets.QVBoxLayout(self.frame_bot_cam_added)
        self.layout_frame_bot_cam_added.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_bot_cam_added.setSpacing(0)
        self.layout_frame_bot_cam_added.setObjectName("layout_frame_bot_cam_added")
        self.label_info_device_added = QtWidgets.QLabel(self.frame_bot_cam_added)
        self.label_info_device_added.setMinimumSize(QtCore.QSize(200, 40))
        self.label_info_device_added.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_device_added.setFont(font)
        self.label_info_device_added.setObjectName("label_info_device_added")
        self.layout_frame_bot_cam_added.addWidget(self.label_info_device_added)
        self.tableWidget_device_added = QtWidgets.QTableWidget(self.frame_bot_cam_added)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_device_added.setFont(font)
        self.tableWidget_device_added.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_device_added.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_device_added.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_device_added.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_device_added.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_device_added.setDragEnabled(True)
        self.tableWidget_device_added.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_device_added.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_device_added.setObjectName("tableWidget_device_added")
        self.tableWidget_device_added.setColumnCount(4)
        self.tableWidget_device_added.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_device_added.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_device_added.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_device_added.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_device_added.setHorizontalHeaderItem(3, item)
        self.tableWidget_device_added.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_device_added.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget_device_added.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_device_added.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_device_added.verticalHeader().setVisible(False)
        self.layout_frame_bot_cam_added.addWidget(self.tableWidget_device_added)
        self.frame_confirm_delete_cam = QtWidgets.QFrame(self.frame_bot_cam_added)
        self.frame_confirm_delete_cam.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_confirm_delete_cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_confirm_delete_cam.setObjectName("frame_confirm_delete_cam")
        self.layout_frame_confirm_delete_cam = QtWidgets.QHBoxLayout(self.frame_confirm_delete_cam)
        self.layout_frame_confirm_delete_cam.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_confirm_delete_cam.setSpacing(10)
        self.layout_frame_confirm_delete_cam.setObjectName("layout_frame_confirm_delete_cam")
        self.frame_add_cam_blank = QtWidgets.QFrame(self.frame_confirm_delete_cam)
        self.frame_add_cam_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_cam_blank.setObjectName("frame_add_cam_blank")
        self.layout_frame_confirm_delete_cam.addWidget(self.frame_add_cam_blank)
        self.btn_edit_cam = QtWidgets.QPushButton(self.frame_confirm_delete_cam)
        self.btn_edit_cam.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_edit_cam.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit_cam.setFont(font)
        self.btn_edit_cam.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_edit_cam.setObjectName("btn_edit_cam")
        self.layout_frame_confirm_delete_cam.addWidget(self.btn_edit_cam)
        self.btn_delete_cam = QtWidgets.QPushButton(self.frame_confirm_delete_cam)
        self.btn_delete_cam.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_delete_cam.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete_cam.setFont(font)
        self.btn_delete_cam.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_delete_cam.setObjectName("btn_delete_cam")
        self.layout_frame_confirm_delete_cam.addWidget(self.btn_delete_cam)
        self.layout_frame_bot_cam_added.addWidget(self.frame_confirm_delete_cam)
        self.layout_frame_add_cam.addWidget(self.frame_bot_cam_added)
        self.layout_page_setting_camera.addWidget(self.frame_add_cam)
        self.stackedWidget_setting.addWidget(self.page_setting_camera)
        self.page_setting_line_token = QtWidgets.QWidget()
        self.page_setting_line_token.setObjectName("page_setting_line_token")
        self.layout_page_setting_line_token = QtWidgets.QVBoxLayout(self.page_setting_line_token)
        self.layout_page_setting_line_token.setContentsMargins(0, 0, 0, 0)
        self.layout_page_setting_line_token.setSpacing(0)
        self.layout_page_setting_line_token.setObjectName("layout_page_setting_line_token")
        self.frame_add_token = QtWidgets.QFrame(self.page_setting_line_token)
        self.frame_add_token.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_token.setObjectName("frame_add_token")
        self.layout_fram_add_token = QtWidgets.QVBoxLayout(self.frame_add_token)
        self.layout_fram_add_token.setContentsMargins(0, 0, 0, 0)
        self.layout_fram_add_token.setSpacing(0)
        self.layout_fram_add_token.setObjectName("layout_fram_add_token")
        self.frame_top_add_token = QtWidgets.QFrame(self.frame_add_token)
        self.frame_top_add_token.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_top_add_token.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_top_add_token.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_token.setObjectName("frame_top_add_token")
        self.layout_frame_top_add_token = QtWidgets.QVBoxLayout(self.frame_top_add_token)
        self.layout_frame_top_add_token.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_top_add_token.setSpacing(10)
        self.layout_frame_top_add_token.setObjectName("layout_frame_top_add_token")
        self.label_top_add_token = QtWidgets.QLabel(self.frame_top_add_token)
        self.label_top_add_token.setMinimumSize(QtCore.QSize(0, 30))
        self.label_top_add_token.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_add_token.setFont(font)
        self.label_top_add_token.setObjectName("label_top_add_token")
        self.layout_frame_top_add_token.addWidget(self.label_top_add_token)
        self.frame_top_add_token_2 = QtWidgets.QFrame(self.frame_top_add_token)
        self.frame_top_add_token_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_token_2.setObjectName("frame_top_add_token_2")
        self.layout_frame_top_add_token_2 = QtWidgets.QHBoxLayout(self.frame_top_add_token_2)
        self.layout_frame_top_add_token_2.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_token_2.setSpacing(10)
        self.layout_frame_top_add_token_2.setObjectName("layout_frame_top_add_token_2")
        self.label_token_name = QtWidgets.QLabel(self.frame_top_add_token_2)
        self.label_token_name.setMinimumSize(QtCore.QSize(85, 0))
        self.label_token_name.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_token_name.setFont(font)
        self.label_token_name.setObjectName("label_token_name")
        self.layout_frame_top_add_token_2.addWidget(self.label_token_name)
        self.lineEdit_token_name = QtWidgets.QLineEdit(self.frame_top_add_token_2)
        self.lineEdit_token_name.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_token_name.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_token_name.setFont(font)
        self.lineEdit_token_name.setObjectName("lineEdit_token_name")
        self.layout_frame_top_add_token_2.addWidget(self.lineEdit_token_name)
        self.label_token_address = QtWidgets.QLabel(self.frame_top_add_token_2)
        self.label_token_address.setMinimumSize(QtCore.QSize(90, 0))
        self.label_token_address.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_token_address.setFont(font)
        self.label_token_address.setObjectName("label_token_address")
        self.layout_frame_top_add_token_2.addWidget(self.label_token_address)
        self.lineEdit_token_address = QtWidgets.QLineEdit(self.frame_top_add_token_2)
        self.lineEdit_token_address.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_token_address.setFont(font)
        self.lineEdit_token_address.setObjectName("lineEdit_token_address")
        self.layout_frame_top_add_token_2.addWidget(self.lineEdit_token_address)
        self.layout_frame_top_add_token.addWidget(self.frame_top_add_token_2)
        self.frame_top_add_token_3 = QtWidgets.QFrame(self.frame_top_add_token)
        self.frame_top_add_token_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_top_add_token_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_top_add_token_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_token_3.setObjectName("frame_top_add_token_3")
        self.layout_frame_top_add_token_3 = QtWidgets.QHBoxLayout(self.frame_top_add_token_3)
        self.layout_frame_top_add_token_3.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_token_3.setSpacing(10)
        self.layout_frame_top_add_token_3.setObjectName("layout_frame_top_add_token_3")
        self.frame_top_add_token_blank = QtWidgets.QFrame(self.frame_top_add_token_3)
        self.frame_top_add_token_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_token_blank.setObjectName("frame_top_add_token_blank")
        self.layout_frame_top_add_token_3.addWidget(self.frame_top_add_token_blank)
        self.btn_add_token_reset = QtWidgets.QPushButton(self.frame_top_add_token_3)
        self.btn_add_token_reset.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_token_reset.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_token_reset.setFont(font)
        self.btn_add_token_reset.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_add_token_reset.setObjectName("btn_add_token_reset")
        self.layout_frame_top_add_token_3.addWidget(self.btn_add_token_reset)
        self.btn_add_token = QtWidgets.QPushButton(self.frame_top_add_token_3)
        self.btn_add_token.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_token.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_token.setFont(font)
        self.btn_add_token.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_add_token.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_add_token.setObjectName("btn_add_token")
        self.layout_frame_top_add_token_3.addWidget(self.btn_add_token)
        self.layout_frame_top_add_token.addWidget(self.frame_top_add_token_3)
        self.layout_fram_add_token.addWidget(self.frame_top_add_token)
        self.frame_bot_token_added = QtWidgets.QFrame(self.frame_add_token)
        self.frame_bot_token_added.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_bot_token_added.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_bot_token_added.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot_token_added.setObjectName("frame_bot_token_added")
        self.layout_frame_bot_token_added = QtWidgets.QVBoxLayout(self.frame_bot_token_added)
        self.layout_frame_bot_token_added.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_bot_token_added.setSpacing(0)
        self.layout_frame_bot_token_added.setObjectName("layout_frame_bot_token_added")
        self.label_toke_added = QtWidgets.QLabel(self.frame_bot_token_added)
        self.label_toke_added.setMinimumSize(QtCore.QSize(200, 40))
        self.label_toke_added.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_toke_added.setFont(font)
        self.label_toke_added.setObjectName("label_toke_added")
        self.layout_frame_bot_token_added.addWidget(self.label_toke_added)
        self.tableWidget_token_added = QtWidgets.QTableWidget(self.frame_bot_token_added)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_token_added.setFont(font)
        self.tableWidget_token_added.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_token_added.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_token_added.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_token_added.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_token_added.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_token_added.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_token_added.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_token_added.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_token_added.setRowCount(0)
        self.tableWidget_token_added.setObjectName("tableWidget_token_added")
        self.tableWidget_token_added.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_token_added.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_token_added.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_token_added.setHorizontalHeaderItem(2, item)
        self.tableWidget_token_added.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_token_added.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget_token_added.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_token_added.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_token_added.verticalHeader().setVisible(False)
        self.tableWidget_token_added.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_token_added.verticalHeader().setHighlightSections(False)
        self.tableWidget_token_added.verticalHeader().setMinimumSectionSize(23)
        self.layout_frame_bot_token_added.addWidget(self.tableWidget_token_added)
        self.frame_delete_token = QtWidgets.QFrame(self.frame_bot_token_added)
        self.frame_delete_token.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_delete_token.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_delete_token.setObjectName("frame_delete_token")
        self.layout_frame_delete_token = QtWidgets.QHBoxLayout(self.frame_delete_token)
        self.layout_frame_delete_token.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_delete_token.setSpacing(10)
        self.layout_frame_delete_token.setObjectName("layout_frame_delete_token")
        self.frame_add_token_blank = QtWidgets.QFrame(self.frame_delete_token)
        self.frame_add_token_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_token_blank.setObjectName("frame_add_token_blank")
        self.layout_frame_delete_token.addWidget(self.frame_add_token_blank)
        self.btn_edit_token = QtWidgets.QPushButton(self.frame_delete_token)
        self.btn_edit_token.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_edit_token.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit_token.setFont(font)
        self.btn_edit_token.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_edit_token.setObjectName("btn_edit_token")
        self.layout_frame_delete_token.addWidget(self.btn_edit_token)
        self.btn_delete_token = QtWidgets.QPushButton(self.frame_delete_token)
        self.btn_delete_token.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_delete_token.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete_token.setFont(font)
        self.btn_delete_token.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_delete_token.setObjectName("btn_delete_token")
        self.layout_frame_delete_token.addWidget(self.btn_delete_token)
        self.layout_frame_bot_token_added.addWidget(self.frame_delete_token)
        self.layout_fram_add_token.addWidget(self.frame_bot_token_added)
        self.layout_page_setting_line_token.addWidget(self.frame_add_token)
        self.stackedWidget_setting.addWidget(self.page_setting_line_token)
        self.page_setting_address = QtWidgets.QWidget()
        self.page_setting_address.setObjectName("page_setting_address")
        self.layout_page_setting_address = QtWidgets.QVBoxLayout(self.page_setting_address)
        self.layout_page_setting_address.setContentsMargins(0, 0, 0, 0)
        self.layout_page_setting_address.setSpacing(0)
        self.layout_page_setting_address.setObjectName("layout_page_setting_address")
        self.frame_top_add_address = QtWidgets.QFrame(self.page_setting_address)
        self.frame_top_add_address.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_top_add_address.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_top_add_address.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_address.setObjectName("frame_top_add_address")
        self.layout_frame_top_add_token_4 = QtWidgets.QVBoxLayout(self.frame_top_add_address)
        self.layout_frame_top_add_token_4.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_top_add_token_4.setSpacing(10)
        self.layout_frame_top_add_token_4.setObjectName("layout_frame_top_add_token_4")
        self.label_top_add_address = QtWidgets.QLabel(self.frame_top_add_address)
        self.label_top_add_address.setMinimumSize(QtCore.QSize(0, 30))
        self.label_top_add_address.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_add_address.setFont(font)
        self.label_top_add_address.setObjectName("label_top_add_address")
        self.layout_frame_top_add_token_4.addWidget(self.label_top_add_address)
        self.frame_top_add_address_2 = QtWidgets.QFrame(self.frame_top_add_address)
        self.frame_top_add_address_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_address_2.setObjectName("frame_top_add_address_2")
        self.layout_frame_top_add_token_5 = QtWidgets.QHBoxLayout(self.frame_top_add_address_2)
        self.layout_frame_top_add_token_5.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_token_5.setSpacing(10)
        self.layout_frame_top_add_token_5.setObjectName("layout_frame_top_add_token_5")
        self.label_address_position = QtWidgets.QLabel(self.frame_top_add_address_2)
        self.label_address_position.setMinimumSize(QtCore.QSize(85, 0))
        self.label_address_position.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_address_position.setFont(font)
        self.label_address_position.setObjectName("label_address_position")
        self.layout_frame_top_add_token_5.addWidget(self.label_address_position)
        self.lineEdit_address_position = QtWidgets.QLineEdit(self.frame_top_add_address_2)
        self.lineEdit_address_position.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_address_position.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_address_position.setFont(font)
        self.lineEdit_address_position.setObjectName("lineEdit_address_position")
        self.layout_frame_top_add_token_5.addWidget(self.lineEdit_address_position)
        self.label_address_info = QtWidgets.QLabel(self.frame_top_add_address_2)
        self.label_address_info.setMinimumSize(QtCore.QSize(90, 0))
        self.label_address_info.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_address_info.setFont(font)
        self.label_address_info.setObjectName("label_address_info")
        self.layout_frame_top_add_token_5.addWidget(self.label_address_info)
        self.lineEdit_address_info = QtWidgets.QLineEdit(self.frame_top_add_address_2)
        self.lineEdit_address_info.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_address_info.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_address_info.setFont(font)
        self.lineEdit_address_info.setObjectName("lineEdit_address_info")
        self.layout_frame_top_add_token_5.addWidget(self.lineEdit_address_info)
        self.label_address_ip = QtWidgets.QLabel(self.frame_top_add_address_2)
        self.label_address_ip.setMinimumSize(QtCore.QSize(29, 0))
        self.label_address_ip.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_address_ip.setFont(font)
        self.label_address_ip.setObjectName("label_address_ip")
        self.layout_frame_top_add_token_5.addWidget(self.label_address_ip)
        self.lineEdit_address_ip = QtWidgets.QLineEdit(self.frame_top_add_address_2)
        self.lineEdit_address_ip.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_address_ip.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_address_ip.setFont(font)
        self.lineEdit_address_ip.setObjectName("lineEdit_address_ip")
        self.layout_frame_top_add_token_5.addWidget(self.lineEdit_address_ip)
        self.layout_frame_top_add_token_4.addWidget(self.frame_top_add_address_2)
        self.frame_top_add_address_3 = QtWidgets.QFrame(self.frame_top_add_address)
        self.frame_top_add_address_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_top_add_address_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_top_add_address_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_address_3.setObjectName("frame_top_add_address_3")
        self.layout_frame_top_add_token_6 = QtWidgets.QHBoxLayout(self.frame_top_add_address_3)
        self.layout_frame_top_add_token_6.setContentsMargins(15, 0, 0, 0)
        self.layout_frame_top_add_token_6.setSpacing(10)
        self.layout_frame_top_add_token_6.setObjectName("layout_frame_top_add_token_6")
        self.label_position_warning = QtWidgets.QLabel(self.frame_top_add_address_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_position_warning.setFont(font)
        self.label_position_warning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_position_warning.setObjectName("label_position_warning")
        self.layout_frame_top_add_token_6.addWidget(self.label_position_warning)
        self.frame_top_add_address_blank = QtWidgets.QFrame(self.frame_top_add_address_3)
        self.frame_top_add_address_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_add_address_blank.setObjectName("frame_top_add_address_blank")
        self.layout_frame_top_add_token_6.addWidget(self.frame_top_add_address_blank)
        self.btn_add_address_reset = QtWidgets.QPushButton(self.frame_top_add_address_3)
        self.btn_add_address_reset.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_address_reset.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_address_reset.setFont(font)
        self.btn_add_address_reset.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_add_address_reset.setObjectName("btn_add_address_reset")
        self.layout_frame_top_add_token_6.addWidget(self.btn_add_address_reset)
        self.btn_add_address = QtWidgets.QPushButton(self.frame_top_add_address_3)
        self.btn_add_address.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_address.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_address.setFont(font)
        self.btn_add_address.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_add_address.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_add_address.setObjectName("btn_add_address")
        self.layout_frame_top_add_token_6.addWidget(self.btn_add_address)
        self.layout_frame_top_add_token_4.addWidget(self.frame_top_add_address_3)
        self.layout_page_setting_address.addWidget(self.frame_top_add_address)
        self.frame_bot_address_added = QtWidgets.QFrame(self.page_setting_address)
        self.frame_bot_address_added.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_bot_address_added.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_bot_address_added.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot_address_added.setObjectName("frame_bot_address_added")
        self.layout_frame_bot_token_added_2 = QtWidgets.QVBoxLayout(self.frame_bot_address_added)
        self.layout_frame_bot_token_added_2.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_bot_token_added_2.setSpacing(0)
        self.layout_frame_bot_token_added_2.setObjectName("layout_frame_bot_token_added_2")
        self.label_address_added = QtWidgets.QLabel(self.frame_bot_address_added)
        self.label_address_added.setMinimumSize(QtCore.QSize(200, 40))
        self.label_address_added.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_address_added.setFont(font)
        self.label_address_added.setObjectName("label_address_added")
        self.layout_frame_bot_token_added_2.addWidget(self.label_address_added)
        self.tableWidget_address_added = QtWidgets.QTableWidget(self.frame_bot_address_added)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_address_added.setFont(font)
        self.tableWidget_address_added.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_address_added.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_address_added.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_address_added.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_address_added.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_address_added.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_address_added.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_address_added.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_address_added.setRowCount(0)
        self.tableWidget_address_added.setObjectName("tableWidget_address_added")
        self.tableWidget_address_added.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_address_added.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_address_added.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_address_added.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_address_added.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_address_added.setHorizontalHeaderItem(4, item)
        self.tableWidget_address_added.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_address_added.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget_address_added.horizontalHeader().setHighlightSections(True)
        self.tableWidget_address_added.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_address_added.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_address_added.verticalHeader().setVisible(False)
        self.tableWidget_address_added.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_address_added.verticalHeader().setHighlightSections(False)
        self.tableWidget_address_added.verticalHeader().setMinimumSectionSize(23)
        self.layout_frame_bot_token_added_2.addWidget(self.tableWidget_address_added)
        self.frame_delete_address = QtWidgets.QFrame(self.frame_bot_address_added)
        self.frame_delete_address.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_delete_address.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_delete_address.setObjectName("frame_delete_address")
        self.layout_frame_delete_token_2 = QtWidgets.QHBoxLayout(self.frame_delete_address)
        self.layout_frame_delete_token_2.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_delete_token_2.setSpacing(10)
        self.layout_frame_delete_token_2.setObjectName("layout_frame_delete_token_2")
        self.frame_add_address_blank = QtWidgets.QFrame(self.frame_delete_address)
        self.frame_add_address_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_address_blank.setObjectName("frame_add_address_blank")
        self.layout_frame_delete_token_2.addWidget(self.frame_add_address_blank)
        self.btn_edit_address = QtWidgets.QPushButton(self.frame_delete_address)
        self.btn_edit_address.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_edit_address.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit_address.setFont(font)
        self.btn_edit_address.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_edit_address.setObjectName("btn_edit_address")
        self.layout_frame_delete_token_2.addWidget(self.btn_edit_address)
        self.btn_delete_address = QtWidgets.QPushButton(self.frame_delete_address)
        self.btn_delete_address.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_delete_address.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete_address.setFont(font)
        self.btn_delete_address.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_delete_address.setObjectName("btn_delete_address")
        self.layout_frame_delete_token_2.addWidget(self.btn_delete_address)
        self.layout_frame_bot_token_added_2.addWidget(self.frame_delete_address)
        self.layout_page_setting_address.addWidget(self.frame_bot_address_added)
        self.stackedWidget_setting.addWidget(self.page_setting_address)
        self.page_setting_system_info = QtWidgets.QWidget()
        self.page_setting_system_info.setObjectName("page_setting_system_info")
        self.layout_page_setting_system_info = QtWidgets.QVBoxLayout(self.page_setting_system_info)
        self.layout_page_setting_system_info.setContentsMargins(0, 0, 0, 0)
        self.layout_page_setting_system_info.setSpacing(0)
        self.layout_page_setting_system_info.setObjectName("layout_page_setting_system_info")
        self.label_system_info = QtWidgets.QLabel(self.page_setting_system_info)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_system_info.setFont(font)
        self.label_system_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_system_info.setLineWidth(0)
        self.label_system_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_system_info.setObjectName("label_system_info")
        self.layout_page_setting_system_info.addWidget(self.label_system_info)
        self.stackedWidget_setting.addWidget(self.page_setting_system_info)
        self.layout_frame_setting_mid.addWidget(self.stackedWidget_setting)
        self.layout_page_setting.addWidget(self.frame_setting_mid)
        self.frame_setting_bot = QtWidgets.QFrame(self.page_setting)
        self.frame_setting_bot.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_setting_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setting_bot.setObjectName("frame_setting_bot")
        self.layout_frame_setting_bot = QtWidgets.QHBoxLayout(self.frame_setting_bot)
        self.layout_frame_setting_bot.setContentsMargins(20, 0, 20, 0)
        self.layout_frame_setting_bot.setSpacing(20)
        self.layout_frame_setting_bot.setObjectName("layout_frame_setting_bot")
        self.frame_setting_blank_4 = QtWidgets.QFrame(self.frame_setting_bot)
        self.frame_setting_blank_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setting_blank_4.setObjectName("frame_setting_blank_4")
        self.layout_frame_setting_bot.addWidget(self.frame_setting_blank_4)
        self.btn_setting_save = QtWidgets.QPushButton(self.frame_setting_bot)
        self.btn_setting_save.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_setting_save.setFont(font)
        self.btn_setting_save.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_setting_save.setObjectName("btn_setting_save")
        self.layout_frame_setting_bot.addWidget(self.btn_setting_save)
        self.layout_page_setting.addWidget(self.frame_setting_bot)
        self.stackedWidget_menu.addWidget(self.page_setting)
        self.layout_frame_content.addWidget(self.stackedWidget_menu)
        self.layout_frame_content_right.addWidget(self.frame_content)
        self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.layout_frame_grip = QtWidgets.QHBoxLayout(self.frame_grip)
        self.layout_frame_grip.setContentsMargins(0, 0, 2, 0)
        self.layout_frame_grip.setSpacing(0)
        self.layout_frame_grip.setObjectName("layout_frame_grip")
        self.frame_lebel_version = QtWidgets.QFrame(self.frame_grip)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_lebel_version.setFont(font)
        self.frame_lebel_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.frame_lebel_version.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lebel_version.setObjectName("frame_lebel_version")
        self.layout_frame_lebel_version = QtWidgets.QHBoxLayout(self.frame_lebel_version)
        self.layout_frame_lebel_version.setContentsMargins(10, 0, 10, 0)
        self.layout_frame_lebel_version.setSpacing(0)
        self.layout_frame_lebel_version.setObjectName("layout_frame_lebel_version")
        self.label_bot_count = QtWidgets.QLabel(self.frame_lebel_version)
        self.label_bot_count.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_bot_count.setFont(font)
        self.label_bot_count.setText("")
        self.label_bot_count.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_bot_count.setObjectName("label_bot_count")
        self.layout_frame_lebel_version.addWidget(self.label_bot_count)
        self.label_top_info_3 = QtWidgets.QLabel(self.frame_lebel_version)
        self.label_top_info_3.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_top_info_3.setFont(font)
        self.label_top_info_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_top_info_3.setObjectName("label_top_info_3")
        self.layout_frame_lebel_version.addWidget(self.label_top_info_3)
        self.label_version = QtWidgets.QLabel(self.frame_lebel_version)
        self.label_version.setMinimumSize(QtCore.QSize(0, 0))
        self.label_version.setMaximumSize(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_version.setFont(font)
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.layout_frame_lebel_version.addWidget(self.label_version)
        self.layout_frame_grip.addWidget(self.frame_lebel_version)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
"    background-image: url(:/icons/16x16/cil-size-grip.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.layout_frame_grip.addWidget(self.frame_size_grip)
        self.layout_frame_content_right.addWidget(self.frame_grip)
        self.layout_frame_center.addWidget(self.frame_content_right)
        self.layout_frame_container_right.addWidget(self.frame_center)
        self.layout_frame_main.addWidget(self.frame_container_right)
        self.layout_centralwidget.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_menu.setCurrentIndex(2)
        self.stackedWidget_setting.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_toggle_menu.setToolTip(_translate("MainWindow", "Menu"))
        self.label_title_top_bar.setText(_translate("MainWindow", "IT 71"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximization.setToolTip(_translate("MainWindow", "Maximization"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label_top_info_2.setText(_translate("MainWindow", "| HOME"))
        self.label_home_display.setText(_translate("MainWindow", "Waiting for incoming dectection."))
        self.btn_home_end_alert.setText(_translate("MainWindow", "End Alert"))
        item = self.tableWidget_cam_list.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_cam_list.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_cam_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No."))
        item = self.tableWidget_cam_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Device name"))
        self.btn_show_cam.setText(_translate("MainWindow", "Show "))
        self.label_alert_setting_show_cam.setText(_translate("MainWindow", "Select your device."))
        self.label_alert_setting_device_name.setText(_translate("MainWindow", "Name : "))
        self.label_alert_setting_device_address.setText(_translate("MainWindow", "Address : "))
        self.label_alert_setting_device_description.setText(_translate("MainWindow", "Position : "))
        self.label_notification_status.setText(_translate("MainWindow", "Notification Status : "))
        self.btn_enable_disable_notification.setText(_translate("MainWindow", "Enable / Disable"))
        self.label_selec_line.setText(_translate("MainWindow", "Select Line to alert :"))
        self.btn_select_line.setText(_translate("MainWindow", "Select"))
        self.btn_setting_camera.setText(_translate("MainWindow", "IP Camera"))
        self.btn_setting_line_token.setText(_translate("MainWindow", "Line Token"))
        self.btn_setting_address.setText(_translate("MainWindow", "Address"))
        self.btn_setting_system_info.setText(_translate("MainWindow", "System info"))
        self.label_top_add_cam.setText(_translate("MainWindow", "Add Device :"))
        self.label_add_cam_name.setText(_translate("MainWindow", "Name"))
        self.lineEdit_add_cam_name.setPlaceholderText(_translate("MainWindow", "Home 1"))
        self.label_add_cam_ip.setText(_translate("MainWindow", "IP Address"))
        self.lineEdit_add_cam_ip.setPlaceholderText(_translate("MainWindow", "192.168.0.237"))
        self.label_add_cam_port.setText(_translate("MainWindow", "Port"))
        self.lineEdit_add_cam_port.setPlaceholderText(_translate("MainWindow", "8090"))
        self.label_add_cam_position.setText(_translate("MainWindow", "Address"))
        self.btn_select_address.setText(_translate("MainWindow", "Select"))
        self.lineEdit_add_cam_position.setPlaceholderText(_translate("MainWindow", "ช่องแสดงบ้านเลขที่ โดยเพิ่มข้อมูลในหัวข้อ Address ก่อนถึงจะเลือกได้"))
        self.label_add_cam_username.setText(_translate("MainWindow", "Username"))
        self.lineEdit_add_cam_username.setPlaceholderText(_translate("MainWindow", "admin"))
        self.label_add_cam_password.setText(_translate("MainWindow", "Password"))
        self.lineEdit_add_cam_password.setPlaceholderText(_translate("MainWindow", "888888"))
        self.btn_add_cam_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_add_cam.setText(_translate("MainWindow", "Add"))
        self.label_info_device_added.setText(_translate("MainWindow", "Devices added :"))
        item = self.tableWidget_device_added.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No."))
        item = self.tableWidget_device_added.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_device_added.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableWidget_device_added.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.btn_edit_cam.setText(_translate("MainWindow", "Edit selected device"))
        self.btn_delete_cam.setText(_translate("MainWindow", "Delete selected device"))
        self.label_top_add_token.setText(_translate("MainWindow", "Add line token :"))
        self.label_token_name.setText(_translate("MainWindow", "Name"))
        self.lineEdit_token_name.setPlaceholderText(_translate("MainWindow", "Group Alert 1"))
        self.label_token_address.setText(_translate("MainWindow", "Token"))
        self.lineEdit_token_address.setPlaceholderText(_translate("MainWindow", "zNNUzZVu5ysu6GvcWqljXJ1SvOpmePWtqorx5QeoutK"))
        self.btn_add_token_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_add_token.setText(_translate("MainWindow", "Add"))
        self.label_toke_added.setText(_translate("MainWindow", "Tokens added :"))
        item = self.tableWidget_token_added.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No."))
        item = self.tableWidget_token_added.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_token_added.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Token"))
        self.btn_edit_token.setText(_translate("MainWindow", "Edit selected token"))
        self.btn_delete_token.setText(_translate("MainWindow", "Delete selected token"))
        self.label_top_add_address.setText(_translate("MainWindow", "Add address :"))
        self.label_address_position.setText(_translate("MainWindow", "Position"))
        self.lineEdit_address_position.setPlaceholderText(_translate("MainWindow", "POSITION_1"))
        self.label_address_info.setText(_translate("MainWindow", "Address"))
        self.lineEdit_address_info.setPlaceholderText(_translate("MainWindow", "บ้านเลขที่ 123/1"))
        self.label_address_ip.setText(_translate("MainWindow", "IP"))
        self.lineEdit_address_ip.setPlaceholderText(_translate("MainWindow", "192.168.0.202"))
        self.label_position_warning.setText(_translate("MainWindow", "* หมายเหตุ : เพิ่มข้อมูลโดยพิมพ์ POSITION_ ตามด้วยลำดับตัวเลขที่ต้องการ"))
        self.btn_add_address_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_add_address.setText(_translate("MainWindow", "Add"))
        self.label_address_added.setText(_translate("MainWindow", "Address added :"))
        item = self.tableWidget_address_added.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No."))
        item = self.tableWidget_address_added.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Position"))
        item = self.tableWidget_address_added.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_address_added.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableWidget_address_added.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.btn_edit_address.setText(_translate("MainWindow", "Edit selected address"))
        self.btn_delete_address.setText(_translate("MainWindow", "Delete selected address"))
        self.label_system_info.setText(_translate("MainWindow", " Name : โปรแกรมตรวจจับการบุกรุกบริเวณรั้ว \n"
" Version : 1.9.4 \n"
" จัดทำโดยกลุ่ม : IT 71"))
        self.btn_setting_save.setText(_translate("MainWindow", "Save"))
        self.label_top_info_3.setText(_translate("MainWindow", "2020:12:9 18:00:00 น."))
        self.label_version.setText(_translate("MainWindow", "V.1.9.4"))

import Content.icons.icons_rc
