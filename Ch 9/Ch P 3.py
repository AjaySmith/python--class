f = open('C:\\Users\\Anja\\text.txt')
t = f.read()
f.close()

n = open('C:\\Users\\Anja\\new.txt', 'w')
r = n.write(t)
n.close()
