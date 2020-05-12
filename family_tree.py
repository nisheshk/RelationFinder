class Person(object):
    def __init__(self, name, age=None, gender=None, remarks = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.remarks = remarks
        self.relations = {}
    

class Relations(object):

    def add_child_relation(self, obj1, obj2):
        if "Child" in obj1.relations:
            obj1.relations["Child"].add(obj2)
        else:
            obj1.relations["Child"] = set([obj2])
        self.sibbling_relation_auto_calculate(obj1, obj2)    
        
        
    def parent_child_relation(self, obj1, obj2, relation):
        if relation == "Child":
            add_child_relation(obj1, obj2)
        if relation == "Father" or obj2.gender == "M":
            obj1.relations["father"] = set([obj2])
            self.add_child_relation(obj2, obj1)
        if relation == "Mother" or obj2.gender == "F":
            obj1.relations["Mother"] = set([obj2])
            self.add_child_relation(obj2, obj1)

    def wife_relation(self, obj1, obj2, relation, count = 0):
        if "Wife" in obj1.relations:
            obj1.relations["wife"].add(obj2)
        else:
            obj1.relations["wife"] = set([obj2])
        if count == 0:
            self.husband_relation(obj2, obj1, relation, count+1)

    def husband_relation(self, obj1, obj2, relation, count = 0):
        if "Husband" in obj1.relations:
            obj1.relations["husband"].add(obj2)
        else:
            obj1.relations["husband"] = set([obj2])
        if count == 0:
            self.wife_relation(obj2, obj1, relation, count+1)
        

    def sibbling_relation(self, obj1, obj2, relation, count = 0):
        if relation == "Sibbling" and "Sibbling" in obj1.relations:
            obj1.relations["Sibbling"].add(obj2)
        else:
            obj1.relations["Sibbling"] = set([obj2])
        
        if count == 0:
            self.sibbling_relation(obj2, obj1 ,relation, 1)

    def sibbling_relation_auto_calculate(self, obj1, obj2):
        children = obj1.relations["Child"]  #Parents children
        #children iterate harek sibbling ma obj2 add
        for child in children:
            if obj2.name != child.name:
                if "Sibbling" in child.relations:
                    child.relations["Sibbling"].add(obj2)
                else:
                    child.relations["Sibbling"] = set([obj2])
                if "Sibbling" in obj2.relations:
                    obj2.relations["Sibbling"].add(child)
                else:
                    obj2.relations["Sibbling"] = set([child])
        

  

    
def relation_builder():

    fopen = open("family_import.txt", "r")
    family_relation = fopen.readlines()
    fopen.close()
    
    person_obj = {}
    relation_dic = {"Father":Relations().parent_child_relation, "Mother": Relations().parent_child_relation, "Husband": Relations().husband_relation,\
                        "Wife": Relations().wife_relation}
    
    for relations  in family_relation:
        relations = relations.split(",")
        person1 = relations[0].strip()
        person2 = relations[2].strip()
        relation = relations[1].strip()
        if relation in relation_dic:

            if person1 not in  person_obj:  #If Person1 object not exists; then create one
                p1 = Person(name = person1)
                person_obj[person1] = p1
            else:                           #Else select from the person_obj dic
                p1 = person_obj[person1]
            if person2 not in  person_obj:  #If Person2 object not exists; then create one
                p2 = Person(name = person2)
                person_obj[person2] = p2
            else:                           #Else select from the person_obj dic3
                p2 = person_obj[person2]
                
            relation_dic[relation](p1, p2, relation)

##    For testing purpose
##    for k,v in person_obj.items():
##        print (v.name)
##        for j in v.relations:
##            print (j)
##            for k in v.relations[j]:
##                print (k.name)
##            print ("\n*******\n")

##    for k,v in person_obj.items():
##        if v.name == "Yagya Mani Kalakheti":
##            for j in v.relations:
##                print (j)
##                for k in v.relations[j]:
##                    print (k.name)
##                print ("\n*******\n")

    return person_obj

