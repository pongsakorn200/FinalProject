# Import modules

import urllib.request
import urllib.parse
import requests
import json
import logging
import sys
import platform
import cv2
import os
import glob
import math
import argparse
import os.path
import numpy as np
import time
import random
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QTimer, QThread, pyqtSignal, QThreadPool
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QImage, QMovie
from PyQt5.QtWidgets import *

# GUI FILE
from app_modules import *

from paho.mqtt import client as mqtt_client
from SqliteHelper import *
import RPi.GPIO as GPIO

conn = SqliteHelper("Content/database/database.db")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#GPIO27 : ResetButton Pin : input
GPIO.setup(13, GPIO.IN)
#GPIO24 : Relay Pin : output
GPIO.setup(18, GPIO.OUT)
#GPIO27 : Led Pin : output
GPIO.setup(29, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
GPIO.output(29, GPIO.LOW)         

class CheckStatus(QThread):
    def __init__(self):
        QThread.__init__(self)
        
    def run(self):
        conn = sqlite3.connect("Content/database/database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT devices.ip,devices.name,position.ip,position.position FROM devices INNER JOIN position ON devices.name=position.device_name")
        ViewData = cursor.fetchall()
        
        while True:
            timecheck = self.showTime()
            if int(timecheck) % 300 == 0:
                for data in ViewData:
                    ping = self.check_ping(str(data[0]))
                    print(data[1] + ": IP: " + data[0] + " is " + ping)
                    pings = self.check_ping(str(data[2]))
                    print(data[3] + ": IP: " + data[2] + " is " + pings)
            time.sleep(0.1)
            
    def check_ping(self, hostname):
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            pingstatus = "Online"
        else:
            pingstatus = "Offline"
        return pingstatus

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('ss')
        return timeDisplay
        

class ButtonBox(QThread):
    def __init__(self):
        QThread.__init__(self)
        
    def run(self):
        while True:
            self.check_button_box()
            time.sleep(0.1)                
        
    def check_button_box(self):
        if GPIO.input(13) :
                GPIO.output(18,GPIO.LOW)
                MainWindow.resetHomeScreen()
        else:
                GPIO.output(18,GPIO.HIGH)

class GetPosition(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):

        broker = '192.168.0.201'
        port = 1883
        topic = "alert/position"

        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{random.randint(0, 100)}'

        def connect_mqtt() -> mqtt_client:
            def on_connect(client, userdata, flags, rc):
                if rc == 0:
                    print("Connected to MQTT Broker!")
                else:
                    print("Failed to connect, return code %d\n", rc)

            client = mqtt_client.Client(client_id)
            client.username_pw_set('IT71_mosquitto', 'it71_password')
            client.on_connect = on_connect
            client.connect(broker, port)
            return client

        def subscribe(client: mqtt_client):
               
            def __show__detect__(position):
                MainWindow.showDetect(position)

            def __get__image__(self, position):
                AppFunctions.getImageFromIPCam(self, position)
                        
            def on_message(client, userdata, msg):
                payloadRecieve = msg.payload.decode()
                print(f"Received '{payloadRecieve}' from '{msg.topic}' topic")
                __get__image__(self, payloadRecieve)
                __show__detect__(payloadRecieve)
            client.subscribe(topic)
            client.on_message = on_message
            
        
        time.sleep(0.5)
        client = connect_mqtt()
        subscribe(client)
        client.loop_forever()

class MainWindow(QMainWindow):
    ########################################################################
    ## MainWindow
    ########################################################################
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.position = GetPosition()
        self.position.start()
        
        self.buttonBox = ButtonBox()
        self.buttonBox.start()
        
        self.check_status = CheckStatus()
        self.check_status.start()

        # Another Window
        self.Edit_device = Edit_device_setting()
        self.Edit_line = Edit_token_setting()
        self.Edit_address = Edit_address_setting()
        self.Line_select = SelectLineTable()
        self.Address_select = SelectAddressTable()

        ## ==> ICON
        self.setWindowIcon(QtGui.QIcon("Content/icons/icon.png"))

        ## ==> MINI MAP
        self.ui.label_home_mini_map.setPixmap(QtGui.QPixmap('Content/images/alert/mini_map.png'))

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('IT 71')
        UIFunctions.labelTitle(self, 'IT 71')

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 700)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget_menu.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "ALERT", "btn_alert_setting", "url(:/icons/16x16/cil-lightbulb.png)", True)
        UIFunctions.addNewMenu(self, "SETTING", "btn_setting", "url(:/icons/16x16/cil-settings.png)", False)

        ## ==> START PAGE
        ## HOME
        self.ui.stackedWidget_menu.setCurrentWidget(self.ui.page_home)
        ## SETTING
        self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_camera)

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        ## ==> WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        ## ==> LOAD DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## ==> CREATE TIMER
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.showTime()

        ## ==> HOME PAGE
        self.ui.btn_home_end_alert.clicked.connect(self.resetHomeScreen)

        ## ==> SETTING MENU CONNECT PAGE
        self.ui.btn_setting_camera.clicked.connect(self.Button)
        self.ui.btn_setting_line_token.clicked.connect(self.Button)
        self.ui.btn_setting_address.clicked.connect(self.Button)
        self.ui.btn_setting_system_info.clicked.connect(self.Button)

        ## ==> SETTING CAMERA PAGE
        self.ui.btn_add_cam.clicked.connect(self.saveDeviceInput)
        self.ui.btn_add_cam_reset.clicked.connect(self.resetDeviceInput)
        self.ui.btn_edit_cam.clicked.connect(self.editDataDevice)     
        self.ui.btn_delete_cam.clicked.connect(self.deleteDataDevice)
        self.ui.btn_select_address.clicked.connect(self.selectAddressList)

        ## ==> SETTING TOKEN PAGE
        self.ui.btn_add_token_reset.clicked.connect(self.resetTokenInput)
        self.ui.btn_add_token.clicked.connect(self.saveTokenInput)
        self.ui.btn_edit_token.clicked.connect(self.editDataToken)     
        self.ui.btn_delete_token.clicked.connect(self.deleteDataToken)

        ## ==> ALERT PAGE
        AppFunctions.loadDataDeviceList(self)
        self.ui.tableWidget_cam_list.selectionModel().selectionChanged.connect(self.on_selection)
        self.ui.btn_show_cam.clicked.connect(self.selectionCamChanged)
        self.ui.btn_select_line.clicked.connect(self.selectLineList)
        #self.ui.btn_enable_disable_notification.setCheckable(True)
        self.ui.btn_enable_disable_notification.clicked.connect(self.enableAlert)
        
        ## ==> SETTING ADDRESS PAGE
        self.ui.btn_add_address.clicked.connect(self.saveAddressInput)
        self.ui.btn_add_address_reset.clicked.connect(self.resetAddressInput)
        self.ui.btn_edit_address.clicked.connect(self.editDataAddress)     
        self.ui.btn_delete_address.clicked.connect(self.deleteDataAddress)

        ## SHOW ==> MAIN WINDOW
        self.show()

    def enableAlert(self):
        AppFunctions.enableAlert(self)
    
    ## ==> RESET HOME SCREEN
    def resetHomeScreen(self):
        self.ui.label_home_display.setText("Waiting for incoming dectection.")
        self.ui.label_home_mini_map.setPixmap(QtGui.QPixmap('Content/images/alert/mini_map.png'))
        self.ui.label_top_info_1.setText('Return to main display.')
        self.setLightDisplay(False)
        self.checkButtonState()

    def setDisplay(self, image):
        self.ui.label_home_display.setPixmap(QtGui.QPixmap(image))

    ## ==> SHOW IMAGE DETECTION
    def setMiniMap(self, position):
        movie = QMovie("Content/images/alert/" + position + ".gif")
        self.ui.label_home_mini_map.setMovie(movie)
        movie.start()
    
    def setLightDisplay(self, run):
        if run:
            GPIO.output(29,GPIO.HIGH)
        else:
            GPIO.output(29,GPIO.LOW)
            
    def checkButtonState(self):
        GPIO.output(18,GPIO.LOW)
    
    def showDetect(self, position):
        conn_check_notify = sqlite3.connect("Content/database/database.db")
        cursor_check_notify = conn_check_notify.cursor()
        cursor_check_notify.execute("SELECT devices.notify FROM position INNER JOIN devices ON position.device_name = devices.name WHERE position.position = ?",(str(position),))
        ViewData_notify = cursor_check_notify.fetchall()
        
        cursor_check_status = conn_check_notify.cursor()
        cursor_check_status.execute("SELECT devices.status FROM position INNER JOIN devices ON position.device_name = devices.name WHERE position.position = ?",(str(position),))
        ViewData_status = cursor_check_status.fetchall()
        
        if ViewData_notify:
            for i in range(len(ViewData_notify)):
                notify = "".join(ViewData_notify[i])
        else:
            notify = "Disable"
            
        if ViewData_status:
            for i in range(len(ViewData_status)):
                status = "".join(ViewData_status[i])
        else:
            status = "Offline"
            
        if status == "Online" and notify == "Enable":
            for count in range(1 ,5): #for ip cam
                INPUT_FILE = 'Content/images/detected/image-' + str(int(count)) + '.jpg'
                #INPUT_FILE = 'Content/images/street.jpg'
                OUTPUT_FILE = 'Content/images/detected/'
                LABELS_FILE = 'Content/models/coco.names'
                CONFIG_FILE = 'Content/models/yolov2.cfg'
                WEIGHTS_FILE = 'Content/models/yolo_final.weights'
                CONFIDENCE_THRESHOLD = 0.7
                LIST_CLEAR = int(count)
                print (LIST_CLEAR)
                try:
                    AppFunctions.detectProcess(self, INPUT_FILE, OUTPUT_FILE, LABELS_FILE, CONFIG_FILE, WEIGHTS_FILE, CONFIDENCE_THRESHOLD, LIST_CLEAR, position)
                except:
                    AppFunctions.detectProcess(self, "Content/images/None.png", OUTPUT_FILE, LABELS_FILE, CONFIG_FILE, WEIGHTS_FILE, CONFIDENCE_THRESHOLD, LIST_CLEAR, position)
            print('Complete.')
        elif status == "Online" and notify == "Disable":
            print("Selected device is now disable notification.")
        elif status == "Offline":
            print("Selected device is now offline.")
        else:
            print("errno")
    
    ## ==> MOUSE CLICK
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ########################################################################
    ## ==> APP INTERFACE
    ########################################################################
    ## ==> SHOW TIME
    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.ui.label_top_info_3.setText(timeDisplay)

    ## ==> MOUSE DOUBLE CLICK
    def eventFilter(self, watched, event):
        if watched == self.ui.tableWidget_cam_list and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())


    ########################################################################
    ## ==> APP SETTING MENUS
    ######################################################################## 
    ## ==> LOAD DEVICE
    def loadDataDevice(self):
        self.ui.tableWidget_device_added.setRowCount(0)
        ## enumerate means (index,value)
        
        device_list = conn.select("SELECT id,name FROM devices")
        for row_number,row_data in enumerate(device_list):
            self.ui.tableWidget_device_added.insertRow(row_number)
            
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_device_added.setItem(row_number,column_number,cell)
                self.ui.tableWidget_device_added.item(row_number,0).setText(str(row_number + 1))

        device_ip = conn.select("SELECT ip FROM devices")
        for row_number,row_data in enumerate(device_ip):
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_device_added.setItem(row_number,column_number+2,cell)
                
        device_status = conn.select("SELECT status FROM devices")
        for row_number,row_data in enumerate(device_status):
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_device_added.setItem(row_number,column_number+3,cell)

    ## ==> LOAD LINE TOKEN
    def loadDataToken(self):
        result = conn.select("SELECT * FROM tokens")
        self.ui.tableWidget_token_added.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.ui.tableWidget_token_added.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_token_added.setItem(row_number,column_number,cell)
                self.ui.tableWidget_token_added.item(row_number,0).setText(str(row_number + 1))
                
    ## ==> LOAD ADDRESS
    def loadDataAddress(self):
        result = conn.select("SELECT id,position,address,ip,status FROM position")
        self.ui.tableWidget_address_added.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.ui.tableWidget_address_added.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_address_added.setItem(row_number,column_number,cell)
                self.ui.tableWidget_address_added.item(row_number,0).setText(str(row_number + 1))

    ## ==> open select line to notify widget and close
    def selectLineList(self):
        try:
            current_row = self.ui.tableWidget_cam_list.currentRow()
            select = self.ui.tableWidget_cam_list.item(current_row,1).text()
            print("select : " + select)
            self.Line_select.displayInfo()
        except:
            print ("please select table")
            QMessageBox().information(self, "Attention", "please select table")
            
    ## ==> open select address and close
    def selectAddressList(self):
        self.Address_select.displayInfo()
        

    ## ==> open edit device widget
    def editDataDevice(self):
        try:
            select = self.ui.tableWidget_device_added.currentRow()
            name = self.ui.tableWidget_device_added.item(select,1).text()
            result = conn.select("SELECT name,ip,port,username,password FROM devices WHERE name='" + str(name) + "'")
            self.Edit_device.displayInfo()
            for data in result:
                self.Edit_device.lineEdit_name.setText(str(data[0]))
                self.Edit_device.lineEdit_ip.setText(str(data[1]))
                self.Edit_device.lineEdit_port.setText(str(data[2]))
                self.Edit_device.lineEdit_username.setText(str(data[3]))
                self.Edit_device.lineEdit_password.setText(str(data[4]))
                
            address_result = conn.select("SELECT address FROM position WHERE device_name='" + str(name) + "'")
            address = ""
            print(len(address_result))
            for i in range(len(address_result)):
                address += "".join(address_result[i]) + ", "
            
            self.Edit_device.lineEdit_address.setText(address)
        except:
            print ("please select device")
            QMessageBox().information(self, "Attention", "please select device")

    ## ==> open edit token widget
    def editDataToken(self):
        try:
            select = self.ui.tableWidget_token_added.currentRow()
            name = self.ui.tableWidget_token_added.item(select,1).text()
            token = self.ui.tableWidget_token_added.item(select,2).text()
            result = conn.select("SELECT name,address FROM tokens WHERE name='" + str(name) + "' AND address='" + str(token) + "'")
            self.Edit_line.displayInfo()
            for data in result:
                self.Edit_line.lineEdit_name.setText(str(data[0]))
                self.Edit_line.lineEdit_token.setText(str(data[1]))
        except:
            print ("please select tokem")
            QMessageBox().information(self, "Attention", "please select token")

    ## ==> open edit address widget
    def editDataAddress(self):
        try:
            select = self.ui.tableWidget_address_added.currentRow()
            position = self.ui.tableWidget_address_added.item(select,1).text()
            address = self.ui.tableWidget_address_added.item(select,2).text()
            ip = self.ui.tableWidget_address_added.item(select,3).text()
            result = conn.select("SELECT position,address,ip FROM position WHERE position='" + str(position) + "' AND address='" + str(address) + "'")
            self.Edit_address.displayInfo()
            for data in result:
                self.Edit_address.lineEdit_position.setText(str(data[0]))
                self.Edit_address.lineEdit_address_info.setText(str(data[1]))
                self.Edit_address.lineEdit_ip.setText(str(data[2]))
        except:
            print ("please select address")
            QMessageBox().information(self, "Attention", "please select address")

    ## ==> RESET INPUT ADD DEVICE
    def resetDeviceInput(self):
        AppFunctions.resetDeviceInput(self)

    ## ==> SAVE INPUT ADD DEVICE
    def saveDeviceInput(self):
        AppFunctions.saveDeviceInput(self)
        AppFunctions.resetDeviceInput(self)

    ## ==> DELETE SELECT DEVICE
    def deleteDataDevice(self):
        AppFunctions.deleteDataDevice(self)

    ## ==> RESET INPUT ADD TOKEN
    def resetTokenInput(self):
        AppFunctions.resetTokenInput(self)

    ## ==> SAVE INPUT ADD TOKEN
    def saveTokenInput(self):
        AppFunctions.saveTokenInput(self)
        AppFunctions.resetTokenInput(self)

    ## ==> DELETE SELECT TOKEN
    def deleteDataToken(self):
        AppFunctions.deleteDataToken(self)
    
    ## ==> RESET INPUT ADD ADDRESS
    def resetAddressInput(self):
        AppFunctions.resetAddressInput(self)

    ## ==> SAVE INPUT ADD ADDRESS
    def saveAddressInput(self):
        AppFunctions.saveAddressInput(self)
        AppFunctions.resetAddressInput(self)

    ## ==> DELETE SELECT ADDRESS
    def deleteDataAddress(self):
        AppFunctions.deleteDataAddress(self)
        
    ## ==> SELECT EDIT DEVICE
    def selectionEditDeiviceChanged(self):
        AppFunctions.selectionEditDeviceChanged(self)

    ## ==> SAVE SETTING

    ## ==> RELOAD DEVICE
    def clearDataDevice(self):
        while(self.ui.tableWidget_device_added.rowCount() > 0):
            self.ui.tableWidget_device_added.removeRow(0)

    ## ==> RELOAD TOKEN
    def clearDataToken(self):
        while(self.ui.tableWidget_token_added.rowCount() > 0):
            self.ui.tableWidget_token_added.removeRow(0)
            
    ## ==> RELOAD ADDRESS
    def clearDataAddress(self):
        while(self.ui.tableWidget_address_added.rowCount() > 0):
            self.ui.tableWidget_address_added.removeRow(0)

    def on_selection(self, selected):
        try:
            select = self.ui.tableWidget_cam_list.currentRow()
            selected = self.ui.tableWidget_cam_list.item(select,1).text()
            device_list = conn.select("SELECT name FROM devices WHERE name='" + str(selected) + "'")
            
            for data in device_list:
                self.ui.label_alert_setting_device_name.setText('Name : ' + str(data[0]))
            
            address_result = conn.select("SELECT address FROM position WHERE device_name='" + str(selected) + "'")
            address = ""
            for i in range(len(address_result)):
                address += " ".join(address_result[i]) + ", "
            self.ui.label_alert_setting_device_address.setText('Address : ' + address)
                
            position_result = conn.select("SELECT position FROM position WHERE device_name='" + str(selected) + "'")
            position = ""
            for i in range(len(position_result)):
                position += " ".join(position_result[i]) + ", "
            self.ui.label_alert_setting_device_description.setText('Position : ' + position)
            
            notify = conn.select("SELECT notify FROM devices WHERE name='" + str(selected) + "'")
            for data in notify:
                self.ui.label_notification_status.setText('Notification Status : ' + str(data[0]))
            line_selected = conn.select("SELECT token_name FROM device_has_token WHERE device_name='" + str(selected) + "'")
            device_has_line = []
            text = ""
            for data in line_selected:
                device_has_line.append(data)

            for i in range(len(device_has_line)):
                text = text + "".join(device_has_line[i]) + ", "

            self.ui.label_select_line.setText('     ' + text)
        except:
            pass

    def selectionCamChanged(self):
        try:
            AppFunctions.selectionCamChanged(self)
        except:
            pass

    ## ==> DYNAMIC MENUS FUNCTIONS
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget_menu.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NOTIFY SETTING
        if btnWidget.objectName() == "btn_alert_setting":
            self.ui.stackedWidget_menu.setCurrentWidget(self.ui.page_alert_setting)
            UIFunctions.resetStyle(self, "btn_alert_setting")
            UIFunctions.labelPage(self, "Alert")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            AppFunctions.loadDataDeviceList(self)

        # PAGE SETTING
        if btnWidget.objectName() == "btn_setting":
            self.ui.stackedWidget_menu.setCurrentWidget(self.ui.page_setting)
            UIFunctions.resetStyle(self, "btn_setting")
            UIFunctions.labelPage(self, "Setting")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.loadDataDevice()

        # PAGE SETTING CAMERA
        if btnWidget.objectName() == "btn_setting_camera":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_camera)
            UIFunctions.resetSettingStyle(self, "btn_setting_camera")
            btnWidget.setStyleSheet(UIFunctions.selectSettingMenu(btnWidget.styleSheet()))
            self.loadDataDevice()

        # PAGE SETTING LINE TOKEN
        if btnWidget.objectName() == "btn_setting_line_token":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_line_token)
            UIFunctions.resetSettingStyle(self, "btn_setting_line_token")
            btnWidget.setStyleSheet(UIFunctions.selectSettingMenu(btnWidget.styleSheet()))
            self.loadDataToken()

        # PAGE SETTING ADDRESS
        if btnWidget.objectName() == "btn_setting_address":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_address)
            UIFunctions.resetSettingStyle(self, "btn_setting_address")
            btnWidget.setStyleSheet(UIFunctions.selectSettingMenu(btnWidget.styleSheet()))
            self.loadDataAddress()

        # PAGE SETTING SYSTEM INFO
        if btnWidget.objectName() == "btn_setting_system_info":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_system_info)
            UIFunctions.resetSettingStyle(self, "btn_setting_system_info")
            btnWidget.setStyleSheet(UIFunctions.selectSettingMenu(btnWidget.styleSheet()))

