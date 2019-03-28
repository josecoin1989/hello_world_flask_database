from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

test = Blueprint('test', __name__)


@test.route('/hello/<name>')
def hello(name):
    return 'Hello '+name

@test.route('/sum/<int:n1>/<int:n2>')
def sum(n1,n2):

    return str(n1+n2)

@test.route('/subtraction/<int:n1>/<int:n2>')
def subtraction(n1,n2):

    return 'The result of {} - {} = {}'.format(n1,n2,n1-n2)
