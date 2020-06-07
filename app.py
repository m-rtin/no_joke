import pickle

from flask import Flask, render_template, request, session
from tensorflow.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

MAX_LEN = 50

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        input_text = request.form["input_text"]
        prediction = round(predict(input_text)*100, 2)
        return render_template("result.html", result=prediction)


def predict(text):
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=MAX_LEN)
    score = model.predict([x_test])[0]
    return score[0]


if __name__ == '__main__':
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    model = load_model("model.h5")
    app.run(threaded=False, debug=True)
