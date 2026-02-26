import flask
import os

app = flask.Flask(__name__)

@app.route('/trigger', methods=['GET'])
def trigger_script():
    if os.path.exists('trigger.txt'):
        with open('trigger.txt', 'r') as f:
            command = f.read().strip()
        os.system(command)
        return f"Executed command: {command}", 200
    else:
        return "No trigger file found.", 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)

    