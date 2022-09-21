def read(path):
	with open(path, 'r') as file:
		return file.read().split('\n')

def write(path, arr):
	with open(path, 'w') as file:
		file.write('\n'.join(' '.join(row) for row in arr))

WORDS = read('words_alpha.txt')
words_lens = [[] for _ in range(5)]
segments = [set() for _ in range(7)]
for word in WORDS:
	if 4 <= len(word) <= 8:
		words_lens[len(word)-4] += [word]
		for i in range(2,len(word)+1):
			segments[i-2] |= {word[:i]}

write('words.csv', words_lens)
write('segments.csv', segments)