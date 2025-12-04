from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template('myform.html')
@app.route("/submit",methods=["POST"])
def submit():
    name=request.form['username']
    return render_template('greet.html',name=name)
app.run(debug=True)