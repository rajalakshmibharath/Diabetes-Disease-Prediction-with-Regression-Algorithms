import sys # sys will have all informarion reagarding the exception
from src.logger import logging 

# creating custome error message 
def error_message_detail(error, error_detail:sys): #the error details is present in the sys
		# the error_detail.exc_info returns three variables out of which the third variables gives the info on what is the error, where it occured (which line)
		_,_,exc_tb = error_detail.exc_info()
		file_name = exc_tb.tb_frame.f_code.co_filename
		error_message = "Error occured in the pzthon script name [{0}] line no [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno,str(error))
		
		return error_message

class CustomException(Exception):
	def __init__(self,error_message, error_detail:sys):
		super().__init__(error_message)   #inheriting the init function
		self.error_message = error_message_detail(error_message, error_detail= error_detail)

	def __str__(self):
		return self.error_message