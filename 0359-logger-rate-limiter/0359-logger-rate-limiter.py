class Logger:

    def __init__(self):
        # self.logger = [] # stores arrays within this array
        self.messageTracker = {} # message --> timestamp last printed

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageTracker.keys():
            # print message
            self.messageTracker[message] = timestamp

            return True
        else: 
            if self.messageTracker[message] + 10 > timestamp:
                # can't print
                return False
            else:
                self.messageTracker[message] = timestamp
                return True

         
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)