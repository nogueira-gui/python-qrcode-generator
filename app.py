from flask import Flask, render_template, request, send_file
import qrcode
import qrcode.constants

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']

    qr = qrcode.QRCode( 
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
        )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')

    filename = 'static/qr.png'
    img.save(filename)

    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)