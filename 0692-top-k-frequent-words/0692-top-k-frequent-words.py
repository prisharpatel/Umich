class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # return k most frequent strings in words

        # max heap - storing the most frequent words

        cnt = Counter(words) # O(N)
        heap = []
        
        for word, freq in cnt.items():
            # add to heap based on frequency but also include the word 
            toAdd = (-1 *freq, word)
            heap.append(toAdd)
        heapq.heapify(heap)
        output = []
        for i in range(k): 
            freq, word = heapq.heappop(heap)
            output.append(word)
        return output