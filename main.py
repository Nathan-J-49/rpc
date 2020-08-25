from random import choice

class RPS:
	def __init__(self):
		self.opt = ['rock', 'paper', 'scissors']
		self.usr_score = 0
		self.cpu_score = 0
		self.rules = {
			'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'
			}
		self.match()
	def err(self,msg):
		print(f"ERROR: {msg}")
	
	def disp_score(self):
		print(f"SCORES:\n\tYOU: {self.usr_score} \n\tCPU: {self.cpu+score}\n")

def ask(self):
	for i in range(len(self.opt)):print(f"{i + 1}.{self.opt[i]}")
	usr = input("\nSelect 1 option:  ")
	try: usr = int(usr) - 1
	except ValueError:
	self.err("invalid. must input number\n")
	return self.ask()
	if -1 < usr < len(self.opt): returnself.opt[usr]
	else:
		self.err(f"input invalid. seriously? number between 1 and {len(self.opt)}!\n")
		return self.ask()

#def next week!!!!!!!!!