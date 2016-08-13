#!/usr/bin/env python

from bokeh.server.server import Server
from bokeh.command.util import build_single_handler_applications

#imports to run my server
from bokeh.embed import autoload_server #to put bokeh in the flask app
from flask import Flask,render_template, redirect, url_for, request,session
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload
import sys
from collections import OrderedDict
import threading
import time

#setup flask 
flaskApp = Flask(__name__)
flaskApp.debug = True

#initialize some values, sanatize the paths to the bokeh plots
files = ['bokeh/ex1.py','bokeh/ex2.py']
argvs = {}
urls = []
for i in files:
    argvs[i]=None
    urls.append(i.split('/')[-1].split('.')[0])
host = 'localhost'
app_port = 5567
bokeh_port = 6060

def run_bokeh_server(bok_io_loop):
    ##turn file paths into bokeh apps
    apps = build_single_handler_applications(files,argvs)
    ##args lifted from bokeh serve call to Server, with the addition of my own io_loop
    kwags = {
        'io_loop':bok_io_loop,
        'generade_session_ids':True,
        'redirect_root':True,
        'use_x_headers':False,
        'secret_key':None,
        'num_procs':1,
        'host':['%s:%d'%(host,app_port),'%s:%d'%(host,bokeh_port)],
        'sign_sessions':False,
        'develop':False,
        'port':bokeh_port,
        'use_index':True
    }
    srv = Server(apps,**kwags)


@flaskApp.route('/',methods=['GET']) #a sample page to display the bokeh docs
def graph_page():
    #pull the bokeh server apps
    bokeh_scripts = {} 
    for plot in urls:
        bokeh_scripts[plot]=autoload_server(model=None, url='http://%s:%d'%(host,bokeh_port), app_path="/"+plot) # pulls the bokeh apps off of the bokeh server

    #order the plots
    all_divs= OrderedDict()
    all_divs.update(bokeh_scripts)
    all_divs = OrderedDict(sorted(all_divs.items(), key=lambda x: x[0]))

    #throw the plots on a jinja2 template
    return render_template('graph_template.html',div_dict=all_divs)


def rest_of_tornado(io_loop_here):
    ##a test to see if I can shutdown while the server is running. This will eventually get a button somewhere.
    print('starting countdown')
    time.sleep(300)
    print('countdown finished') 
    io_loop.stop()


if __name__ == "__main__":
    #initialize the tornado server
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(flaskApp)
    )
    http_server.listen(app_port)
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(io_loop)

    #call the turn off test
    nadostop = threading.Thread(target=rest_of_tornado,args=(io_loop,))
    nadostop.start()
    
    #add the io_loop to the bokeh server
    run_bokeh_server(io_loop)
    print('starting the server on http://%s:%d/'%(host,app_port))

    #run the bokeh server
    io_loop.start()
