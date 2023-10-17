#!/usr/bin/env python3
from random import choice


def pick(file):
	with open(f'{file}.txt', 'r') as f:
		return choice(f.read().split('\n'))


s = pick("contents/subjects")
m = pick("contents/modifiers")
a = pick("contents/actions")
e = pick("contents/environments")


print(f'\n hmm... draw: {s} {m} {a} {e}')