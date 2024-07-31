# pip install ollama
# pip install gtts
# pip install mpg123

import ollama
from gtts import gTTS
from mpg123 import Mpg123, Out123

sl = "en"
prompt = "Why is the sky blue?"

stream = ollama.chat(
#    model='llama3.1',
    model='tinyllama',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

text = ""
for chunk in stream:
   content = chunk['message']['content']
   if content!="." and content!="\n":
       text = text + content
   else:
       text = text + content
       print(text)
       tts = gTTS(text, lang=sl)
       tts.save("gTTS.mp3")
       mp3 = Mpg123("gTTS.mp3")
       out = Out123()
       for frame in mp3.iter_frames(out.start):
           out.play(frame)
       text = ""
