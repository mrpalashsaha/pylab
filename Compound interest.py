import pylab

principle = 10000 # initial investment
interestRate = 0.5
years = 20
values = []

for i in range (years +1 ):
  values.append(principle)
  principle += principle * interestRate
  
  pylab.plot (values)
  
  pylab.title (5% growth, compound annually)
  pylab.xlabel ('years of compounding')
  pylab.ylabel ('value of principle ($)')
  
  pylab.show()
