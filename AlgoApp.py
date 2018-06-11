# -*- coding:utf-8 -*-
import falcon
import os
import sys
import time

#sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))


from AlgoResource_new import AlgoResource

#from commons.src.elb.elb_resource import ElbResource

def loader():

    start_time = int(time.time())

    algoResource = AlgoResource('config/AIFlyapi_config.yaml')
    # falcon.API instances are callable WSGI apps
    app = falcon.API()
    # caffe_model will handle all requests to the '/caffe_model' URL path
    app.add_route('/AI_server/predict/', algoResource)
    #app.add_route('/elb-healthcheck', elb_resource)
    return app