# me first flask application

#from flask import Flask, request, session, render_template
from flask import Flask, session, render_template, url_for, request, redirect

app = Flask(__name__)

# Sessions variables are stored client side, on the users browser
# the content of the variables is encrypted, so users can't
# actually see it. They could edit it, but again, as the content
# wouldn't be signed with this hash key, it wouldn't be valid
# You need to set a scret key (random text) and keep it secret
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


# example of multiple urls resolving to a single template
@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)

@app.route("/shopping")
def shopping():
    food = ["cheese","tuna","beef","toothpaste"]
    return render_template("shopping.html", food=food)

@app.route("/bacon",methods=['GET','POST'])
def bacon():
    if request.method == 'POST':
        return 'you are using POST - method used: %s' % request.method
    else:
        return "you're probably using GET - method used: %s" % request.method

@app.route('/tuna')
def tuna():
    return '<h2>Tune is Good!!!</h2>'

# a string
@app.route('/myname/<username>')
def myname(username):
    return 'Hey there %s' % username

# must be an integer
@app.route('/post/<int:post_id>')
def foo(post_id):
    return 'my Postie Id is %s' % post_id

# ----------  TEMPLATE STUFF ---------------------

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


# ----------  START IT UP  ---------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
