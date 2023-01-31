import http.server
import socketserver
import queries as q

PORT = 8080

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if '.csv' not in self.path:
            self.path = 'frontend/index.html'
        if self.path == 'get_customer_ranking':
            q.generate_customer_ranking()
        elif self.path == 'get_order_prices':
            q.generate_order_prices()
        elif self.path == 'get_product_customers':
            q.generate_product_customers()
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = HttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()