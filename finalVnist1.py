import speech_recognition as sr
import pygame as pg
import sqlite3
from gtts import gTTS
r = sr.Recognizer()
m = sr.Microphone()
c = 0
ch = 'y'
text2 = "Do you want to continue? ( yes or no )"
pg.mixer.init()
def play_music(music_file, volume=1.0):
    pg.mixer.music.set_volume(volume)
    pg.mixer.music.load(music_file)
    print("Music file {} loaded!".format(music_file))
    clock = pg.time.Clock()
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)
    #try:
    #except pg.error:
    #print("File {} not found! ({})".format(music_file, pg.get_error()))
    return
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while (ch == 'y' or ch =='Y'):
        c = c + 1
        print("Please, say Patient name")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            value1 = r.recognize_google(audio)
            if str is bytes:
                print(u"You said {}".format(value1).encode("utf-8"))
            else:
                print("You said {}".format(value1))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        conn = sqlite3.connect('test.db')
        data = conn.execute("select * from vnist1 where Pname = '" + value1 + "'")
        text  =''
        if(value1 == 'quit'):
            text = "bye"
            print (text)
            speech = gTTS(text,'en')
            file = "a" + str(c) + "gir.mp3"
            speech.save(file)
            music_file = file
            volume = 0.8
            play_music(music_file, volume)
            break;
        for row in data:
            text = "Patient name is " + row[1] + ". The ward number is " + str(row[3]) + ". The room number is " + str(row[4])
        print (text)
        speech = gTTS(text,'en')
        file = "a" + str(c) + "gir.mp3"
        speech.save(file)

        music_file = file
        volume = 0.8
        play_music(music_file, volume)
        print("Do you want to know details of other patient:(y/n):")
        ch = input()

except KeyboardInterrupt:
    pass