import subprocess

def stereo_to_mono():
    try:
        subprocess.check_call("cd temp/ && ffmpeg -i stereo_ask.wav -ac 1 mono_ask.wav", shell=True)  
    except subprocess.CalledProcessError:
        print("failed at stereo_to_mono()")

def mono_to_stereo():
    try:
        subprocess.check_call("cd temp/ && ffmpeg -i mono_answer.wav -ac 2 stereo_answer.wav", shell=True)  
    except subprocess.CalledProcessError:
        print("failed at mono_to_stereo()")
      
