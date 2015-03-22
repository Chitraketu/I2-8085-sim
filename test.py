class hello:
	def __init__(self,name):
		self.file = open(name,'r')
		self.a = self.file.read().split('\n')
	def show(self):
	 	print self.a
hell = hello("file")
hell.show()