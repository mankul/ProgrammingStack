from functools import partial
from functools import wraps
# from functools import FrozenSet
def memoize(func):
	
	cache = func.__memo_cache__ = {}
	@wraps(func)
	def memoizer(*args, **kwargs):
		# key = FrozenDict.make_hashable(args, kwargs)
		key = frozenset(args)
		if key not in func.__memo_cache__:
			print("creating new key")
			cache[key] = func(*args, **kwargs)
		return cache[key]
	return memoizer

@memoize
def getByServerID(serverID):
	print("get by server ID")
		

def main():
	for i in range(10):
		print(getByServerID(i))
	for i in range(10):
		print(getByServerID(i))


if __name__ == "__main__":
	main()