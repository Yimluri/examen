from flask import Flask,request,render_template


examen1 = Flask(__name__)

#rutasimpleHTML
@examen1.route('/')
def normal():
   return render_template('ej1.html')

#formulario
@examen1.route('/formulario')
def form():
   return render_template('ej2.html')

#numalcuadrado
@examen1.route('/numeroalcuadrado/<int:num>')
def numeroalcuadrado(num):
   r= num*num
   hola = str(r)
   return 'El cuadrado del número es: '+hola+' .'

@examen1.route('/formulario', methods=['GET'])
def formulario():
    if request.method == 'GET':
        nombre = request.form['nombre']
        edad = request.form['edad']
        print(nombre, edad)
        return 'Datos recibidos en el Server'


@examen1.errorhandler(404)
def error(e):
    return 'No existe'

if __name__ == '__main__':
  examen1.run(port=1000,debug=True)

