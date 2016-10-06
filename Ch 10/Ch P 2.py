import pickle
favorites = ['Reading', 'Writing', 'Sleeping', 'Movies']

file = open('favorite.dat', 'wb')
pickle.dump(favorites, file)
file.close()

f = open('favorite.dat', 'rb')
favorites = pickle.load(f)
print(favorites)
