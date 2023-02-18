from flask import Flask, jsonify, request, render_template
import os
import converter

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        converter
        return 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
