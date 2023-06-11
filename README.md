# Text-to-Speech API

This is a simple Text-to-Speech API using Flask and the Google Text-to-Speech (gTTS) library.

## Installation

1. Install the required packages:

```bash
pip install Flask gTTS
```

## Usage

1. Run the `app.py` file:

```bash
python app.py
```

The API will be available at: `http://localhost:8089/tts`

2. To use the API, make a POST request with a form containing the 'text' parameter.

Example using cURL:

```bash
curl -X POST -F "text=Hello, World!" http://localhost:8089/tts --output output.mp3
```

This will generate an `output.mp3` file with the spoken text.

## API Endpoint

- **POST** `/tts`

  Convert the input text to speech.

  - Form parameters:
    - `text` (required): The text to be converted to speech.

  - Returns:
    - A response with the audio/mpeg content type containing the generated speech as an MP3 file.

  - Error handling:
    - If the 'text' parameter is missing in the request form, the API will return a 400 status code with the message "Missing 'text' parameter in request form".
    - If the input text is empty or contains only whitespace, the API will return a 400 status code with the message "Input text cannot be empty".

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
