from flask import Flask, session, request, flash, redirect, url_for, render_template, send_from_directory

app= Flask(__name__)

app.secret_key="soul"

VALID_USER="admin"
VALID_PASS="1234"




books=[
    {'id':1, 'title': 'гарри поттер', 'author':'джоан роулинг', 'year':2001},
    {'id':2, 'title': 'учебник английского', 'author':'Анастасия Путилина', 'year':2008}
]

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/books')
def books_list():
    return render_template('books.html', books=books)


@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = None
    for item in books:
        if item["id"] == book_id:
            book = item
            break

    if book:
        return render_template("books_detail.html", book=book)
    else:
        return "книга не найдена", 404


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year=request.form['year']

        new_book = {
            "id": len(books) + 1,
            "title": title,
            "author": author,
            "year": year
        }

        books.append(new_book)

        flash('книга добавлена', 'success')

        return redirect(url_for('books_list'))

    return render_template("add_book.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == VALID_USER and password == VALID_PASS:
            session['logged_in'] = True
            session['username'] = username
            flash('вы вошли в систему', 'success')
            return redirect(url_for('add_book'))
        else:
            flash('вы не вошли в систему', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('вы вышли из системы', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)