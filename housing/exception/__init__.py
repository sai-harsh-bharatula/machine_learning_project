import os
import sys

class exceptionHousing(Exception):
    def __init__(self, errorMessage:Exception, errorDetail: sys):
        super().__init__(errorMessage)
        self.errorMessage=exceptionHousing.getDetailedErrorMessage(errorMessage=errorMessage,
                                                                         errorDetail=errorDetail
                                                                        )
    @staticmethod
    def getDetailedErrorMessage(errorMessage:Exception,errorDetail:sys)->str:
        """
        errorMessage: Exception object
        errorDetail: object of sys module
        """
        _,_ ,exec_tb = errorDetail.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        errorMessage = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{errorMessage}]
        """
        return errorMessage
        
    def __str__(self):
        return self.errorMessage


    def __repr__(self) -> str:
        return exceptionHousing.__name__.str()