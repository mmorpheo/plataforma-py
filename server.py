import os
from flask import Flask, send_from_directory, render_template, redirect

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('sitio/index.html')

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')


@app.route('/')
def inicio():
    return render_template('sitio/index.html')



@app.route('/comics')
def comics():
    return render_template('sitio/comics.html')

@app.route('/mangas')
def mangas():
    return render_template('sitio/mangas.html')

@app.route('/tutoriales')
def tutoriales():
    return render_template('sitio/tutoriales.html')






@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/comics')
def admin_comics():
    return render_template('admin/comics.html')

@app.route('/admin/mangas')
def admin_mangas():
    return render_template('admin/mangas.html')

@app.route('/admin/tutoriales')
def admin_tutoriales():
    return render_template('admin/tutoriales.html')

@app.route('/admin/tutoriales/guardar', methods=['POST'])
def admin_tutoriales_guardar():
    print(request.form['txtTituloTutorial'])
    return redirect('/admin/tutoriales')


@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    return render_template('admin/logout.html')

@app.route('/admin/css/style')
def admin_css_style():
    return render_template('admin/css/style.css')


if __name__ == "__main__":
    app.run(port=port)
