def codeHide (filename, shift):
	
	def parse (filename):
		i = 0
		name = ""
		while i < len (filename):
			if filename[i] != '.':
				name += filename[i]
				i += 1
			else:
				break
				
		name += "_hidden"
		
		while i < len (filename):
			name += filename[i]
			i += 1

		return name
			
			
	name = parse (filename)
	f1 = open (filename, "r")
	f2 = open (name, "a")
	for i in f1:
		for j in i:
			f2.write (chr (ord (j) + shift))
		f2.write ("\n")


def codeRetrieve (filename, shift):
	def parse (filename):
		i = 0
		name = ""
		while i < len (filename):
			if filename[i] != '.':
				name += filename[i]
				i += 1
			else:
				break
				
		name += "_original"
		
		while i < len (filename):
			name += filename[i]
			i += 1

		return name
		
	name = parse (filename)
	f1 = open (filename, "r")
	f2 = open ("temp.py", "a")
	
	for i in f1:
		for j in i:
			if j == '\n':
				pass
			else:
				f2.write (chr (ord (j) - shift))
		f2.write ("\n")
	
	
	f2 = open ("temp.py", "r")		
	f3 = open (name, "ab")
	for i in f2:
		temp = i.split (" ")
		del temp[0]
		i = ''.join (temp)
		f3.write (i)
