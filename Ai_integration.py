from PyQt5 import QtWidgets
from mainpage import Ui_mainpage  
from aichatbot import get_gemini_response
import google.generativeai as genai

# Configure the API key for the Gemini AI model
genai.configure(api_key="AIzaSyCMI2Jvlogkvej_KTVbqntq6tUCPZn_nu0")

class MainWindow(QtWidgets.QMainWindow, Ui_mainpage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Initialize the Gemini AI model
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

        # Connect the ai_chat_enter button's clicked signal to the handle_ai_chat_input method
        self.ai_chat_enter.clicked.connect(self.handle_ai_chat_input)

    def handle_ai_chat_input(self):
        question = self.ai_chat_input.text()
        title, response = get_gemini_response(question)
        self.ai_chat.clear()
        self.ai_chat.append(f"<h2 style='color: white;'>{title}</h2>")  # Set text color to white
        for chunk in response:
            self.ai_chat.append(f"<p style='color: white;'>{chunk.text}</p>")  # Set text color to white
        self.ai_chat.append('_' * 80)
        self.ai_chat.append("<h2 style='color: white;'>Chat History</h2>")  # Set text color to white
        for entry in self.chat.history:
            if hasattr(entry, 'question_text') and hasattr(entry, 'response_text'):
                self.ai_chat.append(f"<div style='background-color:#D3D3D3; color: white;'>Q: {entry.question_text}</div>")
                self.ai_chat.append(f"<div style='background-color:#F5F5F5; color: white;'>A: {entry.response_text}</div>")
        self.ai_chat.append('_' * 80)
        self.ai_chat_input.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())