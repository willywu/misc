#! /usr/bin/python


class WordBrainSolver(object):
	
	def __init__(self):
		self.board = []
		self.all_words = []
		for i in range(10):
			self.all_words.append([])
		with open('words.txt', 'r') as words_file:
			for word in words_file.readlines():
				clean_word = word.lower().strip()
				if len(clean_word) < 10:
					self.all_words[len(clean_word)].append(word.lower().strip())
	
	def get_board(self):
		default_rows = 3
		print("What is the number of rows? (default=%s)" % default_rows)
		num_rows = int(raw_input() or default_rows)
		for row in range(num_rows):
			print("What are the contents of row #%s? " % (row+1))
			self.board.append(raw_input().lower())
	
	def print_board(self):
		for row in self.board:
			print(row)
			
	def make_createable_words_of_length(self, n):
		creatable_words = []
		board_len = len(self.board)
		for i in range(board_len):
			for j in range(board_len):
				prefix = ""
				taken = []
				potential_words = self.all_words[n][:]
				creatable_words.extend(self.make_words(i, j, potential_words, prefix, taken, n))
		return creatable_words
	
	def make_words(self, i, j, potential_words, prefix, taken, n):
		new_prefix = prefix+self.board[i][j]
		next_potential_words = [word for word in potential_words if word.startswith(new_prefix)]
		new_taken = taken[:]
		new_taken.append((i,j))
		if len(prefix)+1 == n:
			return next_potential_words
		else:
			valid_words = []
			for x_step in [-1, 0, 1]:
				for y_step in [-1, 0, 1]:
					x_to_check = i+x_step
					y_to_check = j+y_step
					if x_to_check >= 0 and x_to_check < len(self.board) and y_to_check >= 0 and y_to_check < len(self.board) and (x_step, y_step) != (0, 0) and (x_to_check, y_to_check) not in new_taken and len(next_potential_words) > 0:
						if len(new_prefix) > 2:
							print("Checking (%s,%s) (%s) for prefix %s with potential words %s and taken %s" % (x_to_check, y_to_check, self.board[x_to_check][y_to_check], new_prefix, next_potential_words, new_taken))
						valid_words.extend(self.make_words(x_to_check, y_to_check, next_potential_words, new_prefix, new_taken, n))
			return valid_words

if __name__=="__main__":
	wbs = WordBrainSolver()
	wbs.get_board()
	print("What word length would you like to find?")
	word_len = int(raw_input())
	creatable_words = wbs.make_createable_words_of_length(word_len)
	for word in creatable_words:
		print(word)
