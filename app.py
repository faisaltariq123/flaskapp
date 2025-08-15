## flask app routing 

from flask import Flask, render_template, request, redirect, url_for

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

@app.route ("/form", methods=["GET","POST"])
def form ():
    if request.method=='GET':
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        avg_marks = (maths+science+history)/3
        if avg_marks>=50:
            res='success'
        else:
            res='fail'

        return redirect(url_for(res,score=avg_marks))

        #return render_template('form.html', score=avg_marks)

if __name__=="__main__":
    app.run(debug=True)