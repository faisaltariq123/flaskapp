## flask app routing 

from flask import Flask

app=Flask(__name__)

@app.route ("/", methods=["GET"])
def welcome():
    return "<h1>Welcome here</h1>"

@app.route ("/index", methods=["GET"])
def index():
    return "<h2>Welcome to index page</h2>"

@app.route ("/success/<int:score>")
def success(score):
    return "The person got "+ str(score)

@app.route ("/fail/<int:score>")
def fail (score):
    return "The person got "+ str(score)

# @app.route ("/form", methods=["GET","POST"])
# def form (score):
#     return "The person got "+ str(score)


if __name__=="__main__":
    app.run(debug=True)