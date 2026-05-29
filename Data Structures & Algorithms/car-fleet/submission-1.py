class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = slow_car_eta = 0
        for p, s in sorted(zip(position, speed), reverse = True):
            eta = (target - p) / s
            if eta > slow_car_eta:
                ans += 1
                slow_car_eta = eta
        return ans
            
        
                
        