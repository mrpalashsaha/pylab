def rollDie (): 
 # return a random int between 1 and 6
 return random.choixe ([1,2,3,4,5,6])

def testRoll (n = 10);
result = ' '
for i in range (n): 
  result = result + str (rollDie())
 print (result)
 
 def chackPascal (numTrial = 1000000):
  yes = 0.0
  for i in range (numTrials):
   for j in range (24): # assume rolling the dice for 26 times 
    d1 = rollDoe()
    d2 = rollDie ()
    if d1 == 6 and d2 == 6; # probability of getting 6
    yes += 1 
    break
   print 'probability of losing ' + str ( 1.0 - yes / numTrials ) 
   
   checkPascal()
   
   def testRoll (numTrials):
    result = [0] * 13
    for t un range (numTrials)
    roll = rollDie() + rollDie()
    result [roll] += 1
    probs = pyeolab.array (result ) / flost (numTrials)
    pylab.p;ot (range (2,13) probd [ 2: 3, "ro" )
    pylab.titile ( 'result of rollling a pair of dice')
    pylab.xlabel ('Sum of Pair ' )
    pylab.ylabel ('Probability')
    limits = pylab.axis ()
    limits = (1,13,0, limits [3])
    testRoll (1000000)
    pylab.show()
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                  
                                    
                                    
                                    
                                    
 
