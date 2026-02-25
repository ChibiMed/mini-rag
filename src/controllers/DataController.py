from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os
class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE * 1024 * 1024:
            return False, ResponseSignal.FILE_SIZE_EXCEEDS_LIMIT.value
        
        return True, ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value

    def generate_unique_filename(self, original_file_name: str, project_id: str):

        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        clean_filename = self.get_clean_filename(
            original_file_name=original_file_name
            )

        new_file_path = os.path.join(
            project_path,
            random_key + "_" + clean_filename
            )
        
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + clean_filename
            )
            

        return new_file_path

    def get_clean_filename(self, original_file_name: str):
        # Remove special characters and spaces, keep only alphanumeric and underscores
        clean_name = re.sub(r'[^\w.]', '', original_file_name.strip())
        clean_name = clean_name.replace(" ", "_")  # Replace spaces with underscores
        return clean_name