from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        def do_ping():
            json_ping = json.dumps({'status': 'OK'})
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_ping.encode(encoding='utf_8'))

        if self.path == '/ping':
            do_ping()

        elif self.path == '/start':
            json_data = json.dumps({'status': 'start'})
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode(encoding='utf_8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # input data
        post_data = json.loads(post_data)
        json_game_data = json.dumps({'status': 'data'})
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json_game_data.encode(encoding='utf_8'))


game_service = service.Service()
run(handler_class=HttpGetHandler)
