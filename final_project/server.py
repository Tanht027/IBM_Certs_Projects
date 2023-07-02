# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline

import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request


import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    text = translator.englishToFrench(textToTranslate)
    return text
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text = translator.frenchToEnglish(textToTranslate)
    return text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
     return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
