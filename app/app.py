import os
from http.server import BaseHTTPRequestHandler, HTTPServer

name    = os.getenv("STUDENT_NAME", "unknown")
surname = os.getenv("STUDENT_SURNAME", "unknown")
group   = os.getenv("STUDENT_GROUP", "unknown")
sid     = os.getenv("STUDENT_ID", "unknown")

BANNER = f"""================================
DevOps Student Application
================================

Name: {name}
Surname: {surname}
Group: {group}
Student ID: {sid}

Application is running successfully!"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(BANNER.encode())

if __name__ == "__main__":
    print(BANNER, flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
