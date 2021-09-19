from datetime import datetime
from flask import Flask, render_template, request, Response
import stream
import json
from shared import logger
from main import app

@app.route("/healthcheck")
def healthcheck():
    return "ok"

@app.route('/cam/<camId>/stream', methods=['GET'])
def camstream(camId):
    logger.info("Begin stream")
    return Response(stream.main(camId), mimetype='audio/mpeg4-generic')