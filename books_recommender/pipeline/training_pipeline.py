from books_recommender.components.stage_00_data_ingestion import DataIngestion

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()


    def start_data_ingestion(self):
        """
        Starts the data ingestion stage of the pipeline.
        Function returns None
        """
        self.data_ingestion.initiate_data_ingestion()