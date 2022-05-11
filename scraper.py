import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
  count = 0
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  citations = soup.find_all(title="Citations needed")

  for citation in citations:
    count += 1
  print(f'Citation Count: {count}\n')
  return count

def get_citations_needed_report(URL):
  string = ""
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  citations = soup.find_all(title="Citations needed")
  
  for citation in citations:
    string += f'{citation.parent.parent.parent.text}\n'
  print(string)
  return string
  
if __name__ == '__main__':
  URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
  get_citations_needed_count(URL)
  get_citations_needed_report(URL)