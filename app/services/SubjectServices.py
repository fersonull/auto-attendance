import json
import os

class SubjectServices:
    def load_subjects():
        file_path = os.path.join("data", "subjects.json")
        with open(file_path, "r") as file:
            return json.load(file)