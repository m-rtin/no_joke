from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        input_text = request.form["input_text"]
        return render_template("result.html", result=input_text)




if __name__ == '__main__':
    app.run(debug=True)
