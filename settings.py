# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QMainWindow
import resourcesCascade
from PyQt5.QtGui import QPixmap
from add_course_settings import Ui_add_course_settings
from course_manager import CourseManager
import mysql.connector


class Ui_settings(object):
    
    def openAddCourses(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_add_course_settings()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(1211, 807)
        settings.setStyleSheet("background-color: rgb(37, 60, 105);\n"
"")
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1221, 801))
        self.bg.setText("")
        self.bg.setPixmap(QPixmap(":/images/images for cascade/bg_image.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.logo.setStyleSheet("background-color: rgb(99, 106, 154);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"box-shadow: 10px 10px 5px rgba(0, 0, 0, 1);")
        self.logo.setText("")
        self.logo.setPixmap(QPixmap(":/images/images for cascade/Cascade-removebg-preview.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logo_bg_shadow = QtWidgets.QLabel(self.centralwidget)
        self.logo_bg_shadow.setGeometry(QtCore.QRect(25, 25, 61, 61))
        self.logo_bg_shadow.setStyleSheet("background-color: rgb(23, 35, 67);\n"
"border-radius: 10px;\n"
"")
        self.logo_bg_shadow.setText("")
        self.logo_bg_shadow.setObjectName("logo_bg_shadow")
        self.intro_nav = QtWidgets.QLabel(self.centralwidget)
        self.intro_nav.setGeometry(QtCore.QRect(570, 20, 101, 41))
        self.intro_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.intro_nav.setObjectName("intro_nav")
        self.studyplan_nav = QtWidgets.QLabel(self.centralwidget)
        self.studyplan_nav.setGeometry(QtCore.QRect(680, 20, 81, 41))
        self.studyplan_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.studyplan_nav.setObjectName("studyplan_nav")
        self.calender_nav = QtWidgets.QLabel(self.centralwidget)
        self.calender_nav.setGeometry(QtCore.QRect(770, 20, 71, 41))
        self.calender_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.calender_nav.setObjectName("calender_nav")
        self.stats_nav = QtWidgets.QLabel(self.centralwidget)
        self.stats_nav.setGeometry(QtCore.QRect(850, 20, 61, 41))
        self.stats_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.stats_nav.setObjectName("stats_nav")
        self.faq_nav = QtWidgets.QLabel(self.centralwidget)
        self.faq_nav.setGeometry(QtCore.QRect(930, 20, 41, 41))
        self.faq_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.faq_nav.setObjectName("faq_nav")
        self.about_nav = QtWidgets.QLabel(self.centralwidget)
        self.about_nav.setGeometry(QtCore.QRect(990, 20, 41, 41))
        self.about_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.about_nav.setObjectName("about_nav")
        self.contact_nav = QtWidgets.QLabel(self.centralwidget)
        self.contact_nav.setGeometry(QtCore.QRect(1050, 20, 51, 41))
        self.contact_nav.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Montserrat\";")
        self.contact_nav.setObjectName("contact_nav")
        self.nav_line = QtWidgets.QLabel(self.centralwidget)
        self.nav_line.setGeometry(QtCore.QRect(550, 60, 551, 1))
        self.nav_line.setStyleSheet("background-color: rgb(255, 255, 255,0.5);")
        self.nav_line.setText("")
        self.nav_line.setObjectName("nav_line")
        self.homepage = QtWidgets.QPushButton(self.centralwidget)
        self.homepage.setGeometry(QtCore.QRect(1120, 30, 31, 28))
        self.homepage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 14px;")
        self.homepage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QPixmap(":/images/images for cascade/homepage_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homepage.setIcon(icon)
        self.homepage.setObjectName("homepage")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(1160, 30, 31, 28))
        self.help.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 14px;")
        self.help.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QPixmap(":/images/images for cascade/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setObjectName("help")
        self.main_box = QtWidgets.QLabel(self.centralwidget)
        self.main_box.setGeometry(QtCore.QRect(60, 120, 1091, 611))
        self.main_box.setStyleSheet("border-radius: 17px;\n"
"background-color: rgb(167, 145, 203,0.2);")
        self.main_box.setText("")
        self.main_box.setObjectName("main_box")
        self.main_box_2 = QtWidgets.QLabel(self.centralwidget)
        self.main_box_2.setGeometry(QtCore.QRect(90, 150, 1031, 551))
        self.main_box_2.setStyleSheet("border-radius: 17px;\n"
"background-color: rgb(0, 0, 0,0.6);")
        self.main_box_2.setText("")
        self.main_box_2.setObjectName("main_box_2")
        self.settings_title = QtWidgets.QLabel(self.centralwidget)
        self.settings_title.setGeometry(QtCore.QRect(910, 170, 181, 61))
        self.settings_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.settings_title.setStyleSheet("background: transparent;\n"
"font: 25pt \"Montserrat\";\n"
"font-weight: bold;\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignRight;\n"
"")
        self.settings_title.setObjectName("settings_title")
        self.nav_line_2 = QtWidgets.QLabel(self.centralwidget)
        self.nav_line_2.setGeometry(QtCore.QRect(699, 234, 400, 1))
        self.nav_line_2.setStyleSheet("\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop:0 rgba(255, 255, 255, 0),\n"
"    stop:1 rgba(255, 255, 255, 200));")
        self.nav_line_2.setText("")
        self.nav_line_2.setObjectName("nav_line_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 250, 461, 431))
        self.widget.setStyleSheet("background: transparent;")
        self.widget.setObjectName("widget")
        self.courses_title = QtWidgets.QLabel(self.widget)
        self.courses_title.setGeometry(QtCore.QRect(10, 10, 181, 61))
        self.courses_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.courses_title.setStyleSheet("background: transparent;\n"
"font: 23pt \"Montserrat\";\n"
"font-weight: bold;\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignLeft;\n"
"")
        self.courses_title.setObjectName("courses_title")
        self.nav_line_3 = QtWidgets.QLabel(self.widget)
        self.nav_line_3.setGeometry(QtCore.QRect(10, 70, 400, 1))
        self.nav_line_3.setStyleSheet("\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop:0 rgba(255, 255, 255, 200),\n"
"    stop:1 rgba(255, 255, 255, 0));")
        self.nav_line_3.setText("")
        self.nav_line_3.setObjectName("nav_line_3")
        self.checkBox_1 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_1.setGeometry(QtCore.QRect(10, 90, 21, 31))
        self.checkBox_1.setStyleSheet("QCheckBox {\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    font: 12pt \"Montserrat\";\n"
"    color: rgb(195, 195, 195);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #c3c3c3;\n"
"    background: none;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #c3c3c3;\n"
"    background-color: rgb(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    image: url(\"C:/Users/Saanvi Sharma/Documents/PE2/checkmark.png\");\n"
"}\n"
"\n"
"")
        self.checkBox_1.setText("")
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setTristate(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 130, 21, 42))
        self.checkBox_2.setStyleSheet("QCheckBox {\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    font: 12pt \"Montserrat\";\n"
"    color: rgb(195, 195, 195);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #c3c3c3;\n"
"    background: none;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #c3c3c3;\n"
"    background-color: rgb(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    image: url(\"C:/Users/Saanvi Sharma/Documents/PE2/checkmark.png\");\n"
"}\n"
"\n"
"")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 180, 21, 42))
        self.checkBox_3.setStyleSheet("QCheckBox {\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    font: 12pt \"Montserrat\";\n"
"    color: rgb(195, 195, 195);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #c3c3c3;\n"
"    background: none;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #c3c3c3;\n"
"    background-color: rgb(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    image: url(\"C:/Users/Saanvi Sharma/Documents/PE2/checkmark.png\");\n"
"}\n"
"\n"
"")
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 230, 21, 42))
        self.checkBox_4.setStyleSheet("QCheckBox {\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    font: 12pt \"Montserrat\";\n"
"    color: rgb(195, 195, 195);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #c3c3c3;\n"
"    background: none;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #c3c3c3;\n"
"    background-color: rgb(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    image: url(\"C:/Users/Saanvi Sharma/Documents/PE2/checkmark.png\");\n"
"}\n"
"\n"
"")
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.course1 = QtWidgets.QLabel(self.widget)
        self.course1.setGeometry(QtCore.QRect(50, 100, 321, 31))
        self.course1.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.course1.setObjectName("course1")
        self.course2 = QtWidgets.QLabel(self.widget)
        self.course2.setGeometry(QtCore.QRect(50, 140, 321, 31))
        self.course2.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.course2.setObjectName("course2")
        self.course3 = QtWidgets.QLabel(self.widget)
        self.course3.setGeometry(QtCore.QRect(50, 190, 321, 31))
        self.course3.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.course3.setObjectName("course3")
        self.course4 = QtWidgets.QLabel(self.widget)
        self.course4.setGeometry(QtCore.QRect(50, 240, 321, 31))
        self.course4.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.course4.setObjectName("course4")
        self.delete_course_button = QtWidgets.QLabel(self.widget)
        self.delete_course_button.setGeometry(QtCore.QRect(330, 10, 41, 51))
        self.delete_course_button.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.delete_course_button.setText("")
        self.delete_course_button.setPixmap(QtGui.QPixmap(":/images/images for cascade/delete_note_icon.png"))
        self.delete_course_button.setObjectName("delete_course_button")
        self.add_course_button = QtWidgets.QLabel(self.widget)
        self.add_course_button.mousePressEvent = self.openAddCourses
        self.add_course_button.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.add_course_button.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 255, 255,0);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(142, 123, 173);\n"
