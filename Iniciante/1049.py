A = input('')
B = input('')
C = input('')

if A.lower() == 'vertebrado':
	if B.lower() == 'ave':
		if C.lower() == 'carnivoro':
			print ('aguia')
		elif C.lower() == 'onivoro':
			print ('pomba')
	elif B.lower() == 'mamifero':
		if C.lower() == 'herbivoro':
			print ('vaca')
		elif C.lower() == 'onivoro':
			print ('homem')
if A.lower() == 'invertebrado':
	if B.lower() == 'inseto':
		if C.lower() == 'hematofago':
			print('pulga')
		elif C.lower() == 'herbivoro':
			print('lagarta')
	elif B.lower() == 'anelideo':
		if C.lower() == 'hematofago':
			print('sanguessuga')
		elif C.lower() == 'onivoro':
			print('minhoca')