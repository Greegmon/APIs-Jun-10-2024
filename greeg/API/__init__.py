import json
import requests
import random

from .server import mc_server

class download:
  def FB(self, fb):
    url = f"https://hoanghao.me/api/facebook/download?url={fb}"
    res = requests.get(url).json()
    if 'error' in res:
      if res['error'].startswith('T'):
        return {"error": 'Missing fb link'}
      else:
        return {"error": 'Invalid fb link'}
    else:
      return res
class bulalo:
  def catfact(self):
    try:
      url = "https://catfact.ninja/fact"
      res = requests.get(url).json()
      return {"text": res['fact']}
    except Exception as e:
      return {"error": e}
  def Avatar(self, text, Set='1'):
    if not text:
      return {'error': 'Missing text parameter'}
    url = f"https://robohash.org/{text}?set=set{Set}&bgset={random.choice(['bg1','bg2'])}"
    return url
  def secMail(self, action, email='', count='1'):
    try:
      if action == 'getMessages':
        url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={email.split('@')[0]}&domain={email.split('@')[1]}"
        res = requests.get(url).json()
        return res
      elif action == 'getMail':
        url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={count}"
        res = requests.get(url).json()
        return res
      else:
        err = {
          "error_msg": 'Invalid action parameter',
          "action=": 'getMessages, getMail',
          "action": {
            "getMail": {
              "&count=": 'amount of email you want to generate',
              "example": "/tempmail?action=getMail&count=5"
            },
            "getMessages": {
              "&email=": 'Mail name you want to see inbox messages',
              "example": "/tempmail?action=getMessages&email=EXAMPLE@gmail.com"
            }
          }
        }
        return err
    except Exception as e:
      return {"error_msg": e}
  def pinterest(self, search):
    try:
      url = "https://hoanghao.me/api/pinterest?search={}".format(search)
      res = requests.get(url).json()
      if 'error' in res:
        return {"error": 'Failed to fetch data'}
      else:
        return res
    except Exception as jk:
      return {"error": jk}
  def genderize(self, name):
    try:
      if not name:
        return {"name": name, "gender": '??', 'probability': 0}
      url = f"https://api.genderize.io/?name={name}"
      ress = requests.get(url)
      res = ress.json()
      data = {
        "name": name,
        "gender": res['gender'],
        "probability": str(res['probability']).split('.')[1] + "%"
      }
      return data
    except Exception as e:
      return {"error": str(e)}
  def voiceBeast(self, query):
    url = f'https://www.api.vyturex.com/beast?query={query}'
    res = requests.get(url).json()
    return res
  def quiz(self, dif):
    url = "https://opentdb.com/api.php?amount=1&encode=url3986&type=boolean&difficulty=%s"%(dif,)
    res = requests.get(url).json()
    return res

class grape:
  def MCDL(self):
    array = [{'date': '20-09-2022', 'download': 'https://mcpedl.org/uploads_files/20-09-2022/minecraft-1-19-30.apk'}, {'date': '04-10-2022', 'download': 'https://mcpedl.org/uploads_files/04-10-2022/minecraft-1-19-31.apk'}, {'date': '03-11-2022', 'download': 'https://mcpedl.org/uploads_files/03-11-2022/minecraft-1-19-41.apk'}, {'date': '29-11-2022', 'download': 'https://mcpedl.org/uploads_files/29-11-2022/minecraft-1-19-50.apk'}, {'date': '13-12-2022', 'download': 'https://mcpedl.org/uploads_files/13-12-2022/minecraft-1-19-51.apk'}, {'date': '07-02-2023', 'download': 'https://mcpedl.org/uploads_files/07-02-2023/minecraft-1-19-60.apk'}, {'date': '14-03-2023', 'download': 'https://mcpedl.org/uploads_files/14-03-2023/minecraft-1-19-70.apk'}, {'date': '17-03-2023', 'download': 'https://mcpedl.org/uploads_files/17-03-2023/minecraft-1-19-71.apk'}, {'date': '26-04-2023', 'download': 'https://mcpedl.org/uploads_files/26-04-2023/minecraft-1-19-80.apk'}, {'date': '27-04-2023', 'download': 'https://mcpedl.org/uploads_files/27-04-2023/minecraft-1-19-81.apk'}, {'date': '11-07-2023', 'download': 'https://mcpedl.org/uploads_files/11-07-2023/minecraft-1-20-10.apk'},{'date': '16-08-2023', 'download': 'https://mcpedl.org/uploads_files/16-08-2023/minecraft-1-20-15.apk'},{'date': '19-09-2023', 'download': 'https://mcpedl.org/uploads_files/19-09-2023/minecraft-1-20-30.apk'}, {'date': '26-09-2023', 'download': 'https://mcpedl.org/uploads_files/26-09-2023/minecraft-1-20-31.apk'}, {'date': '24-10-2023', 'download': 'https://mcpedl.org/uploads_files/24-10-2023/minecraft-1-20-40.apk'}, {'date': '02-11-2023', 'download': 'https://mcpedl.org/uploads_files/02-11-2023/minecraft-1-20-41.apk'}, {'date': '05-12-2023', 'download': 'https://mcpedl.org/uploads_files/05-12-2023/minecraft-1-20-50.apk'}, {'date': '14-12-2023', 'download': 'https://mcpedl.org/uploads_files/14-12-2023/minecraft-1-20-51.apk'}, {'date': '06-02-2024', 'download': 'https://mcpedl.org/uploads_files/06-02-2024/minecraft-1-20-60.apk'},{'date': '12-03-2024', 'download': 'https://mcpedl.org/uploads_files/12-03-2024/minecraft-1-20-71.apk'}, {'date': '23-04-2024', 'download': 'https://mcpedl.org/uploads_files/23-04-2024/minecraft-1-20-80.apk'}, {'date': '29-04-2024', 'download': 'https://mcpedl.org/uploads_files/29-04-2024/minecraft-1-20-81.apk'}]
    This = []
    for arr in array:
      data = {}
      if 'download' in arr:
        data['version'] = '.'.join(arr['download'].split('/')[5][10:17].split('-'))
        data['link'] = arr['download']
      else:
        pass
      This.append(data)
    return This
  def SERVER(self):
    try:
      return mc_server()
    except Exception as e:
      return {"error": e}

hola = download()
grees = bulalo()
scrape = grape()