import integrate as inte, sys
sys.path.append("../../People")
from two import person as p

##############################################################
## Generate a person and show the change in their confidence 
## range through time
##############################################################

person = p.Person(3)
person.printProbs()

count = 0
for i in range(2,5):
    while count <= 10**i:
        person.randomSearch()
        count = count + 1
    print inte.findProbs(person.getProbsEmpirical(),person.confidence(),1)
