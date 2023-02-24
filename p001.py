def df(f) :
	def innerf():
		print(f())
	return innerf

def helloworld():
	return "hello"

fu = helloworld
nf = df(fu)

nf()

# if

