def parse_file():
	inp = input()
	f = open(inp, "r")
	content = f.read()
	content = content.replace("  ", " ")
	f.close()
	f = open(inp, "w")
	f.write(content)

def main():
	print("Insert file name")
	parse_file()

if __name__ == "__main__":
	main()