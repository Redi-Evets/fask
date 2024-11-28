from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'idercervant@gmail.com'  # Tu correo de Gmail
app.config['MAIL_PASSWORD'] = 'xnjd asqr yeal pjlf'  # Contraseña de aplicación
app.config['MAIL_DEFAULT_SENDER'] = 'idercervant@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        # Crear el mensaje de correo
        msg = Message('Nuevo mensaje desde el formulario de contacto',
                      recipients=['idercervant@gmail.com'])  # El correo que recibirá el mensaje
        msg.body = f'Nombre: {nombre}\nCorreo: {email}\nMensaje: {mensaje}'
        
        # Enviar el correo
        try:
            mail.send(msg)
            return '¡Correo enviado exitosamente!'
        except Exception as e:
            return f'Ocurrió un error: {str(e)}'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
