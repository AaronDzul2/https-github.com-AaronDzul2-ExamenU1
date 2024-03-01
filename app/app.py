from flask import Flask, render_template, request, redirect

app = Flask(__name__)

datos_per = {
    'nombre': 'Aaron Dzul',
    'carrera': 'Ingeniería en Sistemas y Desarrollador',
}
@app.route('/')
def index():

    return render_template('index.html', datos=datos_per)

@app.route('/Mishabilidades')
def Mishabilidades():

    return render_template('Mishabilidades.html')

@app.route('/Misdatos')
def Misdatos():

    return render_template('Misdatos.html')

@app.route('/comentarios', methods=['GET'])
def mostrar_comentarios():
    
    with open('comentarios.txt', 'r') as file:
        comentarios = file.readlines()
    return render_template('comentarios.html', comentarios=comentarios)

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    nombre = request.form['nombre']
    comentario = request.form['comentario']
    nuevo_comentario = f'{nombre}: {comentario}\n'

    with open('comentarios.txt', 'a') as file:
        file.write(nuevo_comentario)

    return redirect('/comentarios')

if __name__ == '__main__':
    app.run(debug=True)
