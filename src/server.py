from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json
import service.GameService as ssGS
# from src.service.GameService import GameService as ssGS


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
            current_game_data = game_service.search_moves()
            json_data = json.dumps(current_game_data, default=lambda x: x.__dict__)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode(encoding='utf_8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        json_post_move = self.rfile.read(content_length)
        # input data
        print(f'json_post_move {json_post_move}')
        post_move = json.loads(json_post_move)
        print(f'post_move {post_move}')
        game_service.search_moves()
        game_service.do_move(post_move)
        json_game_data = json.dumps(game_service.game_data, default=lambda x: x.__dict__)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json_game_data.encode(encoding='utf_8'))


game_service = ssGS.GameService()
run(handler_class=HttpGetHandler)
