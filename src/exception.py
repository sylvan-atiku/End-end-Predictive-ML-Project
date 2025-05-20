import sys   # library for managing the runtime environment
from src.logger import logging  # custom logger for logging messages
#create a functions to push errors raised into custom exception message

def error_message(error: str, error_detail:sys):
    """"
    the function above gets tht errors  and error details within the runtime environment of the sys
    """
    exc_tb=error_detail.exc_info()
    file_name:str = exc_tb.tb_frame.f_code.co_filename
    error_message: str = "Error occurred in python script name [{0}] and line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))


class CustomException(Exception):
    def __init__(self,error_message: str, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divided by zero")
        raise CustomException(e, sys)