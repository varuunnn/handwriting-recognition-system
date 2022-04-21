from flask import Flask, render_template, request
import os
from main import main
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        img = request.files['imagefile']
        img_path = "../images/" + img.filename
        img.save(img_path)
        result = main(img_path)
        print(result)
        os.remove(img_path)
        return render_template('upload.html', prediction=result)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)