from flask import Blueprint, request, jsonify, send_file, render_template
from flask_cors import CORS
import io
import requests
from . import V
from .API import scrape, grees, hola
api = Blueprint('api', __name__)
CORS(api)
@api.route('/')
def A_P_I():
  return render_template('home.html'),200

@api.route('/mc-server')
def random_servers():
  t = scrape.SERVER()
  if 'error' in t:
    return jsonify(t),400
  return jsonify(t),200

@api.route('/catfact')
def random_catfact():
  return jsonify(grees.catfact())


@api.route('/avatar')
def random_avatar():
  text = request.args.get('name')
  Type = request.args.get('type')
  disc = {
    "status": 'error',
    "params":{
      "name=": 'Your avatar name',
      "type=": "There are 5 available avatar types. If the type is not valid, it will default to type 1."
    }
  }
  if not text:
    return jsonify(disc),403
  elif not Type:
    return jsonify(disc),403
  orig = grees.Avatar(text,Set=Type)
  res = requests.get(orig)
  if res.status_code == 200:
    steam = io.BytesIO(res.content)
    return send_file(steam, mimetype='image/jpg'),200
  else:
    return jsonify({'error': 'Failed to fetch your avatar'}),403

@api.route('/tempmail')
def sec_mail():
  action = request.args.get('action')
  if action == 'getMail':
    count = request.args.get('count')
    return grees.secMail(action, count=count)
  elif action == 'getMessages':
    email = request.args.get('email')
    return grees.secMail(action, email=email)
  else:
    return grees.secMail(action)

@api.route('/pinterest')
def search_pinterest():
  q = request.args.get('search')
  if not q:
    return jsonify({"error": 'Tanga mo naman!!'}),403
  else:
    return jsonify(grees.pinterest(q))

@api.route('/ip/<ip>')
def check_ip(ip):
  data = requests.get(f'https://ipinfo.io/{ip}/geo').json()
  return jsonify({
    "city": data['city'],
    "country": data['country'],
    "ip": data['ip'],
    "loc": data['loc'],
    "org": data['org'],
    "postal": data['postal'],
    "region": data['region'],
    "timezone": data['timezone']
  })

@api.route('/genderize')
def api_genderize():
  name = request.args.get('name')
  if name.lower() == 'sheema':
    return jsonify({
      "name": name,
      "gender": 'gay',
      "probability": '69%'
    })
  else:
    return jsonify(grees.genderize(name))

@api.route('/voiceBeast')
def voice_beast():
  query = request.args.get('query')
  if not query:
    return jsonify({"error": 'Missing value'}),403
  return jsonify(grees.voiceBeast(query))

@api.route('/github/<name>')
def github_stalk(name):
  url = f"https://api.github.com/users/{name}"
  res = requests.get(url).json()
  if 'status' in res:
    return jsonify({"status": '404', "message": 'Not Found'}),404
  return jsonify(res),200

@api.route('/insult')
def insult_random():
  url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
  res = requests.get(url).json()
  return jsonify(res),200

@api.route('/joke')
def random_joke():
  res = requests.get('https://official-joke-api.appspot.com/random_joke').json()
  return jsonify(res),200

@api.route('/emojimix')
def country_info():
  x = request.args.get('one')
  y = request.args.get('two')
  url = "https://tenor.googleapis.com/v2/featured?key=AIzaSyAyimkuYQYF_FXVALexPuGQctUWRURdCYQ&contentfilter=high&media_filter=png_transparent&component=proactive&collection=emoji_kitchen_v5&q={}_{}".format(x,y)
  ress = requests.get(url)
  status = ress.status_code
  res = ress.json()
  if 'error' in res:
    return jsonify(res),status
  elif res['locale'] == '':
    return jsonify(res),404
  else:
    return jsonify(res),200

@api.route('/quiz')
def Quiz():
  dif = request.args.get('difficulty')
  if dif not in ['easy', 'medium', 'hard']:
    return jsonify({"status":'error',"error_msg": 'Invalid difficulty, (easy, medium, hard)'}),403
  else:
    respo = grees.quiz(dif)
    return jsonify(respo),200

@api.route('/quote')
def random_quote():
  url = "https://api.quotable.io/random"
  res = requests.get(url).json()
  return jsonify(res),200

@api.route('/fb-download')
def fb_download_video():
  url = request.args.get('url')
  j = hola.FB(url)
  if 'error' in j:
    return jsonify(j),403
  return jsonify(j),200

@api.route('/tiktok/search')
def tiktok_search():
  q = request.args.get('q')
  if not q:
    return jsonify({"error": 'Missing query parameter'}),404
  else:
    Api = '{}tiktok/search?keyword={}'.format(V, q)
    res = requests.get(Api).json()
    if 'error' in res:
      return jsonify({"error": 'OMG may error, oh no!!'}),403
    else:
      return jsonify(res),200