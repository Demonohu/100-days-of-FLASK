from flask import *
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['SECRET_KEY'] = 'oyigiyigi'
app.config["UPLOAD_FOLDER"] = 'uploaded_media/'

@app.route('/') 
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():
    f = request.files['file']
    filename = secure_filename(f.filename)
    if filename == '':
        return redirect('/')
        
    else:
        isValid = False
        while not isValid:
            print("Ensure that there's no space in the filename and the file is in jpg or JPEG format(i.e, the filename should end with .theformat say jpg)")
            filename = input("What do you want to call your file? ")
            if ' ' not in filename and (filename[-4:].lower() == '.jpg' or filename[-5:].lower() == '.jpeg' ):
                isValid = True

        f.save(app.config['UPLOAD_FOLDER'] + filename)
        return render_template('success.html', name = filename)
            
  
if __name__ == '__main__':  
    app.run(debug = True)  