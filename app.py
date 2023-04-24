from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def gracie_template():
    return render_template("index2.html")


@app.route("/about")
def about_me():
    return render_template("about_me.html")
    
@app.route("/major")
def gracie_major():
    return render_template("major.html")
    
@app.route("/artist")
def fav_artist():
    return render_template("fav_artist.html")
    
@app.route("/job")
def job_title():
    return render_template("job.html")

    
    

  
    



    
    
    