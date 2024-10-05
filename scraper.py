import os
import requests

from parsel import Selector
from time import sleep
from dotenv import load_dotenv

'''
- criar uma classe para representar urlo(), organizar melhor o codigo e refatorar a classe noticia
para que possa ser generica.
'''


class Urlo:

  def __init__(self):
    load_dotenv()
    self.news_list = []

  #faz a requisicao
  def makes_requests(self, url):
    try:
      response = requests.get(url, timeout=1)
      sleep(1)

      return response.text if response.status_code == 200 else None
    except requests.exceptions.ReadTimeout:
      return None
    
  #faz a filtragem das informacoes necessarias e cria uma lista de objetos (cada objeto representa uma noticia)
  def urlo(self):
    data = self.makes_requests(os.getenv('URLO'))
    selector = Selector(text=data)

    news_href_link = selector.css('div.post a.post-img::attr(href)').getall()
    news_img_src = selector.css('div.post a.post-img img::attr(src)').getall()
    news_category = selector.css('div.post div.post-body div.post-meta a.post-category::text').getall()
    news_title = selector.css('div.post div.post-body h3.post-title a::text').getall()

    for i in range(len(selector.css('div.col-xs-12 div.col-md-3 div.post').getall())):
      news_index = News()
      news_index.news_href_link = news_href_link[i]
      news_index.news_img_src = news_img_src[i]
      news_index.news_category = news_category[i]
      news_index.news_title = news_title[i]

      self.news_list.append(news_index)


#classe para representar uma noticia
class News:

  def __init__(self):
    self._news_href_link = None
    self._news_img_src = None
    self._news_category = None
    self._news_title = None

  @property
  def news_href_link(self):
    return self._news_href_link
  
  @news_href_link.setter
  def news_href_link(self, news_href_link):
    if not news_href_link: 
      self._news_href_link = None
    else:
      self._news_href_link = news_href_link

  @property
  def news_img_src(self):
    return self._news_img_src
  
  @news_img_src.setter
  def news_img_src(self, news_img_src):
    if not news_img_src:
      self._news_img_src = None
    else:
      self._news_img_src = news_img_src

  @property
  def news_category(self):
    return self._news_category
  
  @news_category.setter
  def news_category(self, news_category):
    if not news_category:
      self._news_category = None
    else:
      self._news_category = news_category

  @property
  def news_title(self):
    return self._news_title
  
  @news_title.setter
  def news_title(self, news_title):
    if not news_title:
      self._news_title = None
    else:
      self._news_title = news_title


#implementacao posterior.
#def urlt():
#  data = makes_requests(os.getenv('URLT'))
