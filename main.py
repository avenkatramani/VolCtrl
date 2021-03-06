from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import socket 
from thread import *
import time

host ="192.168.0.137"
port =1234

class CircleApp(App):
	def connect(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((host,port))
		self.previous_data = 0
		
	def build(self):
		layout1 = BoxLayout(orientation='horizontal')
		self.e1 = Slider(min=0, max = 100, value=0,orientation='vertical')
		self.txt = Label()
		self.txt.text = 'Volume : '+ '0'
		layout1.add_widget(self.e1)
		layout1.add_widget(self.txt)
		self.e1.bind(value=self.updateValue)
		return layout1
		
	def updateValue(self, nstance,value):
		if int(value) != self.previous_data :
			self.previous_data = int(value)
			self.txt.text = 'Volume : '+str(int(value))
			try:
				self.s.send(str(int(value%100.1)))
			except:
				pass
			
	def recieveData(self):
		while True:
			try:
				data = self.s.recv(1024)
				self.txt.text = 'Volume : '+str(int(data))
				self.e1.value = int(data)
			except:
				pass

c = CircleApp()
c.connect()
start_new_thread(c.recieveData,())
c.run()
