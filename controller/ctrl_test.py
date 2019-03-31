"""
Author: José Antonio Domínguez González
Date: 31/03/2019
"""
from flask import Blueprint

# Declare the blueprint which contains the end-poins
test = Blueprint('test', __name__)


@test.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name


@test.route('/sum/<int:n1>/<int:n2>')
def sum(n1, n2):
    """
    Return the sum of the values
    :param n1:
    :param n2:
    :return:
    """
    return str(n1 + n2)


@test.route('/subtraction/<int:n1>/<int:n2>')
def subtraction(n1, n2):
    """
    Return the subtraction of the values
    :param n1:
    :param n2:
    :return:
    """
    return 'The result of {} - {} = {}'.format(n1, n2, n1 - n2)
