def hamiltonian( spins, H ) :
  energy = 0
  # Your code goes here
  energy = -spins[0]*spins[-1] - H*spins[0] 
  for i in range(1,len(spins)) : energy = energy - (spins[i-1] + H)*spins[i] 
  return energy 
  
allup, alldown = 10*[1], 10*[-1]
print( "ENERGY FOR ALL SPIN UP", hamiltonian( allup, 2 ) )
print( "ENERGY FOR ALL SPIN DOWN", hamiltonian( alldown, 1 ) )
