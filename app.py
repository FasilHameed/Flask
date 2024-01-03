from flask import Flask,render_template,request

# create simple flask application
app=Flask(__name__)



# url Routing
@app.route("/",methods=["GET"])
def welcome():
    return "<h1>welcome to Flask app</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the index page"

# variable rule parameter for pages as well
# app.route("sucess")

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and the score is:" + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and the score is:" + str(score)

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')


if __name__=="__main__":
    app.run(debug=False)