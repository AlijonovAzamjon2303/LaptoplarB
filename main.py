from app import FrameWorkApp

app = FrameWorkApp()

@app.route("/home")
def home(request, response):
    response.text = "Home pagedan uyquli salom!"

@app.route("/about")
def about(request, response):
    response.text = "About pagedan Azizxonga salom!"

@app.route("/sardor")
def sardor(request, response):
    response.text = "Sardor okadan salom!"

"""
    "/home" : home,
    "/about" : about,
    "/sardor" : sardor
"""