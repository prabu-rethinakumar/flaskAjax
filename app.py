from flask import *
from werkzeug.utils import *
import os
import json
app = Flask(__name__)



app.config['UPLOAD_PATH'] = 'C:\\Users\abcd\Desktop\Python projects\\files'

global globMsg

def format_match(filename):
    if '.' in filename:
        if filename.rsplit('.', 1)[1] in ('xls', 'csv', 'txt'):
            return True


@app.route('/')
def load_page():
    return render_template("main.html")

#Define ajax a sseperate URI
@app.route('/ajax', methods=["GET"])
def return_stat():
    global globMsg
    response = app.response_class(
        response=json.dumps({'message': globMsg}),
        status=200,
        mimetype='application/json'
    )
    return response

#Sample upload functionality
@app.route('/upload', methods=["POST"])
def check_file():
    file = request.files['upld']
    realloc = request.form['restart']
    if format_match(file.filename) and file:
        sec_file = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], sec_file))
        global globMsg
        globMsg = "Validated File"
        return redirect(url_for('get_file', filename=sec_file, restart=restart))
    else:
        return False

#redirect page for Upload activities - write your own logic here
@app.route('/upload/<restart>/<filename>')
def get_file(restart, filename):
    x = YourLogic()
    f = open(os.path.join(app.config['UPLOAD_PATH'], filename), mode='r')
    global globMsg
    fcount = 0
    count = 0
	#Step 1: Do your logic
    globMsg = "Step#1 completed successfully"
    #if result of Step#1 is success - return step1_result = True
    if step1_result is "":
        globMsg = "Step#2 failed: Terminating"
        return json.dumps({"message": globMsg})
    globMsg = "Step#2 in progress"
    for line in f:
        fcount += 1
        try:
            Logic
        except:
            print("invalid data on file : {}".format(line))
            continue
        if result:
            count += 1
    f.close()
    globMsg = "Step#2 successfully completed"
    if count == 0:
        globMsg = "Overall failure - Terminated Processing"
        return json.dumps({"message": globMsg})
    globMsg = "Step#3 started "
    return json.dumps({"message": globMsg})

if __name__ == "__main__":
    app.run(port=9999, debug=False, threaded=True)
