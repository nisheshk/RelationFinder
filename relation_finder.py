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

        #2d queue, contains all the combinations
        queue = deque([[person1]])
        visited = {}
        
        
        while queue:
            #Pop the left most element(first element)
            path = queue.popleft()

            #Fetch the last element from the popped list
            node = path[-1]
            if node not in visited:
                visited[node] = True
                person1_relation = self.graph[node].relations
                
                for relation_type, members in person1_relation.items():
                    for each_member in members:
                        #Create an array for each combination from the last element of the popped list
                        new_path = list(path)
                        new_path.append(each_member.name)
                        if each_member.name == person2:
                            return new_path

                        #Store the array back in the queue
                        queue.append(new_path)
                        
        return []


def main():
    family_relation = family_tree.relation_builder()
    g = Graph(family_relation)

    print (g.find_relation("Bhairav Kalakheti","Gyanu Kalakheti"))
    
    
if __name__ == "__main__":
    main()
