from flask import (
    Flask,
    jsonify,
    request
)

books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]


app = Flask(__name__)

API_NAME = "/api/v1"


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


@app.route(f"{API_NAME}/books", methods=["GET"])
def list_books():
    """
    list_books --> list al the books
    Args:
    Return:
        books(dict): a book
    """
    return jsonify(books)


@app.route(f"{API_NAME}/books/<book_id>", methods=["GET"])
def get_book_by_id(book_id):
    """
    list_books --> list al the books
    Args:
        book_id(int):
    Return:
        books(dict): a book
    """
    book_to_return = {}
    for book in books:
        if book.get("id") == int(book_id):
            book_to_return = book
            break
    return jsonify(book_to_return)


@app.route(f"{API_NAME}/books", methods=["POST"])
def save_book():
    """
    save_book --> save a book
    Args:
    Return:
    """
    book_json = request.json
    books.append(book_json)
    return jsonify({"message": "The object was saved successfully"})



@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True,
            use_reloader=True,
            port=5000)
