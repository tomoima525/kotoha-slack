# -*- coding: utf-8 -*-
import requests
import json
import os
import re
from flask import Flask, url_for, request, redirect

app = Flask(__name__)

MAX_QUESTIONS = 5
URL = 'https://kotoha-server.herokuapp.com/api/phrases.json'

@app.route('/kotonoha',methods=['POST'])
def kotonoha():
    """
    Example:
        /kotonoha (tag|keyword) []
    """
    text = request.values.get('text')

    if not text:
        return 'hint: (tag|keyword) [words]'

    '''parse text'''
    match = re.search('(tag|keyword)\s*(.*)', text)
    if match:
        kind = match.group(1)
        words = match.group(2)
        if request.method == 'POST':
            tag_param = '?{}={}'.format(kind,words)
            req = URL.join(tag_param)
            query_json = json.loads(requests.get(req).content.decode('utf-8'))
            resp_qs = ['Kotonoha for "%s":"%s"\n' % kind,tag]
            '''debug'''
            resp_j = list(map(get_response_string, qj))
            print('¥¥ response: {}'.format(resp_j))
            '''debug end'''
            resp_qs.extend(map(get_response_string, qj))
            return resp_qs
    else:
        return 'hint: (tag|keyword) [words]'

@app.route('/')
def index():
    return redirect('https://github.com/tomoima525')

def get_response_string(q):
    return 'taglist:{}, text:{}'.format(q['tag_list'],q['text'] )

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=port, debug = debug)
