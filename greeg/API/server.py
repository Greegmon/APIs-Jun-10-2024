from bs4 import BeautifulSoup as Soup
import requests as req
import random

def mc_server():
  page = random.randint(1,1032)
  url = f"https://minecraftservers.org/index/{page}"
  head = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'}
  res = req.get(url,headers=head).text
  soup = Soup(res, 'html.parser')
  
  def g2(CP):
    xx = '_'.join(CP[0].text.lower().split(' '))
    if xx == 'discord':
      B_ = CP[1].find('a')['href']
    else:
      B_ = CP[1].text
    return [xx, B_]
  def g3(CP):
    xj = CP[0].text.lower()
    if xj == 'tags':
      aa = [x.text for x in CP[1].find_all('a')]
      return [xj, ' '.join(aa)]
    else:
      aa = CP[1].text
      return [xj, aa.strip()]
  
  server_list = soup.find('section',class_='server-list')
  lists = server_list.find_all('div',class_='server-listing')
  xxx = [x.get('data-id') for x in lists]
  servers_id = [random.choice(xxx)]
  for ID in servers_id:
    data = {}
    data['server_id'] = ID
    
    murl = 'https://minecraftservers.org/server/{}'.format(ID)
    RES = req.get(murl,headers=head).text
    SOUP = Soup(RES, 'html.parser')
    
    ctn = SOUP.find('div', class_='container-lg')
    div_main = ctn.find('div', class_='col-md-25')
    div_cont = ctn.find('div', class_='col-md-47')
    Title = div_main.find('div',class_='header-bar')
    data['server_name'] = Title.find('div').text
    
    sInfo = div_main.find('div',class_='server-info')
    Suka = sInfo.find_all('div',class_='row')
    for kij in Suka:
      nsjs = kij.find_all('div')
      if len(nsjs) == 2:
        data[g2(nsjs)[0]] = g2(nsjs)[1].strip()
      else:
        data[g3(nsjs)[0]] = g3(nsjs)[1]
    
    oo = random.choice(['classic','sunset','ocean','ice','nether '])
    iizn = "https://status.minecraftservers.org/{}/{}.png".format(oo, ID)
    data['banner_stats'] = iizn
    Info = div_cont.find('div',id='info')
    zn = Info.find('img')['src']
    jzu = Info.find('p').text
    data['banner'] = f"https://minecraftservers.org{zn}"
    data['info'] = jzu.strip()
    
    return data