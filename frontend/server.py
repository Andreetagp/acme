import http.server
import socketserver

PORT = 8080

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'frontend/web/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()