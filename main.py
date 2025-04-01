from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = "200 OK"

    headers = [("Content-type", "text/plain")]

    start_response(status, headers)

    return [b"Assalomu alaykum Taqsir, 60 ta"]


server = make_server("localhost", 8000, app)
server.serve_forever()