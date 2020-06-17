
# importing required modules 
import PyPDF2 
import download_all_pdfs
import requests
import wget
import os
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# Verificate if the atribute (string) can be found on the given pdf object.
# Using PyPDF2
def verificate_string_in_pdf(pdfReader_object, phrase):
	for pages_number in range(pdfReader_object.numPages):
		print('Looking for \"', phrase, '\" in page ', pages_number)
		pageObj = pdfReader.getPage(pages_number)
		if not (pageObj.extractText().find(phrase) == -1):
			return True

	print("Not found")
	return False


result_list = []
author_and_work = download_all_pdfs.return_author_and_work()

# Iterate through the 
for index in author_and_work:

	# Use some filters for the author's name
	if 'Campista' in str(index[0]) or 'Costa' in str(index[0]) or 'Couto' in str(index[0]):
		download_link = index[1]
		author = index[0]

		try:
			wget.download(download_link, 'arquivo.pdf')
		except:
			# In case of 404 or other errors, the for continues on the next loop
			continue

		# creating a pdf file object on eachc loop
		pdfFileObj = open('arquivo.pdf', 'rb') 
		  
		# creating a pdf reader object 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


		# Returns true if the pdf contains the phrase 
		if verificate_string_in_pdf(pdfReader_object = pdfReader, phrase = "15/24494-8") == True:
			result_list.append(author)

		# close the pdf file object 
		pdfFileObj.close() 

		# remove the file so the loop uses the same file name
		os.remove('arquivo.pdf')

# Drop repeated data
works_list = set(result_list)

# Create a .txt files with the given list
f= open("lista_trabalhos_fapesp.txt","w+")

for index in works_list:
     f.write(index + "\n")

f.close()