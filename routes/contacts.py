from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    return render_template('index.html')


@contacts.route('/new')
def add_contac():
    return render_template('about.html')


@contacts.route('/update')
def update():
    return render_template('about.html')


@contacts.route('/delete')
def delete():
    return render_template('about.html')
