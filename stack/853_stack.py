class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):
        """
        Sort based on distance -> Merging from the back
        """
        if len(speed) == 1:
            return 1

        cars = list(zip(position, speed))
        #* O(NlogN)
        cars.sort(key=lambda e: e[0])

        nxt_pos, nxt_pace = cars.pop()
        stack = [(nxt_pos, nxt_pace)]
        nxt_duration = (target - nxt_pos) / nxt_pace
        while cars:
            pos, pace = cars.pop()
            duration = (target - pos) / pace
            if duration <= nxt_duration:
                #* This car can catch up with the next car fleet.
                #* Do nothing -- the car fleet in the stack can represent this car
                #! No need to update the fleet since it blocks this car.
                pass
            else:
                #* Can't catch up -> Form a fleet itself.
                stack.append( (pos, pace) )
                #* Update the duration of the next fleet.
                nxt_duration = duration
                
        return len(stack)