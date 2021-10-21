def logger(verbosity=0):
   def _logger(func):
       def wrapper(*args):
           result = func(*args)
           msg = f'\tcall {func.__name__}'
           if verbosity > 0:
               msg = f'{msg}({", ".join(map(str, args))})'
           if verbosity > 1:
               msg = f'{msg} -> {result}'
           return msg

       return wrapper

   return _logger


@logger(2)
def render_input(field):
   return f'<input id="id_{field}" type="text" name="{field}">'

username_f = render_input('username')
password_f = render_input('password')
print(username_f)
print(password_f)