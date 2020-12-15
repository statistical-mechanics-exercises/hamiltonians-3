import unittest
import numpy as np
from main import *

class UnitTests(unittest.TestCase) :
    def test_energy(self) : 
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
               spins[j] = np.floor( num / 2**(4-j) )
               num = num - spins[j]*2**(4-j)
               if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            coup_eng = spins[0]*spins[len(spins)-1]
            for i in range(len(spins)-1) : coup_eng = coup_eng + spins[i]*spins[i+1]
            self.assertTrue( hamiltonian( spins, 1)==-coup_eng-sumspins, "The hamiltonian does not give correct values for the energy" )
            self.assertTrue( hamiltonian( spins, -1)==-coup_eng+sumspins, "The hamiltonian does not give correct values for the energy" )
            self.assertTrue( hamiltonian( spins, 0)==-coup_eng, "The hamiltonian does not give correct values for the energy" )
            self.assertTrue( hamiltonian( spins, 2)==-coup_eng-2*sumspins, "The hamiltonian does not give correct values for the energy" )
