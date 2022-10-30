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
  
def weight(deco):
	def wrapper():
		deco()
		print('Human hese 60 kg')
	return wrapper

def red_nose(deco):
	def wrapper():
		deco()
		print('Human hese red nose')
	return wrapper

def favorite_color(deco):
	def wrapper():
		deco()
		print('Humans favroite color is red')
	return wrapper


@blue_eyes
@red_hair
@height
@weight
@red_nose
@favorite_color

def human():
  print('This  is human')
human()

