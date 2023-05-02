import pyttsx3
import codecs
import random
import pathlib
from pydub import AudioSegment
import os.path

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150) ### Скорость речи бота - норма 150

Save_Num = random.randint(1, 10000)

try:
    with codecs.open("robotext.txt", "r", "utf-8") as f:
        text = f.read()

    engine.save_to_file(text, "voice%s.ogg" % Save_Num)
    mixed_voice_path = os.path.abspath("voice%s.ogg" % Save_Num)
    print(f"File path: {mixed_voice_path}")
except FileNotFoundError:
    print("Ошибка: файл не найден")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
else:
    engine.runAndWait()
    engine.stop()
    print("Готово")
