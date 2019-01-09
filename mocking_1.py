import mock
import itertools

def real(name):
	if len(name) < 10:
		raise ValueError('String too short to calculate statistics.')

	y = ""
	for i in itertools.permutations(range(len(name)), 10):
		y += str(i)
		print(y)

if __name__ == '__main__':
    with mock.patch("itertools.permutations") as m:
        m.return_value = range(5)
        real("afasdfwefr wefrwefr wefrwefr")