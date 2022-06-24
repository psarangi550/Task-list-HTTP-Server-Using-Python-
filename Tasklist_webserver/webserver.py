from http.server import HTTPServer,BaseHTTPRequestHandler
from http import HTTPStatus
import cgi
import io

tasklist=["Task 1","Task 2","Task 3"]

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path.endswith("/tasklist"):
            self.send_response(HTTPStatus.OK.value)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
        
            #html section 
        
            output = "<html><body>"
            output += "<h1> TASK LIST </h1>"
            output+='<h3><a href="/tasklist/new">Add a New Task</a></h3>'
            for task in tasklist:
                output += f"{task}&nbsp;&nbsp;<a href='/tasklist/{task}/remove'>Remove Task</a></br>"
            output += "</ul>"
            output += "</body></html>"
        
            self.wfile.write(output.encode('utf-8'))
        
        if self.path.endswith("/new"):
            self.send_response(HTTPStatus.OK.value)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            output = "<html><body>"
            output += "<h1> ADD A NEW TASK</h1>"
            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            output += "<input type='text' name='task'>"
            output += "<input type='submit' value='Add'>"
            output += "</form>"
            output += "</body></html>"
            
            self.wfile.write(output.encode())
        
        if self.path.endswith("/remove"):
            listDirpath=self.path.split("/")[2]
            self.send_response(HTTPStatus.OK.value)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            output = "<html><body>"
            output += "<h1> Remove A TASK</h1>"
            output += f'<form method="POST" enctype="multipart/form-data" action="/tasklist/{listDirpath}/remove">'
            output += "<input type='submit' value='Remove'>"
            output += "</form>"
            output +="<a href='/tasklist'>Cancel</a>"
            output += "</body></html>"
            
            self.wfile.write(output.encode())
            
    
    def do_POST(self):
        if self.path.endswith("/new"):
            ctype,params_dict = cgi.parse_header(self.headers.get('content-type'))
            #setting the boundary as bytes type
            params_dict['boundary']=bytes(params_dict['boundary'],"utf-8")
            #fetching the CONTENT_LENGTH Key in here
            content_length=int(self.headers.get('Content-length'))
            #setting the  CONTENT_LENGTH Key in here
            params_dict["CONTENT_LENGTH"]=content_length

            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile,params_dict)
                new_task=fields.get('task')[0]
                tasklist.append(new_task)
            
            self.send_response(301)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Location','/tasklist')
            self.end_headers()
        
        if self.path.endswith("/remove"):
            listDirpath=self.path.split("/")[2]
            element=listDirpath.replace("%20"," ")
            tasklist.remove(element)
            
            self.send_response(301)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Location','/tasklist')
            self.end_headers()
            
                            
                
def main():
    server=HTTPServer(("",8090),RequestHandler)
    print("Server started at port 8090")
    server.serve_forever()
    server.close()
    print("server being shit down")
    
if __name__ == '__main__':
    main()
