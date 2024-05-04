from flask import Flask, jsonify, request, render_template, redirect, url_for
from allocation.adapters import repository
from allocation.service_layer import services
from sqlalchemy import create_engine
from allocation.adapters.orm import metadata, start_mappers
from sqlalchemy.orm import sessionmaker
from allocation.adapters import orm
from allocation.domain import model
from allocation.service_layer import unit_of_work

orm.start_mappers()
orm.create_tables()
#DATABASE_URI = "sqlite:///:memory:"
#engine = create_engine(DATABASE_URI, echo=True)
#metadata.create_all(engine)
app = Flask(__name__)

@app.route("/")
def index():
    message = request.args.get('message', '')
    message_display = f"<p style='color:green;'>{message}</p>" if message else ""
    return f'''
    <h2>Welcome to the Library System!</h2>
    {message_display}
    <p><a href="/add_book">Add a New Book</a></p>
    <p><a href="/add_member">Add a New Member</a></p>
    <p><a href="/borrow_books">Borrow Books</a></p>
    '''

@app.route("/add_book", methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        try:
            id = request.form['id']
            title = request.form['title']
            authors = request.form['authors']
            services.add_book(id, title, authors, unit_of_work.SqlAlchemyBookUnitOfWork())
            return redirect(url_for('index', message='Book successfully added'))
        except KeyError:
            return jsonify({"error": "Missing data in request"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template('add_book.html')

@app.route("/add_member", methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            surname = request.form['surname']
            services.add_member(id, name, surname, unit_of_work.SqlAlchemyMemberUnitOfWork())
            return redirect(url_for('index', message='Member successfully added'))
        except KeyError:
            return jsonify({"error": "Missing data in request"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template('add_member.html')

@app.route("/borrow_books", methods=["GET", "POST"])
def borrow_books_route():
    if request.method == "POST":
        try:
            services.borrow_books(
                request.form["member_id"],
                request.form["book_ids"].split(','),
                unit_of_work.SqlAlchemyMemberUnitOfWork(),
                unit_of_work.SqlAlchemyBookUnitOfWork()
            )
            return redirect(url_for('index', message='Books successfully borrowed'))
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template('borrow_books.html')

if __name__ == "__main__":
    app.run(debug=True)