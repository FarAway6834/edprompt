import builtins as __builtins__;
from functools import wraps as _smart_deco_wrap;
from martialaw.martialaw import partial as _fical

def wither(opener = _fical(open, mode = 'w')):
	def with_deco(func):
		@_smart_deco_wrap(func)
		def with_opener(name, *argv, **kargv):
			with opener(name) as man:
				return func(man, *argv, **kargv)
		return with_opener
	return with_deco

write_the_text_file = wither()(lambda f, x : f.write(x))

class edprompt:
	def __neg__(self):
		res = _
		print(res)
		write_the_text_file(input("save as : "), res)

__builtins__.y = edprompt()