'''
	Deque:A common queue
	Certainly, 'collections.deque' may be a better choice if you want to use.
'''

import pytest

class Deque(object):
	def __init__(self):
		self._elements = []

	def __repr__(self):
		return '<Deque size={!r}>'.format(len(self))

	def append_front(self, x):
		self._elements.insert(0, x)

	def pop_front(self):
		return self._elements.pop(0)

	def append_rear(self, x):
		self._elements.append(x)

	def pop_rear(self):
		return self._elements.pop()

	def __len__(self):
		return len(self._elements)

	def is_empty(self):
		return len(self) == 0

	def clear(self):
		self._elements.clear()

	def front_traverse(self):
		for i in self._elements:
			print('{0} '.format(i), end="")
		print('\n')

	def rear_traverse(self):
		for i in self._elements[::-1]:
			print('{0} '.format(i), end="")
		print('\n')

def main():
	deq = Deque()

	assert deq.is_empty() is True

	deq.append_front('Hello')
	deq.append_front('World')

	assert len(deq) == 2

	deq.front_traverse()
	deq.rear_traverse()

	assert 'World' == deq.pop_front()
	assert 'Hello' == deq.pop_front()

	assert deq.is_empty() is False

	deq.clear()
	assert deq.is_empty() is True

if __name__ == '__main__':
	main()