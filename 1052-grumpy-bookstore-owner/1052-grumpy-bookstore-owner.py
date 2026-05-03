class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        change_loss = 0
        max_change_loss = 0
        satisfy = 0
        for right, (cus, gru) in enumerate(zip(customers, grumpy)):
            if gru:
                change_loss += cus
            else:
                satisfy += cus
            
            if right < minutes-1:
                continue
            max_change_loss = max(max_change_loss, change_loss)

            left = right -minutes+1
            if grumpy[left]:
                change_loss -= customers[left]
        return satisfy + max_change_loss
