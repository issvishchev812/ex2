from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/list_prof/<prof>')
def q(prof):
    return render_template('index.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
