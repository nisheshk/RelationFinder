"""
Author: Nishesh Kalakheti
Date: No Idea about the date because of the COVID-19 situation
Goal: This script reads the file family_import.txt and builds a adjacency list of relation of a person with others.
        The relation is limited to same generation or one generation up and down. This means
        a person can have a father, mother, children and sibbling.
Future Improvement:
        There should be another file which should provide the details of the person like age, gender.
        Right now its all null. This would be really helpful if the input was like A,Children,B
        Then we could figure out if M is the mother or father of A.
"""


class Person(object):
    def __init__(self, name, age=None, gender=None):
        """
            This is an initialization method which sets the properties for any person instance

            Parameters:
            -----------
            name: Takes in the name of the person
            age: Takes in the age of the person
            gender: Takes in the gender of the person

            Properties
            --------
            relations is a dicitionay which is going to store the different relations of the person
            with other person.
            
        """
        
        self.name = name
        self.age = age
        self.gender = gender
        self.relations = {}
    

class Relations(object):
    def add_child_relation(self, obj1, obj2):
        """
            This method adds child relation with its parent

            Parameters:
            -----------
            obj1: Person object (Father/Mother)
            obj2: Person object (Children)
            
        """
        
        if "Child" in obj1.relations:
            obj1.relations["Child"].add(obj2)
        else:
            obj1.relations["Child"] = set([obj2])
        self.sibbling_relation_auto_calculate(obj1, obj2)    
        
        
    def parent_child_relation(self, obj1, obj2, relation):
        """
            This method adds parent relation with its child

            Parameters:
            -----------
            obj1: Person object
            obj2: Person object
            relation: relation could be either Child, Father and Mother.
            If relation == child: obj1 = Parent and obj2 = Children
            If relation == Father or relation == Mother: obj1 = Children and obj2 = Parent
            
        """
        
        if relation == "Father":
            obj1.relations["father"] = set([obj2])
            self.add_child_relation(obj2, obj1)
        else:
            obj1.relations["Mother"] = set([obj2])
            self.add_child_relation(obj2, obj1)

    def wife_relation(self, obj1, obj2, relation, count = 0):
        """
            This method adds wife object to the relations of her husband's object.
            Then it calls husband_relation method which adds husband object to the relations of his wife's object.

            Parameters:
            -----------
            obj1: Person object (Husband)
            obj2: Person object (Wife)
            relation: Wife
            
        """
        
        if "Wife" in obj1.relations:
            obj1.relations["wife"].add(obj2)
        else:
            obj1.relations["wife"] = set([obj2])
        if count == 0:
            self.husband_relation(obj2, obj1, relation, count+1)

    def husband_relation(self, obj1, obj2, relation, count = 0):
        """
            This method adds husband object to the relations of his wife's object.
            Then it calls wife_relation method which adds wife object to the relations of her husband's object.

            Parameters:
            -----------
            obj1: Person object (Wife)
            obj2: Person object (Husband)
            relation: Husband
        """
            
        if "Husband" in obj1.relations:
            obj1.relations["husband"].add(obj2)
        else:
            obj1.relations["husband"] = set([obj2])
        if count == 0:
            self.wife_relation(obj2, obj1, relation, count+1)
        

    def sibbling_relation(self, obj1, obj2, relation, count = 0):
        """
            This method adds sibbling relation between two person

            Parameters:
            -----------
            obj1: Person object
            obj2: Person object
            relation: Sibbling
        """
        
        if relation == "Sibbling" and "Sibbling" in obj1.relations:
            obj1.relations["Sibbling"].add(obj2)
        else:
            obj1.relations["Sibbling"] = set([obj2])
        
        if count == 0:
            self.sibbling_relation(obj2, obj1 ,relation, 1)

    def sibbling_relation_auto_calculate(self, obj1, obj2):
        """
            This method auto calculates sibbling when a child relation is added to its parent.
            It looks for parent other children and adds the sibbling relation amongst all the
            children with the new children.

            Parameters:
            -----------
            obj1: Person object (Father/Mother)
            obj2: Person object (Children)
        """
        
        #Parents children list
        children = obj1.relations["Child"]
        
        for child in children:
            if obj2.name != child.name:
                #This if-else statement adds new child as a sibbling to other child already added 
                if "Sibbling" in child.relations:
                    child.relations["Sibbling"].add(obj2)
                else:
                    child.relations["Sibbling"] = set([obj2])

                #This if-else statement adds already added child of its parent as its sibbling
                if "Sibbling" in obj2.relations:
                    obj2.relations["Sibbling"].add(child)
                else:
                    obj2.relations["Sibbling"] = set([child])
        

def person_exists(person, person_obj):
    """
            This method checks if the person object exists in the dictionary person_obj
            If yes, returns the existing object. Else, creates a new person object and
            returns the same

            Parameters:
            -----------
            obj1: Person object (Father/Mother)
            obj2: Person object (Children)

            Returns:
            -----------
            obj: Person obj
        """
    
    if person not in  person_obj:  
        obj = Person(name = person)
        person_obj[person] = obj
    else:                           
        obj = person_obj[person]
    return obj  
    
def build_relation():
    """
            This method reads the family_import.txt file which defines the relation between various individuals.
            Then it parses the file and creates the person object along with its relations.

            Returns:
            -----------
            person_obj: dictionary which contains all the objects we created.
    """

    #Open the file and read line by line
    fopen = open("family_import.txt", "r")
    family_relation = fopen.readlines()
    fopen.close()

    #This person_obj will contain all the objects we create and is returned from the function eventually.
    #Key = person name; value = person's object.
    person_obj = {}

    #This relation_dic contains the various relation types and the method that needs to be called.
    relation_dic = {"Father":Relations().parent_child_relation, "Mother": Relations().parent_child_relation, "Husband": Relations().husband_relation,\
                        "Wife": Relations().wife_relation}

    #Iterate through the list family_relation and get person1, person2 and the relation between them.
    for relations  in family_relation:
        relations = relations.split(",")
        person1 = relations[0].strip()
        person2 = relations[2].strip()
        relation = relations[1].strip()

        #It does not make sense if person1 == person2. Can X have any relation with X? :D 
        if person1 != person2: 
            if relation in relation_dic:
                #If person object not exists; then create one. Else select from the person_obj dic
                p1 = person_exists(person1, person_obj)
                p2 = person_exists(person2, person_obj)  
                relation_dic[relation](p1, p2, relation)

##    #For testing purpose
##    for k,v in person_obj.items():
##        print (v.name)
##        for j in v.relations:
##            print (j)
##            for k in v.relations[j]:
##                print (k.name)
##            print ("\n*******\n")
##
##    for k,v in person_obj.items():
##        if v.name == "Yagya Mani Kalakheti":
##            for j in v.relations:
##                print (j)
##                for k in v.relations[j]:
##                    print (k.name)
##                print ("\n*******\n")


    return person_obj

