import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFrame
from PyQt5.QtCore import pyqtSignal, Qt
import resourcesCascade
from PyQt5.QtGui import QFont


class Flashcard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flashcards")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: rgb(57, 138, 189);")

        self.questions = []
        self.answers = []
        self.flashcard_items = []

        self.question_label = QLabel("Question:")
        self.question_label.setFont(QFont('Montserrat', 9, QFont.Bold))  
        self.question_label.setStyleSheet("color: white;")
        self.answer_label = QLabel("Answer:")
        self.answer_label.setFont(QFont('Montserrat', 9, QFont.Bold))  
        self.answer_label.setStyleSheet("color: white;")

        self.question_input = QLineEdit()
        self.question_input.setFont(QFont('Montserrat', 8))  
        self.question_input.setStyleSheet("color: white;")
        self.answer_input = QLineEdit()
        self.answer_input.setFont(QFont('Montserrat', 8))  
        self.answer_input.setStyleSheet("color: white;")

        self.add_button = QPushButton("Add Flashcard")
        self.add_button.setFont(QFont('Montserrat', 9))  
        self.add_button.setStyleSheet("color: white;")
        self.add_button.clicked.connect(self.add_flashcard)

        self.flashcard_layout = QVBoxLayout()
        self.flashcard_layout.setSpacing(10)

        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(self.question_input)
        layout.addWidget(self.answer_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.add_button)

        

        

        for i in range(8):
            flashcard = FlashcardItem(f"Card {i+1}", f"Answer {i+1}")
            self.flashcard_layout.addWidget(flashcard)
            self.flashcard_items.append(flashcard)

        layout.addLayout(self.flashcard_layout)
        self.setLayout(layout)

    def add_flashcard(self):
        question = self.question_input.text()
        answer = self.answer_input.text()

        if question and answer:
            self.questions.append(question)
            self.answers.append(answer)
            self.question_input.clear()
            self.answer_input.clear()
            print("Flashcard added successfully!")
            self.update_flashcards()
        else:
            print("Please provide both question and answer.")

    def update_flashcards(self):
        for i in reversed(range(self.flashcard_layout.count())):
            widget = self.flashcard_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        for q, a in zip(self.questions, self.answers):
            flashcard = FlashcardItem(q, a)
            self.flashcard_layout.addWidget(flashcard)
            self.flashcard_items.append(flashcard)

class FlashcardItem(QFrame):
    clicked = pyqtSignal()

    def __init__(self, question, answer):
        super().__init__()
        self.question = question
        self.answer = answer
        self.is_question = True

        self.setStyleSheet("background-color: #57419a;")

        self.label = QLabel(self.question)
        self.label.setFont(QFont('Montserrat', 10))  
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.mousePressEvent = self.toggle_content

        self.delete_button = QPushButton("Delete")
        self.delete_button.setFixedSize(50, 20)
        self.delete_button.setFont(QFont('Montserrat', 8))  
        self.delete_button.setStyleSheet("color: white;")
        self.delete_button.clicked.connect(self.delete_flashcard)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.delete_button)
        layout.setSpacing(5)
        self.setLayout(layout)

    def toggle_content(self, event):
        if self.is_question:
            self.label.setText(self.answer)
        else:
            self.label.setText(self.question)
        self.is_question = not self.is_question

    def delete_flashcard(self):
        self.setParent(None)  # Remove the flashcard

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Flashcard()
    window.show()
    sys.exit(app.exec_())
