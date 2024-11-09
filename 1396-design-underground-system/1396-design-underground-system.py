class UndergroundSystem:

    def __init__(self):
        self.checked_in = {} # id -> (station name, t) # remove from here when you check out 
        self.avgTimes = defaultdict(list) # add to here at checkout (start, end) = [cehckout - checkin]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checked_in: 
            self.checked_in[id] = (stationName, t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        startStation, startTime = self.checked_in[id]
        self.avgTimes[(startStation, stationName)].append(t - startTime)
        # remove id from checked in 
        self.checked_in.pop(id)

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        toCheck = (startStation, endStation)
        timesList = self.avgTimes[toCheck]
        return sum(timesList) / len(timesList)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)