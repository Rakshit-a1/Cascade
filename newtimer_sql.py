from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector 
from datetime import datetime, timedelta

class Ui_Timer(object):
    def __init__(self, timer_dialog):
        self.timer_dialog = timer_dialog
        course_list=self.display_courses()
        self.subject_timers = {subject: 0 for subject in course_list}
        self.current_subject = None
        self.start_time = None

    def setupUi(self, Timer):
        self.timer_dialog.setObjectName("Timer")
        Timer.setObjectName("Timer")
        Timer.resize(498, 82)
        Timer.setStyleSheet("background-color: rgb(70, 57, 116);")
        self.start_button = QtWidgets.QPushButton(Timer)
        self.start_button.setGeometry(QtCore.QRect(312, 37, 81, 31))
        self.start_button.setStyleSheet("font: 8pt \"Montserrat\";\n"
                                         "background-color: rgb(99, 75, 137);\n"
                                         "color: rgb(255,255,255);\n"
                                         "font-weight: 1000;\n"
                                         "border-radius : 4;\n"
                                         "")
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(Timer)
        self.stop_button.setGeometry(QtCore.QRect(400, 37, 81, 31))
        self.stop_button.setStyleSheet("font: 8pt \"Montserrat\";\n"
                                        "background-color: gray;\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-weight: 1000;\n"
                                        "border-radius : 4;\n"
                                        "")
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setEnabled(False)  # Initially disabled

        # Connect button signals to slots
        self.start_button.clicked.connect(self.on_start_clicked)
        self.stop_button.clicked.connect(self.on_stop_clicked)

        self.timer_number = QtWidgets.QTimeEdit(Timer)
        self.timer_number.setGeometry(QtCore.QRect(30, 20, 171, 51))
        self.timer_number.setStyleSheet("font: 26pt \"Montserrat\";\n"
                                        "background-color: rgb(50, 24, 92);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-weight: 1000;")
        self.timer_number.setDisplayFormat("mm:ss")
        self.timer_number.setObjectName("timer_number")

        self.dropdown = QtWidgets.QComboBox(Timer)
        self.dropdown.setGeometry(QtCore.QRect(210, 30, 93, 28))
        course_list=self.display_courses()
        self.dropdown.addItems(course_list)

        self.dropdown.setStyleSheet("font: 8pt \"Montserrat\";\n"
                                        "background-color: rgb(50, 24, 92);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-weight: 1000;")

        self.opacity_slider = QtWidgets.QSlider(Timer)
        self.opacity_slider.setGeometry(QtCore.QRect(310, 10, 171, 22))
        self.opacity_slider.setStyleSheet("QSlider::sub-page:horizontal {; background: #634B89;}\n"
                                          "QSlider::add-page:horizontal {; background: #fff;}\n"
                                          "QSlider::handle:horizontal { ; border-radius: 2px; background-color: rgb(50, 24, 92); }\n"
                                          "")
        self.opacity_slider.setMinimum(10)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setSingleStep(10)
        self.opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.opacity_slider.setObjectName("opacity_slider")

        self.retranslateUi(Timer)
        QtCore.QMetaObject.connectSlotsByName(Timer)

        # Initialize QTimer object for countdown
        self.countdown_timer = QtCore.QTimer(Timer)
        self.countdown_timer.timeout.connect(self.update_countdown)

        # Initialize countdown variables
        self.countdown_running = False
        self.countdown_seconds = 0

        # Connect slider signal to slot
        self.opacity_slider.valueChanged.connect(self.set_opacity)

        # Connect accepted and rejected signals of the dialog to slots
        self.timer_dialog.accepted.connect(self.on_dialog_accepted)
        self.timer_dialog.rejected.connect(self.on_dialog_rejected)

    def retranslateUi(self, Timer):
        _translate = QtCore.QCoreApplication.translate
        Timer.setWindowTitle(_translate("Timer", "Dialog"))
        self.start_button.setText(_translate("Timer", "Start"))
        self.stop_button.setText(_translate("Timer", "Stop"))

    def on_start_clicked(self):
        # Disable Start button, enable Stop button
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        # Start the countdown timer
        self.countdown_seconds = self.timer_number.time().second() + (self.timer_number.time().minute() * 60)
        self.countdown_timer.start(1000)  # Timer ticks every second
        self.countdown_running = True

        # Store the start time and current subject
        self.start_time = QtCore.QTime.currentTime()
        self.current_subject = self.dropdown.currentText()

    def on_stop_clicked(self):
        # Enable Start button, disable Stop button
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

        # Stop the countdown timer
        self.countdown_timer.stop()
        self.countdown_running = False

        # Calculate the time spent on the current subject
        end_time = QtCore.QTime.currentTime()
        elapsed_seconds = self.start_time.secsTo(end_time)
        self.subject_timers[self.current_subject] += elapsed_seconds

        # Reset the start time and current subject
        self.start_time = None
        self.current_subject = None

    def update_countdown(self):
        # Update countdown display every second
        if self.countdown_seconds == 0:
            self.countdown_timer.stop()
            self.countdown_running = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.timer_number.setTime(QtCore.QTime(0, 0, 0))
        else:
            self.countdown_seconds -= 1
            self.timer_number.setTime(QtCore.QTime(0, self.countdown_seconds // 60, self.countdown_seconds % 60))

    def set_opacity(self, value):
        opacity = 1 - (value / 100.0)
        self.timer_dialog.setWindowOpacity(opacity)

    def on_dialog_accepted(self):
        # Dialog accepted (e.g., OK button clicked)
        pass

    def update_time(self, subject, time):
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password123',
            database='cascade_project'
        )

        # Create a cursor object
        cursor = conn.cursor(buffered=True)

        # Check if the subject exists
        select_query = "SELECT COUNT(*) FROM timer WHERE subject = %s"
        cursor.execute(select_query, (subject,))
        subject_exists = cursor.fetchone()[0]

        if subject_exists:
            # Update existing row
            update_query = "UPDATE timer SET time = time + %s WHERE subject = %s"
            cursor.execute(update_query, (time, subject))
        else:
            # Insert new row
            insert_query = "INSERT INTO timer(subject, time) VALUES (%s, %s)"
            cursor.execute(insert_query, (subject, time))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close


    def update_or_insert_timer_usage(self, time):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password123',
            database='cascade_project'
        )
        """Updates or inserts timer usage data in the database."""
        cursor = conn.cursor()

        current_date = datetime.now().date()

        # Check if the current date exists in the table
        select_query = "SELECT COUNT(*) FROM time_per_day WHERE day = %s"
        cursor.execute(select_query, (current_date,))
        date_exists = cursor.fetchone()[0]

        if date_exists:
            # Update existing row
            update_query = "UPDATE time_per_day SET time = time + %s WHERE day = %s"
            cursor.execute(update_query, (time, current_date))
        else:
            # Insert new row
            insert_query = "INSERT INTO time_per_day (day, time) VALUES (%s, %s)"
            cursor.execute(insert_query, (current_date, time))

        conn.commit()
        cursor.close()
        conn.close()
    
    def on_dialog_rejected(self):
        # Dialog rejected (e.g., close button clicked)
        # Display total time spent on each subject
        print("Total time spent on each subject:")
        for subject, time_spent in self.subject_timers.items():
            print(f"{subject}: {time_spent} seconds")
            self.update_time(subject,time_spent)
            self.update_or_insert_timer_usage(time_spent)
            

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

        return(course_list)
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Windows")

    timer_dialog = QtWidgets.QDialog()
    ui = Ui_Timer(timer_dialog)
    ui.setupUi(timer_dialog)

    timer_dialog.show()
    sys.exit(app.exec_())

