class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # return k most frequent strings in words    

        # make a hashmap and increase the count for stirngs
        # sort it based on values O(nlogn)

        # min heap? 
        tracker = defaultdict(int)
        
        for word in words:
            tracker[word] += 1

        # sort by value
        tracker = dict(sorted(tracker.items(), key=lambda x: x[1], reverse = True)) 
        # sort by key
        tracker = dict(sorted(tracker.keys()))


        output = []
        for word in tracker.keys():
            if len(output) < k: 
                output.append(word)
            else: 
                break
        return output
            





        
        