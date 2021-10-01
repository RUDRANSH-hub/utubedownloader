from flask import Flask, render_template, request, url_for, redirect, send_file, session
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "rudranshsri"


@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("see_video.html", url = url)
    return render_template("home.html")

@app.route("/see-video",methods=["GET","POST"])
def see_video():
    if request.method=="POST":

        url=YouTube(session['link'])
        itag=request.form.get('itag')
        video=url.streams.get_by_itag(itag)
        file=video.download()
        return send_file(file,as_attachment=True)
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)