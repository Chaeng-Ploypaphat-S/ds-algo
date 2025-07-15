# Problem: 841. Keys and Rooms
# Difficulty: Medium
# Date: 2025-03-17

from collections import defaultdict
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        keys = defaultdict(list)
        for i, to_room in enumerate(rooms):
            if to_room:
                keys[i] = to_room

        seen = set()
        seen.add(0)

        q = [0]
        while q:
            nxt_room = q.pop()
            for nr in keys[nxt_room]:
                if nr not in seen:
                    seen.add(nr)
                    q.append(nr)

        return len(seen) == len(rooms)
        