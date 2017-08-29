import RPi.GPIO as GPIO    
import socket
import sys
from thread import *
import threading

class Server(object):
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(12, GPIO.OUT)
		self.p = GPIO.PWM(12, 1000)
		self.p.start(50)
		self.host = ''
		self.port = 1234      
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.bind((self.host, self.port))
		self.s.listen(5)
		self.l = threading.Lock()
		self.conns = []
		self.data = '0'

	def threaded_client(self,conn):
		while True:
			try:
				data = conn.recv(1024)
				l.acquire()
				self.data = data
				l.release()
				print(self.data)
			except:
				self.data = ''
			if(not self.data):
				break
			else:
				self.p.ChangeDutyCycle(int(int(self.data)%100.1)))
				for c in self.conns:
					if c != conn:
						try:
							c.send(self.data)
						except:
							pass
		self.conns.remove(conn)
		conn.close()

	def acceptConnection(self):
		while True:
			conn, addr = self.s.accept()
			print('Received new connection')
			conn.send(self.data)
			self.conns += [conn]
			print('Number of connections = ' + str(len(self.conns)))
			start_new_thread(self.threaded_client,(conn,))
            
ser = Server()
ser.acceptConnection()
