from flask import Flask, Response, request
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    tts = gTTS(text=text, lang='en')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return Response(mp3_fp, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(port=8089)
