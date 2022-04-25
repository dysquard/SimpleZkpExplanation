from random import SystemRandom

# Cryptography Public Parameters
g = 22500 # Generator of the finite group
P = 3213876088517980551083924184682325205044405987565585670609523 # Order of the finite group. A big prime number.

# The encrypted knowledge, will be set by a 3rd party. 
# Its preimage, which the prover needs to prove he knows, is not accessible to both the prover and verifier.
h = None

# These parameters will be set in further proving steps and passed from the verifier to the prover or vice versa.
a = e = z = None

    
def specifyKnowledge(w):    
        global h
        h = pow(g,w,P)         
        print('\n'+'The knowledge topic has been designated.'+ '\n' +
        'Neither the verifier nor prover can read since it\'s discarded after this func executed.' + '\n' +
        'Only its encryption is publicly known.' '\n' +
        'If the prover hasn\'t learned it somewhere else before, he won\'t be able to pass the verification.''\n')

class Verifier:

    def __init__(self):        
        return        

    def verify_step1(self):
        global e
        e = SystemRandom().randrange(P)
        print('Verifier:')
        print('random number b = ',e,', b -----> Prover','\n') 

    def verify_step2(self):
        print('Verifier:'+'\n'+'Checking if pow(g,z,P) == (a * pow(encryptedKnowledge,b,P)) % P:')
        
        if pow(g,z,P) == (a * pow(h,e,P)) % P:
            print('Accept! Prover knows the knowledge','\n')
        else:
            print('Reject! Prover knows nothing','\n')
        
class Prover:

    def __init__(self, knowledge_to_verify):
        self.k = knowledge_to_verify
        self.r = SystemRandom().randrange(P)    
        print('Start proving','\n')

    def prove_step1(self):            
        global a
        a = pow(g,self.r,P) 
        print('Prover:')
        print('random number r = ',self.r) 
        print('a = g ** r % p = ',a,', a -----> Verifier','\n') 
            
    def prove_step2(self):
        global z
        z = self.r + e * self.k
        print('Prover:')
        print('z = r + b * knowledge_to_verify = ',a,', z -----> Verifier','\n') 

    

print('\n'+'-------- Zeroknowledge Example Begins --------'+'\n')

specifyKnowledge(w = int(input("Enter your secret knowledge (Intger):")))
prover = Prover(knowledge_to_verify = int(input("Enter Prover's knowledge (Intger) :")))
verifier = Verifier()

prover.prove_step1()
verifier.verify_step1()
prover.prove_step2()
verifier.verify_step2()

