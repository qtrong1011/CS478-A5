from flask import Flask, jsonify, request
from datetime import date
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# initialize our Flask application
app = Flask(__name__)
@app.route("/rps", methods=["GET"])
def rps():
    # get the current day and format it
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    #get the name of the image file from client side
    filename = request.args.get('filename')
    # If filename is empty, just return the welcome statement.
    # Otherwise, predict based on model.h5 and send back the result to client.
    if filename != None:
        model = load_model('model.h5')
        img = image.load_img(filename, target_size=(150, 150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        if (classes[0, 0] == 1):
            result = "Paper"
        if (classes[0, 1] == 1):
            result = "Rock"
        if (classes[0, 2] == 1):
            result = "Scissor"
        return "Rock, Paper and Scissors image classification server.\nJason Luu\n" + d2 + "\n" +  "The image you’ve submitted is classified as a: " + result
    else:
        return "Rock, Paper and Scissors image classification server.\nJason Luu\n" + d2
#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)