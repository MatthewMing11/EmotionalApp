# import Kivy
import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from TextAnalysis import main, analyze
emotions=['anger','disgust','fear','guilt','joy','sadness','shame']
class EmoApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="Return")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        btn2 = Button(text="Parse")
        btn2.bind(on_press=self.parseThis)
        layout.add_widget(btn2)
        btn3 = Button(text="Sample 1")
        btn3.bind(on_press=self.sampleOne)
        layout.add_widget(btn3)
        btn4 = Button(text="Sample 2")
        btn4.bind(on_press=self.sampleTwo)
        layout.add_widget(btn4)
        self.lbl1 = Label(text="Enter some text/speech")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "You wrote " + self.txt1.text
    def parseThis(self,btn):
        if(self.txt1.text and self.txt1.text.strip()):
            analyze(self.txt1.text)
            if(analyze.prediction_posneg[0][0]>analyze.prediction_posneg[0][1]):
                emo="This is very negative"
            else:
                emo="This is very positive"
            index=analyze.prediction_multi[0].tolist().index(sorted(analyze.prediction_multi[0])[-2])        
            self.lbl1.text = emo +"\n It is mostly "+emotions[index]
        else:
            self.lbl1.text = "Please enter valid text"
    def sampleOne(self,btn):
        main("hello.wav")
        if(analyze.prediction_posneg[0][0]>analyze.prediction_posneg[0][1]):
            emo="This is very negative"
        else:
            emo="This is very positive"
        index=analyze.prediction_multi[0].tolist().index(sorted(analyze.prediction_multi[0])[-2])        
        self.lbl1.text = emo +"\n It is mostly "+emotions[index]
    def sampleTwo(self,btn):
        main("hello2.wav")
        if(analyze.prediction_posneg[0][0]>analyze.prediction_posneg[0][1]):
            emo="This is very negative"
        else:
            emo="This is very positive"
        index=analyze.prediction_multi[0].tolist().index(sorted(analyze.prediction_multi[0])[-2])        
        self.lbl1.text = emo +"\n It is mostly "+emotions[index]
# run app
if __name__ == "__main__":
    EmoApp().run()
 # join all items in a list into 1 big string
