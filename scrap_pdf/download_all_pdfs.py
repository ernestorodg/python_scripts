import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import wget


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


# raw_html = open('pagina.html').read()
raw_html = simple_get('https://www.gta.ufrj.br/publicacoes/')
html = BeautifulSoup(raw_html, 'html.parser')

# for i, dd in enumerate(html.select('dd')):
# 	print(dd.text)
# 	if 'pdf' in dd.text:
# 		print('yes')

# print(html.find('dd').find('a'))



# string = r'<class \'NoneType\'><dd>Master Science Thesis<br/>Author - Sérgio Granato de Araújo<br/>Title - "Estudo, Especificação e Implementação 		de Protocolos para o Plano de Controle da RDSI"<br/>Advisor - Aloysio de Castro Pinto Pedroza <br/>COPPE/PEE/UFRJ - 1993.<br/><p></p></dd>'
# auxiliar_html = BeautifulSoup(string, 'html.parser')
# auxiliar_class_type = type(auxiliar_html.dd.a)
# print(auxiliar_class_type)


def return_author_and_work():
	author_and_work = []
	for dd in html.find_all('dd'):
		content = dd.text
		if (dd.a != None):
			string = str(dd.a.get('href'))
			if 'pdf' in string:
				list = [dd.text, string]
				author_and_work.append(list)

	return author_and_work

# url = author_and_work[0]

# wget.download(url, 'arquivo.pdf')



