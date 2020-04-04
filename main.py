import requests
import os
from dotenv import load_dotenv
import argparse

load_dotenv()
TOKEN=os.getenv('TOKEN')


def shorten_link(TOKEN, url):
  shortener_url = 'https://api-ssl.bitly.com/v4/bitlinks'
  headers = {
  'Authorization': 'Bearer {}'.format(TOKEN)
  }
  payload = {
    'long_url': url,
    'title': url,
  }
  response = requests.post(shortener_url, headers=headers, json=payload)

  response.raise_for_status()

  bitlink = response.json()["id"]
  return bitlink


def count_clicks(TOKEN, link):
  counter_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link)
  headers = {
  'Authorization': 'Bearer {}'.format(TOKEN)
  }
  payload = {
    'units': -1,
  }
  
  response = requests.get(counter_url, headers=headers, params=payload)

  response.raise_for_status()

  click_count = response.json()["total_clicks"]
  return click_count


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Позволяет работать с битли')
  parser.add_argument('link', help='Адресс ссылки')
  args = parser.parse_args()
  url = args.link

  if url.startswith('bit.ly/'):
    try:
      clicks_count = count_clicks(TOKEN, url)
    except requests.exceptions.HTTPError:
      print('Введена неправильная ссылка')
    else:
      print('Кликов', clicks_count)

  if url.startswith('http'):
    try:
      bitlink = shorten_link(TOKEN, url)
    except requests.exceptions.HTTPError:
      print('Введена неправильная ссылка')
    else:
      print('Битлинк', bitlink)