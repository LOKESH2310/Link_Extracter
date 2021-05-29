from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

app = Flask(__name__, template_folder="clients/templates", static_folder= "clients/static")

@app.route('/', methods = ["GET","POST"])
def get():
    if request.method=="GET":
        return render_template("index.html")
    else:
        link=request.form['text']
        req = Request(link)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        dict = {}
        for link in soup.findAll('a'):
            dict[link.text]= link.get('href')
        return render_template("index.html" , links= dict)


if __name__ == "__main__":
    app.run(debug=True)