class SelectLineTable(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_LineSelect.ui",self)

        self.btn_apply.clicked.connect(self.apply)
        self.btn_cancel.clicked.connect(self.closeInfo)
        self.loadLine()

    def apply(self):
        line = []
        selected = self.tableWidget_line.selectedItems()
        
        select_row = MainWindow.ui.tableWidget_cam_list.currentRow()
        device_name = MainWindow.ui.tableWidget_cam_list.item(select_row,1).text()
        
        if selected:
            conn.delete("DELETE FROM device_has_token WHERE device_name='" + str(device_name) + "'")
            for item in selected:
                line.append(item.data(0))
                
            for i in range(len(line)):
                name = line[i]
                result = [device_name, name]
                conn.edit("INSERT INTO device_has_token(device_name,token_name) VALUES(?,?)",result)
                print("name : " + name)
        else:
            print ("not changed")
            
        line_selected = conn.select("SELECT token_name FROM device_has_token WHERE device_name='" + str(device_name) + "'")
        device_has_line = []
        text = ""
        for data in line_selected:
            device_has_line.append(data)

        for i in range(len(device_has_line)):
            text = text + ", ".join(device_has_line[i])

        MainWindow.ui.label_select_line.setText('     ' + text)
            
        self.close()

    def loadLine(self):
        conn = SqliteHelper("Content/database/database.db")
        result = conn.select("SELECT name FROM tokens")
        self.tableWidget_line.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget_line.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_line.setItem(row_number,column_number,cell)

    def displayInfo(self):
        self.show()
    
    def closeInfo(self):
        self.close()
        
class SelectAddressTable(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_AddressSelect.ui",self)

        self.btn_apply.clicked.connect(self.apply)
        self.btn_cancel.clicked.connect(self.closeInfo)
        self.loadAddress()

    def apply(self):
        address = []
        selected = self.tableWidget_address.selectedItems()
        name = ""
        if selected:
            for item in selected:
                address.append(item.data(0))
                
            for i in range(len(address)):
                name += "".join(address[i]) + ", "
        else:
            print ("not select")
        MainWindow.ui.lineEdit_add_cam_position.setText(name)
            
        self.close()

    def loadAddress(self):
        conn = SqliteHelper("Content/database/database.db")
        result = conn.select("SELECT address FROM position")
        self.tableWidget_address.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget_address.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_address.setItem(row_number,column_number,cell)

    def displayInfo(self):
        self.show()
    
    def closeInfo(self):
        self.close()

class Edit_device_setting(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_DeviceEdit.ui', self)

        self.btn_save.clicked.connect(self.save)
        self.btn_reset.clicked.connect(self.reset)

    def save(self):
        name = self.lineEdit_name.text()
        position = self.lineEdit_position.text()
        positions = position.split(",")
        ip = self.lineEdit_ip.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        select_row = MainWindow.ui.tableWidget_device_added.currentRow()
        device_name = MainWindow.ui.tableWidget_device_added.item(select_row,1).text()

        if device_id.strip(" ") != "" and name.strip(" ") != "" and position.strip(" ") != "" and ip.strip(" ") != "":
            device_result = [device_id, name, ip, username, password]
            conn.edit("UPDATE devices SET name=?, ip=?, username=?, password=? WHERE name LIKE '%{1}%'".format(device_name) , device_result)
            conn.delete("DELETE FROM position WHERE device_name='" + device_name + "'")
            pos1 = [name, positions[0]]
            pos2 = [name, positions[1]]
            conn.edit("INSERT INTO position(device_name,position) VALUES(?,?)",pos1)
            conn.edit("INSERT INTO position(device_name,position) VALUES(?,?)",pos2)
            result = [name]
            conn.edit("UPDATE device_has_token SET device_name=? WHERE device_name LIKE '%{0}%'".format(device_name) , result)
            conn.edit("UPDATE notify SET device_name=? WHERE device_name LIKE '%{0}%'".format(device_name) , result)
            conn.edit("UPDATE status SET device_name=? WHERE device_name LIKE '%{0}%'".format(device_name) , result)
            MainWindow.clearDataDevice()
            MainWindow.loadDataDevice()
        else:
            AppFunctions.show_error_message_device(self, "Attention")
        
        self.close()

    def displayInfo(self):
        self.show()

    def reset(self):
        self.lineEdit_name.setText("")
        self.lineEdit_address.setText("")
        self.lineEdit_ip.setText("")
        self.lineEdit_username.setText("")
        self.lineEdit_password.setText("")

class Edit_token_setting(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_LineEdit.ui', self)

        self.btn_save.clicked.connect(self.save)
        self.btn_reset.clicked.connect(self.reset)

    def save(self):
        name = self.lineEdit_name.text()
        address = self.lineEdit_token.text()

        select_row = MainWindow.ui.tableWidget_token_added.currentRow()
        token_name = MainWindow.ui.tableWidget_token_added.item(select_row,1).text()
        token_address = MainWindow.ui.tableWidget_token_added.item(select_row,2).text()

        if name.strip(" ") != "" and address.strip(" ") != "":
            token_result = [name, address]
            conn.edit("UPDATE tokens SET name=?, address=? WHERE name LIKE '%{0}%' AND address LIKE '%{1}%'".format(token_name,token_address) , token_result)
            result = [name]
            conn.edit("UPDATE device_has_token SET token_name=? WHERE token_name LIKE '%{0}%'".format(token_name) , result)
            MainWindow.clearDataToken()
            MainWindow.loadDataToken()
        else:
            AppFunctions.show_error_message_token(self, "Attention")

        self.close()

    def reset(self):
        self.lineEdit_name.setText("")
        self.lineEdit_token.setText("")

    def displayInfo(self):
        self.show()
        
class Edit_address_setting(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_AddressEdit.ui', self)

        self.btn_save.clicked.connect(self.save)
        self.btn_reset.clicked.connect(self.reset)

    def save(self):
        position = self.lineEdit_position.text()
        address_info = self.lineEdit_address_info.text()
        ip = self.lineEdit_ip.text()

        select_row = MainWindow.ui.tableWidget_address_added.currentRow()
        position = MainWindow.ui.tableWidget_address_added.item(select_row,1).text()
        address = MainWindow.ui.tableWidget_address_added.item(select_row,2).text()

        if position.strip(" ") != "" and address_info.strip(" ") != "":
            address_result = [position, address_info, ip]
            conn.edit("UPDATE position SET position=?, address=?, ip=? WHERE position LIKE '%{0}%' AND address LIKE '%{1}%'".format(position,address) , address_result)
            MainWindow.clearDataAddress()
            MainWindow.loadDataAddress()
        else:
            AppFunctions.show_error_message_token(self, "Attention")

        self.close()

    def reset(self):
        self.lineEdit_position.setText("")
        self.lineEdit_address_info.setText("")

    def displayInfo(self):
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('Content/fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('Content/fonts/segoeuib.ttf')
    MainWindow = MainWindow()
    try:
        sys.exit(App.exec_())
    except SystemExit:
        print('Closing Window...')
