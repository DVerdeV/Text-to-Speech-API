from flask import Flask, Response, request
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    # Check if 'text' is present in the request form
    if 'text' not in request.form:
        return Response("Missing 'text' parameter in request form", status=400)

    input_text = request.form['text']
    
    # Check if the input text is empty
    if not input_text.strip():
        return Response("Input text cannot be empty", status=400)

    tts_engine = gTTS(text=input_text, lang='en')
    mp3_buffer = BytesIO()
    tts_engine.write_to_fp(mp3_buffer)
    mp3_buffer.seek(0)
    return Response(mp3_buffer, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(port=8089)
