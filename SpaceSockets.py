#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.cors import CORS
from KnowledgeEng.qdb import mergeNode

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()
import logging

from flask.ext.cors import CORS  # The typical way to import flask-cors

logging.basicConfig(level=logging.INFO)

# One of the simplest configurations. Exposes all resources matching /api/* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin.
CORS(app, resources=r'/api/*', allow_headers='Content-Type')

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)



@app.route('/paradroid/api/v1.0/orders/<int:order_id>', methods = ['GET'])
# @auth.login_required
def get_orders(order_id):
    result = False
    if(order_id % 2):
        result = [{'id': 23, 'comp' : True, 'desc':"Worked fine" },{'id': 32,'comp' : True, 'desc':"Worked fine" },{'id': 32,'comp' : True, 'desc':"Worked fine" }]
    res = mergeNode("Person", '{name:"John", age:45}')
    return jsonify( {'task' : result })

@app.route('/paradroid/api/v1.0/env/<int:ref>', methods=['POST'])
# @auth.login_required
def chanage_env(ref):
    if not request.json or not 'title' in request.json:
        abort(400)
    task = [{
        'id': ref,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    },{
        'id': ref,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    },{
        'id': ref,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    }]
    if(ref % 2):
        task['ans'] = True
    # tasks.append(task)
    return jsonify({'task': task}), 202

@app.route('/paradroid/api/v1.0/env/<name>', methods=['POST'])
# @auth.login_required
def chanage_envName(name):
    if not request.json or not 'title' in request.json:
        abort(400)
    task = [{
        'id': name,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    },{
        'id': name,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    },{
        'id': name,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    },{
        'id': name,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'ans': False
    }]

    # tasks.append(task)
    return jsonify({'task': task}), 202




if __name__ == '__main__':
    app.run(debug = True)