import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import sqlite3
class application(App):
   def build(self):
      layout.add_widget(Button(text = 'connect to database(press once)',on_press = self.connect))
      layout.add_widget(Button(text = 'disconnect',on_press = self.disconnect))
      layout = GridLayout(cols=2)
      layout.add_widget(Label(text='name'))
      self.add1 = TextInput(multiline=False)
      layout.add_widget(self.add1)
      layout.add_widget(Label(text='score'))
      self.add2 = TextInput(multiline=False)
      layout.add_widget(self.add2)
      layout.add_widget(Button(text = 'submit',on_press = self.submit))
      def connect(self,instance):
         connection = sqlite3.connect("scoreboard.db")
         cursor = connection.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (name TEXT, score TEXT)")
      def submit(self,instance):
        submitname = str(self.add1.text)
        submitscore = str(self.add2.text)
        cursor.execute('INSERT INTO scoreboard VALUES ("' + submitname + '", "' + submitscore +'")')
        connection.commit()
      def disconnect(self, instance):
         connection.close()