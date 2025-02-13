# -*- coding: utf-8 -*-
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello krampoline!".encode('utf-8'))


PORT = 3000

with HTTPServer(("", PORT), CustomHandler) as httpd:
    print(f"server port : {PORT} ")
    httpd.serve_forever()
