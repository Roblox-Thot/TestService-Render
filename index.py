##########################
#      Config below      #
##########################

save_image:bool = True # Exports the PNG to a file

save_base64:bool = True # Saves the raw Base64 to a file

dump_json:bool = False # do you want the json to be dumped at the end?

##########################
#      Script below      #
##########################

from flask import Flask, request
import json, base64

app:Flask = Flask(__name__)

@app.route('/api/v1/submit_test', methods = ['POST'])
def receive():
    try:
        data = request.data
        data:dict = json.loads(data)
        name:str = data['name']

        if save_image:
            with open(f'{name} Image.png', 'wb') as f: # Outputs the image to (ObjectName) Image.png
                f.write(base64.b64decode(data['image']))

        if save_base64:
            with open(f'{name} Base64.txt', 'w') as f: # Puts the Base64 of the image in (ObjectName) Base64.txt
                f.write('data:image/png;base64,' + data['image'])

        if dump_json:
            with open(f'{name} data.json', 'w') as f:
                json.dump(data, f, indent=4)

        return 'passed' # Tells Studio it passed
    except Exception as e: 
        print(e)
        return 'failed' # Used to tell Studio if it failed (tell me in a issue)

@app.route('/api/v1/alltestfinised', methods = ['POST'])
def bye(): # Only needed to prevent errors
    return ''

@app.route('/<path:p>', methods=['GET', 'POST'])
def all_routes(p): # Catch all just incase
    return ''

@app.route('/', methods=['GET', 'POST'])
def home(): # Prob unneeded but just incase they add a check or something
    return 'OK'

if __name__ == '__main__':
    app.run(port=8001, debug=False)
