from flask import Flask,render_template,url_for,request,redirect
app=Flask(__name__,template_folder='templates')
@app.route("/")
def index():
    return render_template("tools.html")
@app.route("/username",methods=["GET","POST"])
def username():
    if request.method=="POST":
        username=request.form.get('username')
        print(username)
        return redirect(url_for('index'))
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
    app.run(debug=True)
