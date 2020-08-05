import re
import sys
import requests

def main(argv):
	username = argv[1]
	collection = argv[2]
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
	if len(argv) == 3:
		pattern = r'(/[\d\w]+.jpg)'
		for i in img:
			filename = str(re.findall(pattern, i)[0]).replace('/', '')
			with open(filename, 'wb') as f:
				f.write(requests.get(i).content)
			print('%s saved.' % (filename))
		sys.exit(0)
	data = '\n'.join(img)
	filename = argv[3]
	with open(filename, 'w') as f:
		print(data)
		f.writelines(data)
		print('All pictures of the %s\'s collection "%s" have been saved in %s.' % (username, collection, filename))

def usage():
	print('Usage: python3 main.py <username> <collection> [filename]')

if __name__ == '__main__':
	if len(sys.argv) >= 3:
		main(sys.argv)
		sys.exit(0)
	else:
		usage()
		sys.exit(1)
