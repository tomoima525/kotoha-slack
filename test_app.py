# -*- coding: utf-8 -*-
import app

def test_get_request_string():
    assert app.get_request_string('tag', 'Laputa') == \
    'https://kotoha-server.herokuapp.com/api/phrases.json?tag=Laputa'

def test_get_response_string():
    d = {'tag_list': '[Laputa],[Dora]', 'text': 'We leave here in one minute!' }
    assert app.get_response_string(d) == 'We leave here in one minute! from [Laputa],[Dora]'
