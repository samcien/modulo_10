from flask import Flask, jsonify, redirect, url_for, request, render_template
from words import words

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/see_dictionary')
def ver_diccionario():
    return jsonify({"Diccionario": words})


@app.route('/add_word', methods=['GET', 'POST'])
def agregar_palabra():
    if request.method == 'POST':
        palabra = request.form['word']
        significado = request.form['meaning']

        words.append({'palabra': palabra, 'significado': significado})
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('agregar_palabra.html')


@app.route('/edit_word', methods=['GET', 'POST'])
def editar_palabra():
    if request.method == 'POST':
        palabra = request.form['word']
        significado = request.form['meaning']
        for word in words:
            if word['palabra'] == palabra:
                palabra_encontrada = [word]
                if len(palabra_encontrada) > 0:
                    words.remove(palabra_encontrada[0])
                    words.append({'palabra': palabra, 'significado': significado})
                    return render_template('index.html')
    return render_template('editar_palabra.html')


@app.route('/delete_word', methods=['GET', 'POST'])
def borrar_palabra():
    if request.method == 'POST':
        palabra = request.form['word']
        for word in words:
            if word['palabra'] == palabra:
                palabra_encontrada = [word]
                if len(palabra_encontrada) > 0:
                    words.remove(palabra_encontrada[0])
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('eliminar_palabra.html')


@app.route('/search_word', methods=['GET', 'POST'])
def buscar_palabra():
    if request.method == 'POST':

        palabra_1 = request.form['word']

        for word in words:
            if word['palabra'] == palabra_1:
                palabra_encontrada = [word]
                if len(palabra_encontrada) > 0:
                    return jsonify({"Palabra: ": palabra_encontrada[0]})

    return render_template('buscar_palabra.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
