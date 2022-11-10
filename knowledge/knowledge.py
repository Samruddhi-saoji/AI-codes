import json
from logpy import Relation, facts, run, conde, var, eq


#declaring the relations
father = Relation()
mother = Relation()

#the family tree file
with open ('familytree.json') as f:
    tree = json.loads(f.read()) #dictioary
    #family tree is a dictionary with 2 elements: father, mother
    # tree = { father:[list of {father:child} dictionaries]  ,  mother:[list of {mother:child} dictionaries]}


#adding facts to the knowledge base
for item in tree["father"] :
    facts(father, (list(item.keys())[0], list(item.values())[0]))
for item in tree['mother']:
  facts(mother, (list(item.keys())[0], list(item.values())[0]))



#parsing the tree #infering new facts #############################################################

#functions####################################
#function parent(x,y)
#returns true if x is parent of y
def parent(x, y):
  return conde([father(x, y)], [mother(x, y)])

# function sibling(x,y)
#returns true if x, y are siblings
def sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))



#listing all the spouses##############################
f, m, c = var(), var(), var() #declaring variables

#f,m are spouses if f is the father of c, and m is the mother of c
spouses_list = run(0, (f, m), (father, f, c), (mother, m, c))
print("\nList of spouses:")
for item in spouses_list:
  print('Husband:', item[0], '<==> Wife:', item[1])


#ist of Walburga's siblings
sib = var()
sibling_list = run(0, sib, sibling(sib, "Walburga"))
#this list also contains "Walburga". remove it
sibling_list = [x for x in sibling_list if x != "Walburga"]
print("\nWalburga's siblings: " , sibling_list)


#list sirius's cousins
sib, cousin = var(), var()
x, y= var(), var()
cousin_list = run(0, cousin, parent(x, "Sirius"), sibling(x, y), parent(y, cousin) )
#cousin list contains Sirius's siblings too
sibling_list = run(0, sib, sibling(sib, "Sirius")) #list of sirius's sibling
#remove sirius's siblings from cousin_list
cousin_list = [x for x in cousin_list if not (x in sibling_list) ]
print("\nSirius's cousins: " , cousin_list)


#list draco malfoy's aunts 
x , y =  var() , var()
aunt_list = run(0, y, parent(x,"Draco Malfoy"), sibling(x,y))
#this list also contains draco's mother
m = var()
mom = run(0,m , mother(m, "Draco Malfoy"))[0]
aunt_list = [x for x in aunt_list if x != mom]
print("\nDracos aunts: ", aunt_list)


#who is nymphadora tonk's grandfather
x, y = var() , var()
grandfather = run(0, y , parent(x, "Nymphadora Tonks"), father(y, x))
print("\nNymphadora's grandfather is ", grandfather)
