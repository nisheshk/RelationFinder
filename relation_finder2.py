"""
Reference: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
"""

import family_tree
from collections import deque

class Graph(object):
    def __init__(self, graph = None):
        self.graph = {}
        if graph:
            self.graph = graph

    def get_person(self): #Returns the names of each person, which is nothing but graph vertices
        return self.graph.keys()

    def is_isolated(self, person): #Checks if the person has any relation
        if len(self.graph[person].relations) == 0:
            return 1
        return 0

    def find_relation(self, person1, person2):
        if person1 not in self.graph or person2 not in self.graph:
            return []

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
        obj = self.find_relation(person1, person2)
        if obj:
            for i in range(0,len(obj[0])-1,1):
                print ("{0}'s {1} is {2}".format(obj[0][i], obj[1][i+1] , obj[0][i+1]))


def main():
    family_relation = family_tree.relation_builder()
    g = Graph(family_relation)

    a = g.print_relation("Nishesh Kalakheti","Nirmani Kalakheti")
    
if __name__ == "__main__":
    main()
