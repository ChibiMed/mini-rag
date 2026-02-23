from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDS_LIMIT = "file size exceeds limit"
    FILE_UPLOADED_SUCCESSFULLY = "file uploaded successfully"
    FILE_UPLOADED_FAILED = "file upload failed"
