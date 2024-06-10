from flask import Blueprint, render_template

views = Blueprint('views',__name__)

# Home Page
@views.route('/')
def view_root():
  return render_template('home.html')
@views.route('/home')
def view_rooot():
  return render_template('home.html')