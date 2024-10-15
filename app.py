import requests
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']= "jpbahjbhjjhblsfnbvlhhjjsuh"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bible.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    chap_num = db.Column(db.Integer, nullable=False)
    verse_num = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        book_name = request.form.get("name")
        chap = request.form.get("chapter")
        verse = request.form.get("verse")


        
        if not book_name:
            return render_template("index.html")
        else:
            book_name_obj = Book(name=book_name, chap_num=chap, verse_num=verse)
            db.session.add(book_name_obj)
            db.session.commit()



    Bible = Book.query.all()



    url = "https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-kjv/books/{}/chapters/{}/verses/{}.json"

    

    book_id = []
    

    for bik in Bible:
        repiti = requests.get(url.format(bik.name, bik.chap_num, bik.verse_num)).json()


        bike = {
            'bik': bik.name,
            'chap': bik.chap_num,
            'ver': bik.verse_num,
            'text': repiti['text']
        }
        book_id.append(bike)
    

 



    
    return render_template("index.html", pages=book_id)


if __name__ == "__main__":
    app.run(debug=True)