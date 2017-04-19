# coding=utf-8
import json
from django.http import HttpResponse


def HttpJSONResponse(js):
    return HttpResponse(json.dumps(js),
                        content_type='application/json')


def NormalResp(d={}):
    return HttpResponse(json.dumps({'c': 0, 'd': d}),
                        content_type='application/json')
