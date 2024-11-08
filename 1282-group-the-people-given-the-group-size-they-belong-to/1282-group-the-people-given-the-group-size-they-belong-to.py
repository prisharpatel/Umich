class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # understand: n people split into some unknown number of groups and the groupSizes say 
        # what size group a student has to be in 

        # matching - greedy? 
        # - people id's (indexes) iwth same group size into buckets and split each bucket into groups
        # have to be at least O(n) because need to see what size group each person needs to go into 

        # pseudocode 
        # i = id 
        # use a hashmap of size of group --> id of students
        students = defaultdict(list)
        for i, groupSize in enumerate(groupSizes): 
            students[groupSize].append(i)
        
        # go through the keys 
        output = []
        for groupSize in students.keys(): # O(n) is a constraint so constant???
            totalStudents = students[groupSize]
            # since there is guaranteed to be a solution can just split based on group size 
            group = []
            while totalStudents: #O(n)
                if len(group) == groupSize:
                    output.append(group)
                    group = []
                group.append(totalStudents.pop())
            if len(group) == groupSize:
                output.append(group)
        
        
        return output





        