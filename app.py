from flask import *
import subprocess
import os
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/getFromUrl', methods=['POST'])
def getFromUrl():
    path_name = "uploads/"
    if request.method == 'POST':  
        f = request.files['file']
        if os.path.exists(path_name + f.filename):
            os.remove(path_name + f.filename)
        f.save('video.mp4')  
    
    return extractAudioFromVideo('video.mp4')

def extractAudioFromVideo(filename):
    save_path = 'results/audio.mp3'
    if os.path.exists(save_path):
            os.remove(save_path)
    command = "ffmpeg -i "+ filename +" -ab 160k -ac 2 -ar 44100 -vn " + save_path
    subprocess.call(command, shell=True)
    return send_file(save_path, attachment_filename='audio.mp3')

if __name__ == '__main__':
    app.run()