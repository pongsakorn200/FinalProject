## ==> GUI FILE
from main import *

from SqliteHelper import *

list_confidences = []
conn = SqliteHelper("Content/database/database.db")

class AppFunctions(MainWindow):
    ########################################################################
    ## ==> APP EVENTS
    ########################################################################
    ## ==> SAVE IMAGE FROM IP CAMERA
    def getImageFromIPCam(self, select):
        connenct = sqlite3.connect("Content/database/database.db")
        cur = connenct.cursor()
        query = "SELECT devices.ip,devices.username,devices.password FROM devices INNER JOIN position WHERE position.position='" + select + "'"
        cur.execute(query)
        result = cur.fetchall()
        try:
            for data in result:
                url = 'http://' + str(data[0]) + '/snapshot.cgi?user=' + str(data[1]) + '&pwd=' + str(data[2]) + ''
                file_path = 'Content/images/detected/'
                for i in range (1, 4):
                    filename = 'image-{}.jpg'.format(i)
                    full_path = '{}{}'.format(file_path, filename)
                    urllib.request.urlretrieve(url, full_path)
                    print('{} saved.'.format(filename))
        except:
            print("Your device is now offline.")
        connenct.close()            
        
    ## ==> SET IMAGE TO MONITOR
    def setImageMainDisplay(self, largest, OUTPUT_FILE, LIST_CLEAR):
        self.ui.label_home_display.setPixmap(QtGui.QPixmap('{}{}.jpg'.format(OUTPUT_FILE, largest)))
        self.ui.stackedWidget_menu.setCurrentWidget(self.ui.page_home)

    ## SEND TEXT AND PICTURE TO LINE
    def line_pic(message, path_file, line_token):
        URL_LINE = "https://notify-api.line.me/api/notify"
        file_img = {'imageFile': open(path_file, 'rb')}
        msg = ({'message': message})
        LINE_HEADERS = {"Authorization":"Bearer " + line_token}
        session = requests.Session()
        try:
            session_post = session.post(URL_LINE, headers = LINE_HEADERS, files = file_img, data = msg)
            print(session_post.text)
        except:
            print ("No internet connection! Please connect your device with internet.")

    ## DETECT AND/OR PROCESS PERSON
    def detectProcess(self, INPUT_FILE, OUTPUT_FILE, LABELS_FILE, CONFIG_FILE, WEIGHTS_FILE, CONFIDENCE_THRESHOLD, LIST_CLEAR, position):
        global LARGEST
        if (LIST_CLEAR < 4): # for ip cam
            LABELS = open(LABELS_FILE).read().strip().split("\n")
            np.random.seed(4)
            COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
            net = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)
            image = cv2.imread(INPUT_FILE)
            (H, W) = image.shape[:2]
            # determine only the *output* layer names that we need from YOLO
            ln = net.getLayerNames()
            ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            start = time.time()
            layerOutputs = net.forward(ln)
            end = time.time()
            print("[INFO] Processing took {:.6f} seconds".format(end - start))
            boxes = []
            confidences = []
            classIDs = []
            for output in layerOutputs:
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    if confidence > CONFIDENCE_THRESHOLD:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
                        
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, CONFIDENCE_THRESHOLD)
            # ensure at least one detection exists
            if len(idxs) > 0:
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    percent_confidences = '%.2f' %(confidences[i] * 100)
                    print ('Accuracy : {}'.format(str(percent_confidences)))
                    list_confidences.append(str(percent_confidences))
                    # save output image to disk
                    cv2.imwrite('{}{}.jpg'.format(OUTPUT_FILE, str(percent_confidences)), image)
                print(list_confidences)
                LARGEST = max(list_confidences)
                return LARGEST
            # release resources
            cv2.destroyAllWindows()

        else :
            if list_confidences != []:
                connn = sqlite3.connect("Content/database/database.db")

                AppFunctions.setImageMainDisplay(self, LARGEST, OUTPUT_FILE, LIST_CLEAR)
                MainWindow.setMiniMap(self, position)
                MainWindow.setLightDisplay(self, True)
                MainWindow.checkButtonState(self)
                
                cur = connn.cursor()
                query = "SELECT devices.name,devices.ip FROM devices INNER JOIN position WHERE position.position='" + str(position) + "'"
                cur.execute(query)
                result = cur.fetchall()
                for data in result:
                    self.ui.label_top_info_1.setText('Name : ' + str(data[0]) + ' IP : ' + str(data[1]) + ' Accuract : ' + str(LARGEST))

                connect = sqlite3.connect("Content/database/database.db")
                cursor = connect.cursor()
                cursor.execute("SELECT tokens.address FROM position INNER JOIN device_has_token INNER JOIN tokens ON position.device_name = device_has_token.device_name AND device_has_token.token_name = tokens.name WHERE position.position = ?",(str(position),))
                ViewData = cursor.fetchall()
                connect.commit()
                
                device_has_line = []
                for data in ViewData:
                    device_has_line.append(data)

                for i in range(len(device_has_line)):
                    text = "".join(device_has_line[i])
                    print(text)
                    AppFunctions.line_pic('พบเหตุปีนรั้ว\nความมั่นใจ : {} %'.format(LARGEST), '{}{}.jpg'.format( OUTPUT_FILE, LARGEST), text)

            time.sleep(0.5)
            for i in glob.glob(os.path.join('Content/images/detected/',"*.jpg")):
                try:
                    os.chmod(i,0o777)
                    os.remove(i)
                except OSError:
                    pass
            print('Success delete image!')
            list_confidences.clear()

    ########################################################################         
    ## ==> LOAD/RELOAD/ADD/EDIT/DELETE DATABASE
    ########################################################################

    ## ==> LOAD DEVICE IN ALERT PAGE
    def loadDataDeviceList(self):
        device_list = conn.select("SELECT id,name FROM devices")
        cam_list_table = self.ui.tableWidget_cam_list
        cam_list_table.setRowCount(0)
        for row_number, row_data in enumerate(device_list):
            cam_list_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                cell = QtWidgets.QTableWidgetItem(str(data))
                cell.setTextAlignment(Qt.AlignCenter)
                cam_list_table.setItem(row_number,column_number,cell)
                cam_list_table.item(row_number,0).setText(str(row_number + 1))

    ## ==> ADD DEVICE
    def saveDeviceInput(self):
        cam_name = self.ui.lineEdit_add_cam_name.text()
        cam_position = self.ui.lineEdit_add_cam_position.text()
        cam_ip = self.ui.lineEdit_add_cam_ip.text()
        cam_port = self.ui.lineEdit_add_cam_port.text()
        cam_username = self.ui.lineEdit_add_cam_username.text()
        cam_password = self.ui.lineEdit_add_cam_password.text()
        if cam_name.strip(" ") != "" and cam_position.strip(" ") != "" and cam_ip.strip(" ") != "":
            result = [cam_name, cam_ip, cam_port, cam_username, cam_password, "Disable", "Offline"]
            conn.edit("INSERT INTO devices(name,ip,port,username,password,notify,status) VALUES(?,?,?,?,?,?,?)",result)
            position = cam_position.split(",")
            for i in range(len(position)):
                result1 = [position[i]]
                conn.edit("UPDATE position SET device_name=? WHERE address LIKE '%{0}%'".format(cam_position), result1)
            MainWindow.clearDataDevice(self)
            MainWindow.loadDataDevice(self)
        else:
            AppFunctions.show_error_message_device(self, "Attention")
        
        
    ## ==> ADD LINE TOKEN
    def saveTokenInput(self):
        name = self.ui.lineEdit_token_name.text()
        address = self.ui.lineEdit_token_address.text()
        if name.strip(" ") != "" and address.strip(" ") != "":
            result = [str(name), str(address)]
            conn.edit("INSERT INTO tokens(name,address) VALUES(?,?)",result)
            MainWindow.clearDataToken(self)
            MainWindow.loadDataToken(self)
        else:
            AppFunctions.show_error_message_token(self, "Attention")
            
    ## ==> ADD ADDRESS
    def saveAddressInput(self):
        position = self.ui.lineEdit_address_position.text()
        address = self.ui.lineEdit_address_info.text()
        ip = self.ui.lineEdit_address_ip.text()
        if position.strip(" ") != "" and address.strip(" ") != "" and ip.strip(" ") != "":
            result = ["", position, address, ip, "Offline"]
            conn.edit("INSERT INTO position(device_name,position,address,ip,status) VALUES(?,?,?,?,?)",result)
            MainWindow.clearDataAddress(self)
            MainWindow.loadDataAddress(self)
        else:
            AppFunctions.show_error_message_device(self, "Attention")

    ## ==> DELETE DEVICE
    def deleteDataDevice(self):
        try:
            select_row = self.ui.tableWidget_device_added.currentRow()
            cam_name = self.ui.tableWidget_device_added.item(select_row, 1).text()
            cam_ip = self.ui.tableWidget_device_added.item(select_row, 2).text()
            conn.delete("DELETE FROM devices WHERE name LIKE '%{0}%' AND ip LIKE '%{1}%'".format(cam_name, cam_ip))
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print (sys.exc_info()[0])

        MainWindow.clearDataDevice(self)
        MainWindow.loadDataDevice(self)

    ## ==> DELETE LINE TOKEN
    def deleteDataToken(self):
        try:
            select_row = self.ui.tableWidget_token_added.currentRow()
            token_name = self.ui.tableWidget_token_added.item(select_row, 1).text()
            token_address = self.ui.tableWidget_token_added.item(select_row, 2).text()
            conn.delete("DELETE FROM tokens WHERE name LIKE '%{0}%' AND address LIKE '%{1}%'".format(token_name,token_address))
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print (sys.exc_info()[0])

        MainWindow.clearDataToken(self)
        MainWindow.loadDataToken(self)
        
    ## ==> DELETE ADDRESS
    def deleteDataAddress(self):
        try:
            select_row = self.ui.tableWidget_address_added.currentRow()
            position = self.ui.tableWidget_address_added.item(select_row, 1).text()
            address = self.ui.tableWidget_address_added.item(select_row, 2).text()
            conn.delete("DELETE FROM position WHERE position LIKE '%{0}%' AND address LIKE '%{1}%'".format(position,address))
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print (sys.exc_info()[0])

        MainWindow.clearDataAddress(self)
        MainWindow.loadDataAddress(self)

    ## ==> RESET DEVICE INPUT
    def resetDeviceInput(self):
        self.ui.lineEdit_add_cam_name.setText('')
        self.ui.lineEdit_add_cam_port.setText('')
        self.ui.lineEdit_add_cam_position.setText('')
        self.ui.lineEdit_add_cam_ip.setText('')
        self.ui.lineEdit_add_cam_username.setText('')
        self.ui.lineEdit_add_cam_password.setText('')

    ## ==> RESET LINE TOKEN INPUT
    def resetTokenInput(self):
        self.ui.lineEdit_token_name.setText('')
        self.ui.lineEdit_token_address.setText('')
        
    ## ==> RESET LINE ADDRESS INPUT
    def resetAddressInput(self):
        self.ui.lineEdit_address_position.setText('')
        self.ui.lineEdit_address_info.setText('')
        self.ui.lineEdit_address_ip.setText('')

    def show_error_message_device(self, title="Attention", message="Please fill all input!"):
        QMessageBox().information(self, title, message)

    def show_error_message_token(self, title="Attention", message="Please fill all input!"):
        QMessageBox().information(self, title, message)
        
    def show_error_message_address(self, title="Attention", message="Please fill all input!"):
        QMessageBox().information(self, title, message)

    ## ==> SELECT CAMERA CHANGE
    def selectionCamChanged(self):
        select = self.ui.tableWidget_cam_list.currentRow()
        selected = self.ui.tableWidget_cam_list.item(select,1).text()
        device_list = conn.select("SELECT ip,username,password FROM devices WHERE name='" + str(selected) + "'")
        
        for data in device_list:
            try:
                url = 'http://' + str(data[0]) + '/snapshot.cgi?user=' + str(data[1]) + '&pwd=' + str(data[2]) + ''
                AppFunctions.getImageIPCamList(self, url)
            except:
                self.ui.label_alert_setting_show_cam.setText("Your device is offline.")
                print ("camera not connected.", sys.exc_info()[0])


    ## ==> SAVE IMAGE FROM IP CAMERA TO SHOW
    def getImageIPCamList(self, url):
        file_path = 'Content/images/'
        filename = 'image_cam_list.jpg'
        full_path = '{}{}'.format(file_path, filename)
        urllib.request.urlretrieve(url, full_path)
        print('{} saved.'.format(filename))
        self.ui.label_alert_setting_show_cam.setPixmap(QtGui.QPixmap(full_path))

    def enableAlert(self):
        select_row = self.ui.tableWidget_cam_list.currentRow()
        device_name = self.ui.tableWidget_cam_list.item(select_row, 1).text()
        notify = conn.select("SELECT notify FROM devices WHERE name LIKE '%{0}%'".format(device_name))
        for data in notify:
            if str(data[0]) == "Enable":
                result = ["Disable"]
                conn.edit("UPDATE devices SET notify=? WHERE name LIKE '%{0}%'".format(device_name), result)
            if str(data[0]) == "Disable":
                result = ["Enable"]
                conn.edit("UPDATE devices SET notify=? WHERE name LIKE '%{0}%'".format(device_name), result)
            self.ui.label_notification_status.setText('Notification Status : ' + str(data[0]))
            MainWindow.on_selection(self, select_row)