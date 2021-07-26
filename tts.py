import pyttsx3

def text_to_speech(text, gender):
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()

#Testing....
#text = 'Hello ! My name is Snaeihaa.'
#gender = 'Female'  # Voice assistant 
#text_to_speech(text, gender)

#Nessacary Libraries
#from flask_cors import cross_origin
from flask import Flask, render_template, request
#from main import text_to_speech

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
#@cross_origin()

def homepage():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('frontend.html')
    else:
        return render_template('frontend.html')



if __name__ == "__main__":
    app.run(port=8000, debug=True)