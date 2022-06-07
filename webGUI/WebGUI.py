from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
class WebGUI:
    def __init__(self):
        print("[WebGUI] Initializing...")
        self.app = Flask(__name__)
        @self.app.route('/')
        def index():
            return render_template('index.html')
        @self.app.route('/test')