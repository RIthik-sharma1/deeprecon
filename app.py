from flask import Flask,render_template,url_for
app=Flask(__name__,template_folder='templates')
@app.route("/")
def index():
    return render_template("tools.html")
@app.route("/username")
def username():
    return render_template("username.html")
@app.route("/email")
def email():
    return render_template("Email.html")
@app.route("/ip_mac")
def ip_mac():
    return render_template("IP MAC.html")
@app.route("/telephone")
def telephone():
    return render_template("phoneno.html")
if __name__=="__main__":
    app.run()
