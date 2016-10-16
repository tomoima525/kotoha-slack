# -*- coding: utf-8 -*-
import requests
import json
import os
import re
from flask import Flask, url_for, request, redirect, Response

app = Flask(__name__)

URL = 'https://kotoha-server.herokuapp.com/api/phrases.json'

# Check token if you don't want to conflict with other slash commands
#SLACK_KEY =  os.environ['SLACK_KEY']

@app.route('/kotoha',methods=['POST'])
def kotoha():
    """
    Example:
        /kotoha (tag|text) []
    """
    text = request.values.get('text')
    # Check token if you don't want to conflict with other slash commands
    #slack_key = request.values.get('token')
    #if debug is False:
    #    if slack_key != SLACK_KEY:
    #        return 'slack token does not match'
    #else:
    #    print('It\'s debug mode')

    if not text:
        return 'hint: (tag|text) [word]'

    '''parse text'''
    match = re.search('(tag|text)\s*(.*)', text)
    if match:
        kind = match.group(1)
        words = match.group(2)
        if request.method == 'POST':
            tag_param = '{}={}'.format(kind,words)
            req = '?'.join([URL,tag_param])
            query_json = json.loads(requests.get(req).content.decode('utf-8'))
            resp_qs = [':four_leaf_clover: Kotoha for {}:{}\n'.format(kind,words)]
            '''debug'''
            #resp_j = map(get_response_string, query_json)
            #print('response: {}'.format(resp_j))
            '''debug end'''
            resp_qs.extend(map(get_response_string, query_json))
            return Response('\n'.join(resp_qs), content_type='text/plain; charset=utf-8')
    else:
        return 'hint: (tag|text) [words]'

@app.route('/')
def index():
    return redirect('https://github.com/tomoima525')

def get_response_string(qdict):
    return '{} from {}'.format(qdict.get('text'),qdict.get('tag_list'))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=port, debug = debug)
