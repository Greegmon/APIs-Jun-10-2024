from flask import Flask, render_template

V = "https://hoanghao.me/api/"
def create():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'Bobo mag basa neto'
  
  from .view import views
  app.register_blueprint(views, url_prefix='/')
  from .page import page
  app.register_blueprint(page, url_prefix='/page')
  from .api import api
  app.register_blueprint(api, url_prefix='/api')
  
  @app.errorhandler(404)
  def error_handle(x):
    return render_template('404.html')
  
  return app