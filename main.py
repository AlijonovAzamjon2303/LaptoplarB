from wsgiref.simple_server import make_server

def app(environ, start_response):
    with open("/Users/azamjon/Desktop/java.jpg", "rb") as file:
        data = file.read()


    status = "200 OK"

    headers = [("Content-type", "image/jpg")]

    start_response(status, headers)

    return [data]


server = make_server("localhost", 8000, app)
server.serve_forever()