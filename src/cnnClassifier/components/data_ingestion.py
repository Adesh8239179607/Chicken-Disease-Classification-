import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.config.configuration import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info:\n {headers}")

        else:
            logger.info(f"File alraedy exists of size:{get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """
        zip file path:str
        extracts the zip file into directory
        fub=nctioinn return none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
