from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os
import resourcesCascade

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 680)
        MainWindow.setStyleSheet("background-color: rgb(37, 60, 105);\n"
                                 "color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgl = QtWidgets.QLabel(self.centralwidget)
        self.bgl.setGeometry(QtCore.QRect(0, 0, 771, 761))
        self.bgl.setText("")
        self.bgl.setPixmap(QtGui.QPixmap(":/images/images for cascade/bg_image.png"))
        self.bgl.setObjectName("bgl") 
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 771, 731))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.notes_title = QtWidgets.QLabel(self.frame)
        self.notes_title.setGeometry(QtCore.QRect(20, 17, 211, 71))
        self.notes_title.setStyleSheet("color: rgb(167, 145, 203);\n"
                                       "background-color: rgb(255, 255, 255,0);\n"
                                       "font: 40pt \"Montserrat\";\n"
                                       "font-weight: bold;\n"
                                       "")
        self.notes_title.setObjectName("notes_title")
        self.notes_title.setText("Notes")

        self.add_note_button = QtWidgets.QLabel(self.frame)
        self.add_note_button.setGeometry(QtCore.QRect(320, 81, 41, 51))
        self.add_note_button.setStyleSheet("QLabel{\n"
                                            "    background-color: rgb(255, 255, 255,0);\n"
                                            "}\n"
                                            "\n"
                                            "QLabel:hover {\n"
                                            "    color: rgb(142, 123, 173);\n"
                                            "}\n"
                                            "")
        self.add_note_button.setText("")
        self.add_note_button.setPixmap(QtGui.QPixmap(":/images/images for cascade/create_note_icon.png"))
        self.add_note_button.setObjectName("add_note_button")

        self.delete_note_button = QtWidgets.QLabel(self.frame)
        self.delete_note_button.setGeometry(QtCore.QRect(380, 80, 41, 51))
        self.delete_note_button.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.delete_note_button.setText("")
        self.delete_note_button.setPixmap(QtGui.QPixmap(":/images/images for cascade/delete_note_icon.png"))
        self.delete_note_button.setObjectName("delete_note_button")

        self.edit_note_button = QtWidgets.QLabel(self.frame)
        self.edit_note_button.setGeometry(QtCore.QRect(430, 80, 41, 51))
        self.edit_note_button.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.edit_note_button.setText("")
        self.edit_note_button.setPixmap(QtGui.QPixmap(":/images/images for cascade/edit_note_icon.png"))
        self.edit_note_button.setObjectName("edit_note_button")

        self.notes_textbox = QtWidgets.QPlainTextEdit(self.frame)
        self.notes_textbox.setGeometry(QtCore.QRect(10, 90, 761, 641))
        self.notes_textbox.setStyleSheet("QPlainTextEdit {\n"
                                         "    background-color: rgba(255, 255, 255, 0);\n"
                                         "    font: 10pt \"Montserrat\";\n"
                                         "    color: rgb(195, 195, 195);\n"
                                         "}\n"
                                         "\n"
                                         "QScrollArea {\n"
                                         "    background-color: rgb(0, 0, 0,0.3);\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar:vertical {\n"
                                         "    border: none;\n"
                                         "    background: transparent;\n"
                                         "    width: 10px; \n"
                                         "    margin: 0px 0px 0px 0px;\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar::handle:vertical {\n"
                                         "    background-color: rgb(167, 145, 203);\n"
                                         "    min-height: 10px;\n"
                                         "    border-radius: 4px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover{\n"
                                         "    background-color: rgb(129, 113, 158);\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:pressed {    \n"
                                         "    background-color: rgb(158, 121, 203);\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar::sub-line:vertical {\n"
                                         "    border: none;\n"
                                         "    background-color: rgb(167, 145, 203);\n"
                                         "    height: 0px;\n"
                                         "    border-top-left-radius: 7px;\n"
                                         "    border-top-right-radius: 7px;\n"
                                         "    subcontrol-position: top;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:hover {    \n"
                                         "    background-color: rgb(129, 113, 158);\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:pressed {    \n"
                                         "    background-color: rgb(158, 121, 203);\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar::add-line:vertical {\n"
                                         "    border: none;\n"
                                         "    background-color: rgb(167, 145, 203);\n"
                                         "    height: 0px;\n"
                                         "    border-bottom-left-radius: 7px;\n"
                                         "    border-bottom-right-radius: 7px;\n"
                                         "    subcontrol-position: bottom;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:hover {    \n"
                                         "    background-color: rgb(129, 113, 158);\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:pressed {    \n"
                                         "    background-color: rgb(158, 121, 203);\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                         "    background: none;\n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                         "    background: none;\n"
                                         "}\n"
                                         "")
        self.notes_textbox.setObjectName("notes_textbox")

        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 471, 461))
        self.listWidget.setStyleSheet("QScrollArea {\n"
                                      "    background-color: rgb(0, 0, 0,0.3);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical {\n"
                                      "    border: none;\n"
                                      "    background: transparent;\n"
                                      "    width: 10px; \n"
                                      "    margin: 0px 0px 0px 0px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "    background-color: rgb(167, 145, 203);\n"
                                      "    min-height: 10px;\n"
                                      "    border-radius: 4px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{\n"
                                      "    background-color: rgb(129, 113, 158);\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:pressed {    \n"
                                      "    background-color: rgb(158, 121, 203);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color: rgb(167, 145, 203);\n"
                                      "    height: 0px;\n"
                                      "    border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "    subcontrol-position: top;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:hover {    \n"
                                      "    background-color: rgb(129, 113, 158);\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:pressed {    \n"
                                      "    background-color: rgb(158, 121, 203);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color: rgb(167, 145, 203);\n"
                                      "    height: 0px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: bottom;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:hover {    \n"
                                      "    background-color: rgb(129, 113, 158);\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:pressed {    \n"
                                      "    background-color: rgb(158, 121, 203);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItems(["Note 1", "Note 2", "Note 3", "Note 4", "Note 5"])

        self.subheading_textbox = QtWidgets.QPlainTextEdit(self.frame)
        self.subheading_textbox.setGeometry(QtCore.QRect(10, 20, 761, 61))
        self.subheading_textbox.setStyleSheet("QPlainTextEdit {\n"
                                              "    background-color: rgba(255, 255, 255, 0);\n"
                                              "    font: 20pt \"Montserrat\";\n"
                                              "    color: rgb(195, 195, 195);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollArea {\n"
                                              "    background-color: rgb(0, 0, 0,0.3);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:vertical {\n"
                                              "    border: none;\n"
                                              "    background: transparent;\n"
                                              "    width: 10px; \n"
                                              "    margin: 0px 0px 0px 0px;\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar::handle:vertical {\n"
                                              "    background-color: rgb(167, 145, 203);\n"
                                              "    min-height: 10px;\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "QScrollBar::handle:vertical:hover{\n"
                                              "    background-color: rgb(129, 113, 158);\n"
                                              "}\n"
                                              "QScrollBar::handle:vertical:pressed {    \n"
                                              "    background-color: rgb(158, 121, 203);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar::sub-line:vertical {\n"
                                              "    border: none;\n"
                                              "    background-color: rgb(167, 145, 203);\n"
                                              "    height: 0px;\n"
                                              "    border-top-left-radius: 7px;\n"
                                              "    border-top-right-radius: 7px;\n"
                                              "    subcontrol-position: top;\n"
                                              "    subcontrol-origin: margin;\n"
                                              "}\n"
                                              "QScrollBar::sub-line:vertical:hover {    \n"
                                              "    background-color: rgb(129, 113, 158);\n"
                                              "}\n"
                                              "QScrollBar::sub-line:vertical:pressed {    \n"
                                              "    background-color: rgb(158, 121, 203);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar::add-line:vertical {\n"
                                              "    border: none;\n"
                                              "    background-color: rgb(167, 145, 203);\n"
                                              "    height: 0px;\n"
                                              "    border-bottom-left-radius: 7px;\n"
                                              "    border-bottom-right-radius: 7px;\n"
                                              "    subcontrol-position: bottom;\n"
                                              "    subcontrol-origin: margin;\n"
                                              "}\n"
                                              "QScrollBar::add-line:vertical:hover {    \n"
                                              "    background-color: rgb(129, 113, 158);\n"
                                              "}\n"
                                              "QScrollBar::add-line:vertical:pressed {    \n"
                                              "    background-color: rgb(158, 121, 203);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                              "    background: none;\n"
                                              "}\n"
                                              "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                              "    background: none;\n"
                                              "}\n"
                                              "")
        self.subheading_textbox.setCenterOnScroll(False)
        self.subheading_textbox.setObjectName("subheading_textbox")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuedit.menuAction())

        self.actionfind = QtWidgets.QAction(MainWindow)
        self.actionfind.setObjectName("actionfind")
        self.menuedit.addAction(self.actionfind)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connecting itemClicked signal to open_notepad slot
        self.listWidget.itemClicked.connect(self.open_notepad)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.actionfind.setText(_translate("MainWindow", "find and replace"))

    def open_notepad(self, item):
        note_name = item.text()
        note_path = os.path.join(os.getcwd(), f"{note_name}.txt")
        subprocess.Popen(["notepad.exe", note_path])

    def editItem(self, item):
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def addNote(self, item):
        if self.listWidget.indexFromItem(item).row() == self.listWidget.count() - 1:
            new_note = QtWidgets.QListWidgetItem()
            new_note.setText("New Note")
            self.listWidget.addItem(new_note)
            self.save_content(new_note)

    def save_content(self, item):
        note_name = item.text()
        note_content = self.notes_textbox.toPlainText()
        note_path = os.path.join(os.getcwd(), f"{note_name}.txt")
        with open(note_path, "w") as f:
            f.write(note_content)

    


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Windows")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
