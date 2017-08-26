from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.0.137"
port =1234

class CircleApp(App):
	def build(self):
		layout1 = BoxLayout(orientation='horizontal')
		self.e1 = Slider(min=0, max = 100, step = 1, value=0,orientation='vertical')
		self.txt = Label()
		self.txt.text = 'Volume : '+ '0'
		layout1.add_widget(self.e1)
		layout1.add_widget(self.txt)
		self.e1.bind(value=self.updateValue)
		return layout1
	def updateValue(self, nstance,value):
		self.txt.text = 'Volume : '+str(int(value))
		try:
			s.connect((host,port))
			send(str(int(value)).encode()) 
			s.close()
			print('Sent Volume')
		except:
			pass
			
CircleApp().run()
