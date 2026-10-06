from flask import Flask, render_template, redirect, session
import random

app = Flask(__name__)

app.secret_key= "secret-key"

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
    favorites = session.get("favorites", [])

    return render_template(
        "index.html",
        movies=movies,
        favorites=favorites,
        favorites_count=len(favorites)
    )


@app.route("/add/<int:movie_id>")
def add_favorite(movie_id):

    if "favorites" not in session:
        session["favorites"] = []

    favorites = session["favorites"]

    if movie_id not in favorites:
        favorites.append(movie_id)

    session["favorites"] = favorites

    return redirect("/")

@app.route("/favorites")
def favorites():

    favorite_ids = session.get("favorites", [])

    favorite_movies = []

    for movie in movies:
        if movie["id"] in favorite_ids:
            favorite_movies.append(movie)

    return render_template(
        "favorites.html",
        movies=favorite_movies
    )


@app.route("/remove/<int:movie_id>")
def remove_favorite(movie_id):

    favorites = session.get("favorites", [])

    if movie_id in favorites:
        favorites.remove(movie_id)

    session["favorites"] = favorites

    return redirect("/favorites")

@app.route("/clear")
def clear_favorites():

    session["favorites"] = []

    return redirect("/favorites")

@app.route("/random")
def random_movie():
    movie = random.choice(movies)
    return render_template("random.html", movie=movie)




if __name__ == "__main__":
    app.run(debug=True)
