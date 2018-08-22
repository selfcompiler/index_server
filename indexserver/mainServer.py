from flask import Flask, request
import logging
import traceback

import os
import sys
sys.path.append(os.path.join(os.getcwd(), "../"))

from indexserver.helper.index_server_helper import IndexServerHelper

app = Flask(__name__)




@app.route('/initserver', methods=['GET'])
def initializeindex():
    try:
        args = request.args
        #print (args)
        context = str(args['context'])
        gap = int(args['gap'])
        start =  int(args['start'])
        end = int(args['end'])
        IndexServerHelper.initalize_index_table(context,start,end,gap)
        print (context)
        print (gap)
        return "Initialization Completed ,Happy to Server You!! Say thanks to rahul.sk@flipkart.com"
    except Exception as e :
        return "Expected GET to make onboard sequence call http://localhost:8810/initserver?context=<your_context>&start=<start>&end=<end>&gap=<gap> !! Say thanks to rahul.sk@flipkart.com" +str(logging.error(traceback.format_exc()))



@app.route('/nextindex',methods=['GET'])
def nextindex():
    try:
        args = request.args
        context = str(args['context'])
        return IndexServerHelper.getNextIndex(context)
    except:
        print ("Expected GET to index http://localhost:8810/nextindex?context=<your_seq_context> !!")


if __name__ == "__main__":
    app.run(host='10.85.124.158', port=41000)