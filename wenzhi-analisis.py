#python2
# -*- coding: utf-8 -*-
 
from src.QcloudApi.qcloudapi import QcloudApi
 
module='wenzhi'
 
config = {
    'Region': 'my Region',
    'secretId': 'my SecretID',
    'secretKey': 'my SecretKey',
    'method': 'post'
}

'''
action='LexicalAnalysis'
       'TextSentiment'
       'TextClassify'
       'TextKeywords'
       'TextDependency'
       'LexicalSynonym'
       'LexicalCheck'
       'ContentTranscode'
'''
action='TextSentiment'

#different action has differnet params
params={
   'content':'lyrics'
   }
try:
    service = QcloudApi(module, config)
    print service.call(action, params).decode('unicode_escape')
except Exception, e:
    print 'exception:', e
