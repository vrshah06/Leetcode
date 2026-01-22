class AuctionSystem:
    def __init__(self):
        self.bids = {}
    def addBid(self,userId:int,itemId:int,bidAmount:int) -> None:
        if itemId not in self.bids:
            self.bids[itemId] = {}
        self.bids[itemId][userId] = bidAmount
    def updateBid(self,userId:int,itemId:int,newBidAmount:int) -> None:
            self.bids[itemId][userId] = newBidAmount
    def removeBid(self,userId:int,itemId:int) -> None:
        del self.bids[itemId][userId]
    def getHighestBid(self,itemId:int) -> int:
        if itemId not in self.bids:
            return -1
        max_bid = -1
        max_user = -1
        for userId, bidAmount in self.bids[itemId].items():
            if bidAmount > max_bid or (bidAmount == max_bid and userId > max_user):
                max_bid = bidAmount
                max_user = userId
        return max_user
