import tkinter as tk
import speech_recognition as sr
import tensorflow as tf
import numpy as np
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences

class TranslationApp:
    def __init__(self, master):
        self.master = master
        master.title("English to Hindi Translator")
        
        self.label = tk.Label(master, text="Click to translate spoken English to Hindi")
        self.label.pack()
        
        self.translate_button = tk.Button(master, text="Translate", command=self.translate)
        self.translate_button.pack()

        self.result_label = tk.Label(master, text="", wraplength=300)
        self.result_label.pack()
        
        self.model = tf.keras.models.load_model('translation_model.h5')
        self.translation_data = self.load_translation_data()

    def load_translation_data(self):
        translation_data = {}
        with open("data6/english.txt", 'r', encoding='utf-8') as f_eng, open("C:data6/hindi.txt", encoding='utf-8') as f_hindi:
            for eng_line, hindi_line in zip(f_eng, f_hindi):
                eng_phrase = eng_line.strip().lower()
                hindi_translation = hindi_line.strip()
                translation_data[eng_phrase] = hindi_translation
        return translation_data

    def translate(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.config(text="Listening...")
            audio = recognizer.listen(source)
            try:
                spoken_text = recognizer.recognize_google(audio)
                self.label.config(text="Recognized: " + spoken_text)

                first_char = spoken_text.strip().split()[0][0].lower()
                if first_char in ['m', 'o']:
                    self.result_label.config(text="Cannot translate words starting with 'M' or 'O'.")
                    return
                
                spoken_text_lower = spoken_text.lower()
                if spoken_text_lower in self.translation_data:
                    translated_text = self.translation_data[spoken_text_lower]
                    print(f"Translated to Hindi: {translated_text}")
                else:
                    print("Translation not found in the dataset.")
                
                sequence = [self.translation_data.get(word, 0) for word in spoken_text.lower().split()]
                padded_sequence = pad_sequences([sequence], maxlen=50, padding='post')
                prediction = self.model.predict(padded_sequence)
                translated_word_index = np.argmax(prediction)
                translated_word = list(self.translation_data.values())[translated_word_index]
                
                self.result_label.config(text="Translated to Hindi: " + translated_word)

            except sr.UnknownValueError:
                self.label.config(text="Sorry, couldn't understand the audio. Please repeat.")
            except sr.RequestError:
                self.label.config(text="Speech recognition service is unavailable.")
            except Exception as e:
                self.label.config(text="Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()

