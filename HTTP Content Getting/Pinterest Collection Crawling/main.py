import re
import sys
import requests

def main(argv):
	username = argv[1]
	collection = argv[2]
	filename = argv[3]
	url = 'https://www.pinterest.com/' + username + '/' + collection
	response = requests.get(url)
	try:
		if response.status_code != 200:
			raise Exception("Request Failed.")
	except Exception as err:
		print(err)
		sys.exit(2)
	content = response.content.decode()
	img = []
	while True:
		srcset = content.find('srcSet')
		if srcset == -1:
			break
		content = content[srcset:]
		content = content[content.find('.jpg 1x') + 9:]
		img += [content[:content.find('.jpg 2x') + 4]]
		data = '\n'.join(img)
	with open(filename, 'w') as f:
		print(data)
		f.writelines(data)
		print('All pictures of the %s\'s collection "%s" have been saved in %s.' % (username, collection, filename))

def usage():
	print('Usage: python3 main.py <username> <collection> <filename>')

if __name__ == '__main__':
	if len(sys.argv) == 4:
		main(sys.argv)
		sys.exit(0)
	else:
		usage()
		sys.exit(1)
