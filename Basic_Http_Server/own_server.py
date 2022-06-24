from http.server import HTTPServer,BaseHTTPRequestHandler
from http import HTTPStatus
import json
import io
host="localhost"
port=8092

data=[
    {
        "eno":101,
        "ename":"Rika",
        "esal":50000,
        "eaddr":"Banglore"
    },
    {
        "eno":102,
        "ename":"Abismruta",
        "esal":60000,
        "eaddr":"Hsr Layout"
    }
]

class PratikServe(BaseHTTPRequestHandler):
    
    def set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def do_GET(self):
        self.set_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def do_POST(self):
        all_data=self.headers.get('content-length')
        required_data=json.loads(self.rfile.read(int(all_data)))
        data.append(required_data)
        self.set_headers()
        self.wfile.write(json.dumps({"result":"success"}).encode("utf-8"))
        
        
def run_server():
    server=HTTPServer((host,port),PratikServe)
    print("server started at port 8092")
    server.serve_forever()
    server.close()
    print("server been shut down")
    

if __name__=="__main__":
    run_server()