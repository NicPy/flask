class Lab():
	def __init__(self, config):
		self.config = [
			x.strip() for x in config]
		self.walls = []
		self.entry = None
		self.exit = None
		for y, row in enumerate(self.config):
			for x, ch in enumerate(row):
				if ch == '#':
					self.walls.append((x, y))
				elif ch == '@':
					self.entry = (x, y)
					self.walls.append((x, y))
				elif ch == '$':
					self.exit = (x,y)
		self.path = []
		self.height = len(self.config)
		self.width = len(self.config[0])



	def get_directions(self, position, ignore=None):
		x, y = position
		directions = []
		ignore = ignore or []
		if x > 0 and (x-1, y) not in self.walls + ignore:
			directions.append((x-1, y))
		if y > 0 and (x, y-1) not in self.walls + ignore:
			directions.append((x, y-1))
		if x < self.width and (x+1, y) not in self.walls + ignore:
			directions.append((x+1, y))
		if y < self.height and (x, y+1) not in self.walls + ignore:
			directions.append((x, y+1))
		return directions

	def move(self, position, ignore=None):
		# print(position)
		# self.path.append(position)
		ignore = ignore or []
		directions = self.get_directions(position, ignore=ignore)
		for d in directions:
			if d == self.exit:
				# print(" CHECKED")
				return [position, self.exit]

			if d not in ignore:
				result = self.move(d, ignore=ignore+[position])
				if result:
					return [position] + result

	def build_path(self):
		self.path = self.move(self.entry)
		
	def draw(self):
		for y, row in enumerate(self.config):
			for x, ch in enumerate(row):
				print('*' if (x, y) in self.path else ch, end='')
			print()

with open("field.txt", "r") as f:
	lab = Lab(f.readlines())
	# print(lab.move(lab.entry))
	# print(lab.get_directions((1, 2), ignore=[(0, 1)]))

	print(lab.build_path())
	lab.draw()