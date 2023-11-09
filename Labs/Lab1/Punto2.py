#CALCULANDO TU PESO EN OTROS MUNDOS
g_marte = 3.711
g_jupiter = 24.79
g_luna = 1.622
peso_tierra = float(input('Digite su Peso en Kilogramos: '))
masa = peso_tierra / 9.8
peso_marte = masa * g_marte
peso_jupiter = masa * g_jupiter
peso_luna = masa * g_luna
print('SU PESO EN LA LUNA ES {} Kg.'.format(peso_luna))
print('SU PESO EN JÚPITER ES {} Kg.'.format(peso_jupiter))
print('SU PESO EN MARTE ES {} Kg.'.format(peso_marte))