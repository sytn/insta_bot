import string
import random as rd

def create_pass(length=20, lower=string.ascii_lowercase, upper=string.ascii_uppercase, num=string.digits, symbols=string.punctuation):
	xxx = lower + upper + num + symbols
	temp = rd.sample(xxx, length)
	password = "".join(temp)
	return password