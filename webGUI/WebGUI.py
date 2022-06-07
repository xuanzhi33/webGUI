from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
class websocketHandler(WebSocket):
    def handleMessage(self):
        print(self.data)
        self.sendMessage(self.data)
    def handleConnected(self):
        print(self.address, 'connected')
    def handleClose(self):
        print(self.address, 'closed')

class WebGUI:
    def __init__(self):
        print("[WebGUI] Initializing...")
        self.app = Flask(__name__)
        @self.app.route('/')
        def index():
            return render_template('index.html')
        

    def run(self, host="0.0.0.0", port=5300, debug=False):
        self.app.run(host=host, port=port, debug=debug)