"}\n"
"")
        self.add_course_button.setText("")
        self.add_course_button.setPixmap(QPixmap(":/images/images for cascade/create_note_icon.png"))
        self.add_course_button.setScaledContents(True)
        self.add_course_button.setObjectName("add_course_button")
        self.edit_course_button_2 = QtWidgets.QLabel(self.widget)
        self.edit_course_button_2.setGeometry(QtCore.QRect(380, 10, 41, 51))
        self.edit_course_button_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.edit_course_button_2.setText("")
        self.edit_course_button_2.setPixmap(QPixmap(":/images/images for cascade/edit_note_icon.png"))
        self.edit_course_button_2.setObjectName("edit_course_button_2")
        self.view_more_courses = QtWidgets.QPushButton(self.widget, clicked = lambda: self.openAddCourses())
        self.view_more_courses.setGeometry(QtCore.QRect(330, 290, 93, 28))
        self.view_more_courses.setStyleSheet("QPushButton {\n"
"    background-color: rgba(185, 185, 185, 0);\n"
"    font: 8pt \"Montserrat\";\n"
"    color: rgb(154, 154, 154);\n"
"    border-radius: 5px;\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(195, 195, 195);\n"
"}\n"
"")
        self.view_more_courses.setObjectName("view_more_courses")
        self.bg.raise_()
        self.logo_bg_shadow.raise_()
        self.logo.raise_()
        self.intro_nav.raise_()
        self.studyplan_nav.raise_()
        self.calender_nav.raise_()
        self.stats_nav.raise_()
        self.faq_nav.raise_()
        self.about_nav.raise_()
        self.contact_nav.raise_()
        self.nav_line.raise_()
        self.homepage.raise_()
        self.help.raise_()
        self.main_box.raise_()
        self.main_box_2.raise_()
        self.settings_title.raise_()
        self.nav_line_2.raise_()
        self.widget.raise_()
        settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 26))
        self.menubar.setObjectName("menubar")
        settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settings)
        self.statusbar.setObjectName("statusbar")
        settings.setStatusBar(self.statusbar)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "MainWindow"))
        self.intro_nav.setText(_translate("settings", "Introduction"))
        self.studyplan_nav.setText(_translate("settings", "Study Plan"))
        self.calender_nav.setText(_translate("settings", "Calendar"))
        self.stats_nav.setText(_translate("settings", "Statistics"))
        self.faq_nav.setText(_translate("settings", "FAQ\'s"))
        self.about_nav.setText(_translate("settings", "About "))
        self.contact_nav.setText(_translate("settings", "Contact"))
        self.settings_title.setText(_translate("settings", "Settings"))
        self.courses_title.setText(_translate("settings", "Courses"))
        self.course1.setText(_translate("settings", "---"))
        self.course2.setText(_translate("settings", "---"))
        self.course3.setText(_translate("settings", "---"))
        self.course4.setText(_translate("settings", "---"))
        self.view_more_courses.setText(_translate("settings", "View more "))

        self.display_coursename()

    def display_coursename(self):
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password123',
            database='cascade_project'
        )
        
        # Fetch the course name from the table
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT name FROM courses")
        course_name = cursor.fetchall()
                
        for i in range(len(course_name)):
                # Check if a course name was fetched
                if course_name[i]:
                        # Dynamically set the course name to the label
                        getattr(self, 'course' + str(i+1)).setText(course_name[i][0])
                else:
                        break

        
        cursor.close()
        conn.close()
                       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = QtWidgets.QMainWindow()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())
