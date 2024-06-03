import google.cloud.location
import base64
import vertexai
import re
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models




from PyQt5 import QtWidgets
from study_plan import Ui_study_plan 
from file3 import cleaned_response



class StudyPlannerWindow(QtWidgets.QMainWindow, Ui_study_plan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.enter_button.clicked.connect(self.multiturn_generate_content)

    def multiturn_generate_content(self):
        self.text1_1 = self.inputs()
        vertexai.init(project="673460396526", location="northamerica-northeast1")
        model = GenerativeModel(
            "projects/673460396526/locations/northamerica-northeast1/endpoints/1202311566926544896",
        )
        chat = model.start_chat()

        response = chat.send_message([self.text1_1])

        return response
    


    def output(self):
      self.whole_studyplan_output.setPlainText(str(cleaned_response))


    def get_response(self):
        return self.response
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Create the study planner window
    study_planner_window = StudyPlannerWindow()
    study_planner_window.show()

    # Run the application event loop
    sys.exit(app.exec_())

