import sys

def collectInputs(no, TYPE="int"):
	if len(sys.argv) <= no:
		inps = " ".join( [ "<inp{}>".format(i) for i in range(no)] )
		print(f"Usage {__file__} {inps} ")
		sys.exit(1)

	if TYPE == "int":
		return [ int(i) for i in sys.argv[1:no+1]] 
	else:
		return sys.argv[1:no+1]