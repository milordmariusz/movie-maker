import pyttsx3

def comment_to_speach(text, index):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate',180)
    engine.save_to_file(text, f'voices/comments/comment_{index}.mp3')
    engine.runAndWait()
    engine.stop()

def post_to_speach(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate',180)
    engine.save_to_file(text, 'voices/post.mp3')
    engine.runAndWait()
    engine.stop()