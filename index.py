from flask import Flask, request
import json, base64

app = Flask(__name__)

@app.route('/api/v1/submit_test', methods = ['POST'])
def receive():
    try:
        data = request.data
        data = json.loads(data)
        with open("Base64.txt", "w")  as f: # Puts the Base64 of the image in Base64.txt
            f.write("data:image/png;base64,"+data['image'])
        with open("Image.png", "wb")  as f: # Outputs the image to Image.png
            f.write(base64.b64decode(data['image']))
        return "passed" # Tells Studio it passed
    except:
        return "failed" # Used to tell Studio if it failed (tell me in a issue)

@app.route('/api/v1/alltestfinised', methods = ['POST'])
def bye(): # Only needed to prevent errors
    return ""

if __name__ == '__main__':
    app.run(port=8001)
