import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import (get_all_orders,
                   get_single_order,
                   create_employee,
                   update_employee,
                   get_all_employees,
                   get_single_employee,
                   create_product,
                   update_product,
                   get_all_products,
                   get_single_product,
                   create_order,
                   update_order,
                   delete_order)

class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)
        response = {}
        (resource, id) = self.parse_url(self.path)
        if resource == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response = get_all_orders()
        elif resource == "employees":
            if id is not None:
                response = get_single_employee(id)
            else:
                response = get_all_employees()
        elif resource == "products":
            if id is not None:
                response = get_single_product(id)
            else:
                response = get_all_products()
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_resource = None
        if resource == 'orders':
            new_resource = create_order(post_body)
        elif resource == 'employees':
            new_resource = create_employee(post_body)
        elif resource == 'products':
            new_resource = create_product(post_body)
        self.wfile.write(json.dumps(new_resource).encode())
    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == 'orders':
            update_order(id, post_body)
        elif resource == 'employees':
            update_employee(id, post_body)
        elif resource == 'products':
            update_product(id, post_body)
        self.wfile.write(''.encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        (resource, id) = self.parse_url(self.path)

        if resource == 'orders':
            self._set_headers(204)
            delete_order(id)
            self.wfile.write(''.encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
