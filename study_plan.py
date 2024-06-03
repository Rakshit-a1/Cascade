# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'study_plan.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import resourcesCascade
import mysql.connector

class Ui_study_plan(object):
    def setupUi(self, study_plan):
        study_plan.setObjectName("study_plan")
        study_plan.resize(1199, 869)
        study_plan.setStyleSheet("background-color: rgb(37, 60, 105);")
        self.centralwidget = QtWidgets.QWidget(study_plan)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1221, 951))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap(":/images/images for cascade/bg_image.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(440, -10, 381, 71))
        self.main_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_title.setStyleSheet("background: transparent;\n"
"font: 24pt \"Montserrat\";\n"
"font-weight: bold;\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.main_title.setObjectName("main_title")
        self.select_course_title = QtWidgets.QLabel(self.centralwidget)
        self.select_course_title.setGeometry(QtCore.QRect(-10, 100, 311, 51))
        self.select_course_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.select_course_title.setStyleSheet("background: transparent;\n"
"font: 17pt \"Montserrat\";\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.select_course_title.setObjectName("select_course_title")
        self.bg_box1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_box1.setGeometry(QtCore.QRect(30, 100, 741, 141))
        self.bg_box1.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(126, 59, 115,0.5);")
        self.bg_box1.setText("")
        self.bg_box1.setObjectName("bg_box1")
        self.bg_box2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_box2.setGeometry(QtCore.QRect(30, 270, 741, 141))
        self.bg_box2.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(112, 72, 163,0.5);")
        self.bg_box2.setText("")
        self.bg_box2.setObjectName("bg_box2")
        self.specify_date_title = QtWidgets.QLabel(self.centralwidget)
        self.specify_date_title.setGeometry(QtCore.QRect(40, 270, 341, 51))
        self.specify_date_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.specify_date_title.setStyleSheet("background: transparent;\n"
"font: 17pt \"Montserrat\";\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.specify_date_title.setObjectName("specify_date_title")
        self.start_date = QtWidgets.QDateEdit(self.centralwidget)
        self.start_date.setGeometry(QtCore.QRect(130, 356, 110, 22))
        self.start_date.setStyleSheet("font: 7pt \"Montserrat\";\n"
"background-color: rgb(50, 24, 92);\n"
"color: rgb(255,255,255,0.7);\n"
"font-weight: 800;")
        self.start_date.setObjectName("start_date")
        self.start_date_title = QtWidgets.QLabel(self.centralwidget)
        self.start_date_title.setGeometry(QtCore.QRect(60, 350, 71, 31))
        self.start_date_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_date_title.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"font-weight: bold;\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.start_date_title.setObjectName("start_date_title")
        self.end_date_title = QtWidgets.QLabel(self.centralwidget)
        self.end_date_title.setGeometry(QtCore.QRect(316, 350, 71, 31))
        self.end_date_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.end_date_title.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"font-weight: bold;\n"
"color: rgb(167, 145, 203);\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.end_date_title.setObjectName("end_date_title")
        self.end_date = QtWidgets.QDateEdit(self.centralwidget)
        self.end_date.setGeometry(QtCore.QRect(380, 356, 110, 22))
        self.end_date.setStyleSheet("font: 7pt \"Montserrat\";\n"
"background-color: rgb(50, 24, 92);\n"
"color: rgb(255,255,255,0.7);\n"
"font-weight: 800;")
        self.end_date.setObjectName("end_date")
        self.nav_line_2 = QtWidgets.QLabel(self.centralwidget)
        self.nav_line_2.setGeometry(QtCore.QRect(50, 145, 700, 1))
        self.nav_line_2.setStyleSheet("background-color: rgb(255, 255, 255,0.5);")
        self.nav_line_2.setText("")
        self.nav_line_2.setObjectName("nav_line_2")
        self.nav_line_3 = QtWidgets.QLabel(self.centralwidget)
        self.nav_line_3.setGeometry(QtCore.QRect(50, 316, 700, 1))
        self.nav_line_3.setStyleSheet("background-color: rgb(255, 255, 255,0.5);")
        self.nav_line_3.setText("")
        self.nav_line_3.setObjectName("nav_line_3")
        self.bg_box3 = QtWidgets.QLabel(self.centralwidget)
        self.bg_box3.setGeometry(QtCore.QRect(30, 450, 741, 261))
        self.bg_box3.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(72, 147, 163,0.3);")
        self.bg_box3.setText("")
        self.bg_box3.setObjectName("bg_box3")
        self.specify_daytime_title = QtWidgets.QLabel(self.centralwidget)
        self.specify_daytime_title.setGeometry(QtCore.QRect(40, 450, 451, 51))
        self.specify_daytime_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.specify_daytime_title.setStyleSheet("background: transparent;\n"
"font: 17pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.specify_daytime_title.setObjectName("specify_daytime_title")
        self.nav_line_4 = QtWidgets.QLabel(self.centralwidget)
        self.nav_line_4.setGeometry(QtCore.QRect(50, 500, 700, 1))
        self.nav_line_4.setStyleSheet("background-color: rgb(255, 255, 255,0.5);")
        self.nav_line_4.setText("")
        self.nav_line_4.setObjectName("nav_line_4")
        self.free_on_title = QtWidgets.QLabel(self.centralwidget)
        self.free_on_title.setGeometry(QtCore.QRect(50, 660, 71, 31))
        self.free_on_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.free_on_title.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.free_on_title.setObjectName("free_on_title")
        self.add_day_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_day_button.setGeometry(QtCore.QRect(650, 530, 93, 28))
        self.add_day_button.setStyleSheet("background-color: rgb(38, 77, 99);\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.add_day_button.setObjectName("add_day_button")
        self.add_day_button.clicked.connect(self.display_days)
        self.add_time_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_time_button.setGeometry(QtCore.QRect(650, 611, 93, 28))
        self.add_time_button.setStyleSheet("background-color: rgb(38, 77, 99);\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.add_time_button.setObjectName("add_time_button")
        self.add_time_button.clicked.connect(self.display_time)
        self.start_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.start_time.setGeometry(QtCore.QRect(130, 616, 118, 22))
        self.start_time.setStyleSheet("font: 7pt \"Montserrat\";\n"
"background-color: rgb(38, 77, 99);\n"
"color: rgb(255,255,255,0.7);\n"
"font-weight: 800;")
        self.start_time.setObjectName("start_time")
        self.start_time_title = QtWidgets.QLabel(self.centralwidget)
        self.start_time_title.setGeometry(QtCore.QRect(60, 610, 71, 31))
        self.start_time_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_time_title.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.start_time_title.setObjectName("start_time_title")
        self.end_time_title = QtWidgets.QLabel(self.centralwidget)
        self.end_time_title.setGeometry(QtCore.QRect(316, 610, 71, 31))
        self.end_time_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.end_time_title.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.end_time_title.setObjectName("end_time_title")

        self.course_dropdown = QtWidgets.QComboBox(study_plan)
        self.course_dropdown.setGeometry(QtCore.QRect(130, 180, 110, 28))
        course_list=self.display_courses()
        self.course_dropdown.addItems(course_list)
        self.course_dropdown.setStyleSheet("font: 8pt \"Montserrat\";\n"
                                        "background-color: rgb(50, 24, 92);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-weight: 600;")
        
        self.day_dropdown= QtWidgets.QComboBox(study_plan)
        self.day_dropdown.setGeometry(QtCore.QRect(130, 530, 110, 28))
        self.day_dropdown.addItems(['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday'])
        self.day_dropdown.setStyleSheet("font: 8pt \"Montserrat\";\n"
                                        "background-color: rgb(38, 77, 99);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-weight: 600;")
        
        self.end_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.end_time.setGeometry(QtCore.QRect(380, 616, 118, 22))
        self.end_time.setStyleSheet("font: 7pt \"Montserrat\";\n"
"background-color: rgb(38, 77, 99);\n"
"color: rgb(255,255,255,0.7);\n"
"font-weight: 800;")
        self.end_time.setObjectName("end_time")
        self.free_days_output = QtWidgets.QLabel(self.centralwidget)
        self.free_days_output.setGeometry(QtCore.QRect(120, 670, 271, 16))
        self.free_days_output.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.free_days_output.setText("")
        self.free_days_output.setObjectName("free_days_output")
        self.free_days_output.setWordWrap(True)
        self.from_title = QtWidgets.QLabel(self.centralwidget)
        self.from_title.setGeometry(QtCore.QRect(390, 660, 71, 31))
        self.from_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.from_title.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.from_title.setObjectName("from_title")
        self.free_hours_output = QtWidgets.QLabel(self.centralwidget)
        self.free_hours_output.setGeometry(QtCore.QRect(450, 670, 271, 16))
        self.free_hours_output.setStyleSheet("background: transparent;\n"
"font: 8pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.free_hours_output.setText("")
        self.free_hours_output.setObjectName("free_hours_output")
        self.whole_studyplan_output = QtWidgets.QTextEdit(self.centralwidget)
        self.whole_studyplan_output.setGeometry(QtCore.QRect(820, 100, 331, 681))
        self.whole_studyplan_output.setStyleSheet("font: 10pt \"Montserrat\";\n"
"color: rgb(195, 195, 195);")
        self.whole_studyplan_output.setObjectName("whole_studyplan_output")
        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(660, 740, 93, 28))
        self.enter_button.setStyleSheet("font: 8pt \"Montserrat\";\n"
"background-color: rgb(87, 60, 138);\n"
"color: rgb(195, 195, 195);")
        self.enter_button.setObjectName("enter_button")
        self.enter_button.clicked.connect(self.inputs)
        self.bg.raise_()
        self.main_title.raise_()
        self.bg_box1.raise_()
        self.select_course_title.raise_()
        self.bg_box2.raise_()
        self.specify_date_title.raise_()
        self.start_date.raise_()
        self.start_date_title.raise_()
        self.end_date_title.raise_()
        self.end_date.raise_()
        self.nav_line_2.raise_()
        self.nav_line_3.raise_()
        self.bg_box3.raise_()
        self.specify_daytime_title.raise_()
        self.nav_line_4.raise_()
        self.free_on_title.raise_()
        self.add_day_button.raise_()
        self.add_time_button.raise_()
        self.start_time.raise_()
        self.start_time_title.raise_()
        self.end_time_title.raise_()
        self.end_time.raise_()
        self.free_days_output.raise_()
        self.from_title.raise_()
        self.free_hours_output.raise_()
        self.whole_studyplan_output.raise_()
        self.enter_button.raise_()
        study_plan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(study_plan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1199, 26))
        self.menubar.setObjectName("menubar")
        study_plan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(study_plan)
        self.statusbar.setObjectName("statusbar")
        study_plan.setStatusBar(self.statusbar)

        self.retranslateUi(study_plan)
        QtCore.QMetaObject.connectSlotsByName(study_plan)

    def retranslateUi(self, study_plan):
        _translate = QtCore.QCoreApplication.translate
        study_plan.setWindowTitle(_translate("study_plan", "MainWindow"))
        self.main_title.setText(_translate("study_plan", "Create Study Plan"))
        self.select_course_title.setText(_translate("study_plan", "Select Course"))
        self.specify_date_title.setText(_translate("study_plan", "Specify date constraint"))
        self.start_date_title.setText(_translate("study_plan", "START:"))
        self.end_date_title.setText(_translate("study_plan", "END:"))
        self.specify_daytime_title.setText(_translate("study_plan", "Specify day and time constraint"))
        self.free_on_title.setText(_translate("study_plan", "Free on:-"))
        self.add_day_button.setText(_translate("study_plan", "Add"))
        self.add_time_button.setText(_translate("study_plan", "Add"))
        self.start_time_title.setText(_translate("study_plan", "START:"))
        self.end_time_title.setText(_translate("study_plan", "END:"))
        self.from_title.setText(_translate("study_plan", "from"))
        self.enter_button.setText(_translate("study_plan", "Enter"))

    def display_courses(self):
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
        course_list=[]
                
        for i in range(len(course_name)):
                course_list.append(course_name[i][0])

        cursor.close()
        conn.close()

        return course_list
    
    def display_days(self):
        selected_day = self.day_dropdown.currentText()  # Get the selected item text
        current_text = self.free_days_output.text()  # Get the current text of the label
        if current_text:
                # Append the new day with a space if the label already has text
                self.free_days_output.setText(current_text + ' ' + selected_day)
        else:
                # Set the text of the label to the selected item if the label is empty
                self.free_days_output.setText(selected_day)

    def display_time(self):
        current_start_time = self.start_time.time()  # This returns a QTime object
        formatted_start_time = current_start_time.toString("HH:mm:ss")  # Format the time as a string

        current_end_time = self.end_time.time()  # This returns a QTime object
        formatted_end_time = current_end_time.toString("HH:mm:ss")  # Format the time as a string

        #selected_day = self.day_dropdown.currentText()  
        current_text = self.free_hours_output.text()  # Get the current text of the label
        if current_text:
                # Append the new day with a space if the label already has text
                self.free_hours_output.setText(current_text + ' ' + formatted_start_time + '-' + formatted_end_time)
        else:
                # Set the text of the label to the selected item if the label is empty
                self.free_hours_output.setText(formatted_start_time + '-' + formatted_end_time)


    def save_information(self,subject, syllabus, study_period, availability_days, time_slots, ability_score):
        prompt_input=f"Create a study plan for {subject} covering {syllabus}. The study period is from {study_period} with availability on {availability_days} from {time_slots}. User ability score: {ability_score}."
        return(prompt_input)
        
    def inputs(self):
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password123',
            database='cascade_project'
        )
        cursor = conn.cursor(buffered=True)

        subject = self.course_dropdown.currentText()

        cursor.execute("SELECT syllabus FROM courses where name = %s",(subject,))
        syllabus = cursor.fetchall()[0][0]

        study_period = self.start_date.date().toString("MMMM d") + " to " + self.end_date.date().toString("MMMM d")

        availability_days = self.free_days_output.text()

        time_slots = self.free_hours_output.text()

        ability_score = 6
        
        if ability_score < 1:
                ability_score = 1
        if ability_score > 15:
                ability_score = 15
        
        if availability_days.lower() == "everyday":
                availability_days= "Monday Tuesday Wednesday Thursday Friday Saturday Sunday"

        return self.save_information(subject, syllabus, study_period, availability_days, time_slots, ability_score)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    study_plan = QtWidgets.QMainWindow()
    ui = Ui_study_plan()
    ui.setupUi(study_plan)
    study_plan.show()
    sys.exit(app.exec_())
