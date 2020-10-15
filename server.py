import http.server
import socketserver
import urllib.parse as urlparse
import pprint

Handler = http.server.SimpleHTTPRequestHandler

class HttpHandler(Handler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        request = {
            'ip': self.address_string(),
            'path': parsed_path.path,
            'query': parsed_path.query,
            'version': self.server_version,
            'sys_version': self.sys_version,
            'protocol_version': self.protocol_version,
            'headers': {},
        }

        for name, value in sorted(self.headers.items()):
            request["headers"][name] = value
        
        pprint.pprint(request)


def main():
    server = socketserver.TCPServer((HOST, PORT), HttpHandler)
    print("Running at", PORT)
    server.serve_forever()


if __name__ == '__main__':
    HOST, PORT = "", 8080
    main()
