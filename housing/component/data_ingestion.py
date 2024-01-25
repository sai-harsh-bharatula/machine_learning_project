from housing.exception import exceptionHousing
import sys,os
from housing.logger import logging
from housing.entity.config_entity import DataIngestionConfig



class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise exceptionHousing(e,sys)
        
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try : 
            pass
        except Exception as e:
            raise exceptionHousing(e, sys)    