from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "Фантастика, драма",
        "description": "Команда исследователей путешествует через червоточину в космосе, чтобы обеспечить выживание человечества."
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "Фантастика, боевик",
        "description": "Хакер узнает, что его реальность — это компьютерная симуляция, и присоединяется к восстанию."
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre":"Мультфильм, комедия",
        "description": "Зеленый огр отправляется в путешествие, чтобы спасти принцессу и вернуть свое болото."
    },
    {
        "id": 4,
        "title": "Донни Дарко",
        "year": 2001,
        "rating": 8.0,
        "genre":"Фантастика, драма, триллер",
        "description": "Подросток Донни начинает видеть галлюцинации о гигантском кролике, предсказывающем конец света, и пытается предотвратить надвигающуюся катастрофу."
    },
    {
        "id": 5,
        "title": "Бойцовский клуб",
        "year": 1999,
        "rating": 8.8,
        "genre":"Триллер, драма",
        "description": " Страдающий бессонницей офисный работник встречает харизматичного бунтаря, и вместе они создают подпольный бойцовский клуб, который быстро выходит из-под контроля."
    }
]


@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден", 404

if __name__ == "__main__":
    app.run(debug=True)
