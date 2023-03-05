@app.route("/quotes/<int:id>", methods=['DELETE'])
def delete(id):
    connection = get_db()
    cursor = connection.cursor()
    quote_db = cursor.fetchone()
    cursor.execute(quote_db)
    connection.commit()
    quotes = []
    keys = ["id", "author", "text"]
    quote = dict(zip(keys, quote_db))
    quotes.append(quote)
    for quote in quotes:
        if id == quote['id']:
            quotes.remove(quote)
            return f"Quote with id {id} is deleted.", 200
    abort(404, f"Указанного id= {id}, не существует")