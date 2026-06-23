class Solution(object):
    def canVisitAllRooms(self, rooms):
       
        visited = set()
        keys = [0]

        while keys:
            room = keys.pop()
            if room not in visited:
                visited.add(room)
                keys.extend(rooms[room])
        return len(rooms) == len(visited)