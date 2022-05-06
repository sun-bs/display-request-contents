from flask import Flask, request
import os
import urllib.parse
app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route('/', defaults={'u_path': ''}, methods=HTTP_METHODS)
@app.route('/<path:u_path>', methods=HTTP_METHODS)
def index(u_path):
    env_name = os.getenv('ENV', 'default env name')
    return f'<h1>{env_name}</h1>' \
           f'<p>' \
           f'method: {request.method}<br>' \
           f'scheme: {request.scheme}<br>' \
           f'server: {request.server}<br>' \
           f'path: {request.path}<br>' \
           f'query: {urllib.parse.unquote(request.query_string.decode())}<br>' \
           f'body: {urllib.parse.unquote(request.get_data().decode())}<br>' \
           f'headers: {request.headers}<br>' \
           f'remote_addr: {request.remote_addr}' \
           f'</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
