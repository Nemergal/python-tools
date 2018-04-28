units = [ 'o', 'b', 'ko', 'kb', 'mo', 'mb', 'go', 'gb', 'to', 'tb' ]

def base_to(val, base='o', to='go'):
	base = base.lower()
	to = to.lower()

	try:
		val = int(val)
	except:
		raise ValueError('Value must be a number')

	if base not in units or to not in units:
		raise ValueError('Invalid argument(s)')

	base_index = units.index(base)
	to_index = units.index(to)

	if base_index == to_index:
		return val
	else:

		if base_index % 2 != 0 and to_index % 2 == 0: # base = Xb et to Xo
			base_index = base_index - 1
		elif base_index % 2 == 0 and to_index % 2 != 0: # base = Xo et to Xb
			to_index = to_index - 1

		operations_count = int((to_index - base_index) / 2)

		result = val
		for i in range(0, abs(operations_count)):
			if operations_count > 0:
				result = result / 1024
			elif operations_count < 0:
				result = result * 1024
		return result