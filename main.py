def blue_eyes(deco):
	def wrapper():
		deco()
		print('Human hese blue eyes')
	return wrapper
  
def red_hair(deco):
	def wrapper():
		deco()
		print('Human hese red hair')
	return wrapper

def height(deco):
	def wrapper():
		deco()
		print('Human hese 180 cm')
	return wrapper


@blue_eyes
@red_hair
@height

def human():
  print('This  is human')
human()

