from http.server import HTTPServer,BaseHTTPRequestHandler
from http import HTTPStatus

class EchoHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())
        

def main():
    server=HTTPServer(("",8090),EchoHandler)
    print("Server started at port 8090")
    server.serve_forever()
    server.close()
    print("server being shit down")
    
if __name__ == '__main__':
    main()
