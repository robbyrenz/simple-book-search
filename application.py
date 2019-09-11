from flask import Flask, render_template, request

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    book = request.form.get("book")
    books = db.execute(f"SELECT * FROM books WHERE title LIKE '%{book}%'").fetchall()
    if books is None:  # TODO: this is not working!
        return render_template("results.html", books="Your search came up empty!!!")
    return render_template("results.html", books=books)
