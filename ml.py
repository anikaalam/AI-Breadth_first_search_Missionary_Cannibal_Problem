import math


class State():


	#creating the blueprint for a state nose 
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None
		#self.counter = 0

	#Defining goal state, i.e when all CM cross over to otherside/(0.0,Right,3,3)
	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	#funtion to check if working node is valid in accrdance problem constraints 

	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False


	#function to allow comparison between current working node and goal state node
	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

     #using hash datastucture to reference 
     #creating node in hash data structure 
     #find out ????              

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))


def successors(cur_state):
	#EQYUIVALENT TO QUEUE 
	children = [];

	#if boat at intial pos(left) 
	#take 2 M to Right side 
	#defining valid moves for when bpat on left
	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		## Two missionaries cross left to right.
		#checking of new state, sucsoosr 
		#checking if each rule match the current state 
		if new_state.is_valid():
			#if not equal to goal then generae succesor from current state
			#enqueue new state to queue called cheldren[]
			new_state.parent = cur_state
			children.append(new_state)

		# when left, take 2 canibals form left to right 
		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		## Two cannibals cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		## One missionary and one cannibal cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		## One missionary crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		## One cannibal crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

    

def breadth_first_search():
	count = 0
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	#frontier is the queue 
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		#deque a vertex from queuw frontier and ?print it
		state = frontier.pop(0)
		if state.is_goal():
			return state
		#mark as visited , i.e add in explored 
		explored.add(state)
		count += 1
		#counter+=1
		

		
		#create succsors of crrent state 


        #get all the adjacent vertives of the dequed/popped vertice "state"
        #if adjacent vertices not visted or in explored, then mark it visted and eqyure it, add it to frontier
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
				count += 1
		print "NumVisNodes"
		print count 

		#numVisitNodes(explored)

	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print "(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                              + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                              str(state.missionaryRight) + ")"

def main():
	solution = breadth_first_search()
	print "Missionaries and Cannibals solution:"
	print "(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)"
	print_solution(solution)

# if called from the command line, call main()
if __name__ == "__main__":
    main()

