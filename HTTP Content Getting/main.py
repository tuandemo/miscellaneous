from urllib.request import urlopen
import sys, getopt


def usage():
	print("Usage: python3 main.py [options]\n")
	print("Options:")
	print("     -h             \tDisplay the usage and options.")
	print("     --help         \n")
	print("     -i       <url> \tGet <url> from which we get content.")
	print("     --url    <url> \n")
	print("     -o       <file>\tPrint content into <file>")
	print("     --output <file>\n")

def main(argv):
	if not len(argv):
		usage()
		sys.exit(1)
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["help", "url=", "output="])
	except getopt.GetoptError as err:
		usage()
		sys.exit(2)
	url = None
	out = None
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit(0)
		elif opt in ("-i", "--url"):
			url = arg
		elif opt in ("-o", "--output"):
			out = arg
		else:
			pass
	if not url:
		print("Error: URL not found.")
		sys.exit(3)
	response = urlopen(url)
	content = response.read().decode().split("\r\n")
	if not out:
		print("Content from %s:" % (url))
		print(("\n").join(content))
	else:
		f = open(out, "w")
		f.writelines(content)
		print("Content printed successfully into %s." % (out))

if __name__ == "__main__":
	main(sys.argv[1:])