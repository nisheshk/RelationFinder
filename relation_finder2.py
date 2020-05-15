"""
Author: Nishesh Kalakheti
Date: No Idea about the date because of the COVID-19 situation
Goal: To find the relation between two individuals using BFS shortest path technique.
 
Reference: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
"""

import relation_builder
from collections import deque

class Graph(object):
    def __init__(self, graph = None):
        """
            This is an initialization method which initializes the dict graph which is the same person_obj
            dict we had from the script relation_builder.
            

            Parameters:
            -----------
            graph: Takes in the person_obj dict from the script relation_builder

            
        """
        self.graph = {}
        if graph:
            self.graph = graph

    

    def get_person(self): #Returns the names of each person, which is nothing but graph vertices
        """
            This method returns the names of each person, which is nothing but graph vertices.
            Returns:
            -----------
            self.graph.keys(): List 
      
        """
        return self.graph.keys()

    def is_isolated(self, person): #Checks if the person has any relation
        """
            This method checks if the verties has edges. If no edge return 0; else return 1
            
            Returns:
            -----------
            1/0: int
      
        """
        if len(self.graph[person].relations) == 0:
            return 1
        return 0

    def find_relation(self, person1, person2):
        """
            This method is the part where we implement BFS to find the shortest relation(path) between
            two individuals.
            
            Returns:
            -----------
            List
      
        """

        #Check if the person1 name or person2 name exists in the graph. O(1) Time complexity
        if person1 not in self.graph or person2 not in self.graph:
            return []

        #Check if the node is isolataed. O(1) Time complexity
        if self.is_isolated(person1) or self.is_isolated(person2):
            return []

        #2d queue, it will contain the possible paths
        queue = deque([[person1]])

        #If more memory is being consumed; the relation can be figured out later using the person sequence
        #order we recieve from the below algorithm. This means for all the person in new_path array, we
        #need to iterate through the relations dict to find out the relation.
        #Hence save memory in expense of time. 
        relation = deque([[None]])
        visited = {}
        
        
        #O(V+E) Time Complexity where V=Vertices(No of person), E=Edges(Its relation with other people)
        while queue:
            #Pop the left most element(first element)
            path = queue.popleft()
            rel = relation.popleft()
            #Fetch the last element from the popped list
            node = path[-1]
            if node not in visited:
                visited[node] = True
                person1_relation = self.graph[node].relations
                
                for relation_type, members in person1_relation.items():
                    for each_member in members:
                        #Create an array for each combination from the last element of the popped list
                        new_path = list(path)
                        new_rel = list(rel)
                        
                        new_path.append(each_member.name)
                        new_rel.append(relation_type)
                        if each_member.name == person2:
                            return (new_path,new_rel)

                        #Store the array back in the queue
                        queue.append(new_path)
                        relation.append(new_rel)
                        
        return []


    def print_relation(self, person1, person2):
        """
            This method prints the relation between two person.
        """
        obj = self.find_relation(person1, person2)
        if obj:
            for i in range(0,len(obj[0])-1,1):
                print ("{0}'s {1} is {2}".format(obj[0][i], obj[1][i+1] , obj[0][i+1]))
        else:
            print ("No relation between {0} and {1}".format(person1, person2))


def main():
    """
        The driven function.
    """

    #Calls relation_builder script and gets back the person object.
    person_obj = relation_builder.build_relation()

    #Feed the person_obj to the graph
    g = Graph(person_obj)

    #Print the relation between two person.
    a = g.print_relation("Nishesh Kalakheti","Nirmani Kalakheti")
    
if __name__ == "__main__":
    main()
