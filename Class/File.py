#Excel File handler Class
from openpyxl import *

class File:
	def __init__(self):
		pass

	def open(self):
		#opens a Excel File for use in the program
		#will only create an openpyxl file instance
		pass

	def close(self):
		#Closes a Excel File, asking for save before
		#Will likely just delete all references to the Excel file
		#openpyxl has no 'Close'method
		pass

	def new(self):
		#Creates a new openpyxl file, creating all needed sheets
		#Will populate any needed data and will notify main of new
		#file to force update of tables
		pass

	def save(self):
		#saves openpyxl file, This will overwrite file
		pass

	def save_as(self):
		#method to save file as a new name, will be used with
		#New method as well as a menu option. May also have a
		#'Make Copy' method.
		pass
