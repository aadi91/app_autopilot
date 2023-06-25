import matplotlib.pylab as p

s = [35, 25, 20, 10, 10]
k = ['python', 'C++', 'Java', 'JavaScript', 'Ruby']
p.pie(s, labels=k)
p.show()