from flask import render_template,Blueprint,request

from .API import scrape
#======================================
page = Blueprint('page',__name__)

@page.route('/mc-dl')
def mc_dl():
  pkg = scrape.MCDL()
  return render_template('/page/mc-dl.html', pkg=pkg)

@page.route('/source')
def source_code():
  return render_template('/page/source.html')