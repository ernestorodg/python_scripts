
# importing required modules 
import PyPDF2 
import download_all_pdfs

import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import wget
import os

def verificate_string_in_pdf(pdfReader_object, phrase):
	for pages_number in range(pdfReader_object.numPages):
		pageObj = pdfReader.getPage(pages_number)
		if not (pageObj.extractText().find(phrase) == -1):
			return True

	return False


result_list = []
author_and_work = download_all_pdfs.return_author_and_work()


for index in author_and_work:
	if 'Campista' in str(index[0]) or 'Costa' in str(index[0]):

		print(index)

		download_link = index[1]
		author = index[0]


		try:
			wget.download(download_link, 'arquivo.pdf')
		except:
			continue
		# Returns the pdfReader object
		# pdf_name = 'NGO20.pdf'

		# creating a pdf file object 
		pdfFileObj = open('arquivo.pdf', 'rb') 
		  
		# creating a pdf reader object 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


		# Returns true if the pdf contains the phrase 

		if verificate_string_in_pdf(pdfReader_object = pdfReader, phrase = "15/24494-8") == True:
			result_list.append(author)
			print('\nHas the word') 

		# closing the pdf file object 
		pdfFileObj.close() 

		os.remove('arquivo.pdf')

print(result_list)