 
import random

class Game:
	def __init__(self):
		self.player = 'Computer'
		self.options = ['Rock','Paper','Scissors']
		self.player_input = None

	def play(self):
		while(self.player_input != 'Q'):
			self.winner = None
			self.comp_input = random.choice(self.options)[0]

			print("Enter choice as :: ")
			print("R --> Rock")
			print("S --> Scissors")
			print("P --> Paper")
			print("Q --> Quit")

			self.player_input = input("Enter here ... ")

			if(self.player_input == self.comp_input):
				print("It's a Tie , No one Wins ")
			
			else:
				if(self.comp_input == 'R' and self.player_input == 'S' and (self.player_input != 'Q')):
					self.winner = "Computer"
				else:
					self.winner = 'Player'			

				if(self.comp_input == 'P' and self.player_input == 'R' and (self.player_input != 'Q')):
					self.winner = "Computer"
				else:
					self.winner = 'Player'			

				if(self.comp_input == 'S' and self.player_input == 'P' and (self.player_input != 'Q')):
					self.winner = "Computer"
				else:
					self.winner = 'Player'		

				if(self.winner):
					print("Winner is ::",self.winner)	

				print(self.comp_input,self.player_input)
				
				print("Press 'A' to play again or Enter 'Q'")

				in_p = input()

				if(in_p):
					if(in_p == 'A'):
						self.play()
					elif(in_p == 'Q'):
						self.player_input = 'Q'
						break
					else:
						print("Wrong Input")				


if __name__ == '__main__':
	rps = Game()
	rps.play()