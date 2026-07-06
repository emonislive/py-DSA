class Solution:
    count = 0
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n == 0:
            return self.count
        if n == 1:
            # print("move disk " + str(n) + " from rod " + str(fromm) + " to rod " + str(to))
            self.count += 1
            return self.count
            
        self.towerOfHanoi(n - 1, fromm, aux, to)
        # print("move disk " + str(n) + " from rod " + str(fromm) + " to rod " + str(to))
        self.count += 1
        self.towerOfHanoi(n - 1, aux, to, fromm)
        
        return self.count