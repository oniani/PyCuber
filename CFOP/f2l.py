import _import
from cube import *


def push_right(c):
	return sequence("R Ui Ri", c)

def push_left(c):
	return sequence("Li U L", c)

def pull_right(c):
	return sequence("R U Ri", c)

def pull_left(c):
	return sequence("Li Ui L", c)