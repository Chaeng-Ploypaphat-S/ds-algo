# Q1: Create a function that reverses a string recursively.
# Note about the problem: 
# - Time management: took long time to complete. 
# - Bugs: 
#   - Wrong initial call. Passed 'len(word)' instead of 'len(word) - 1'.
#   - Incorrect base case: should return the the whole string when end - start <= 0 
#   - Incorrect base case: should return the two characters in reverse order when 'end - start == 1'
#                          but wrote 'end - start <= 2' instead. T-T
# - Time complexity:  O(n log n), where n is the length of the string but said O(n) in the interview.
# - Space complexity: O(n log n), due to the recursive stack space of a binary-like division 
#                     but said O(n) in the interview.

def reverse(word: str) -> str:
  return reverse_helper(word, 0, len(word) - 1)

def reverse_helper(word: str, start: int, end: int) -> str:
  if end - start <= 0:
    return word[start]
  elif end - start == 1:
    return word[end] + word[start]
  else:
    half = start + (end - start) // 2
    left = reverse_helper(word, start, half)
    right = reverse_helper(word, half + 1, end)
    return right + left


# Q2: Design a Tracker class that tracks servers used for multiple type of requests.
# Types: 'api', 'db'
# The format of the request is: 'api-1', 'db-2', etc.
# Specifications:
# - The Tracker class should have methods to allocate servers and deallocate servers.
# - The number of servers starts at 1.
# - Each allocation, the number of servers increases by 1. 
# - Each allocation, pick the server with the lowest missing number.

from typing import List
from collections import defaultdict

class Tracker:
    def __init__(self, existing_inventory: List[str]=None) -> None:
        self.inventory = defaultdict(list)
        if existing_inventory:
            for server in existing_inventory:
                server_type, server_num = server.split('-')
                server_num = int(server_num)
                self.inventory[server_type].append([server_num, server_num])
            # Sort intervals for each server type
            for servers in self.inventory.values():
                servers.sort()
                
        # merge intervals if necessary
        for server_type, servers in self.inventory.items():
            merged_servers = []
            for start, end in servers:
                if not merged_servers or merged_servers[-1][1] + 1 < start:
                    merged_servers.append([start, end])
                else:
                    merged_servers[-1][1] = max(merged_servers[-1][1], end)
            self.inventory[server_type] = merged_servers

    def allocate(self, server_type: str) -> str:
        server_type = server_type.split('-')[0]
        if server_type not in self.inventory:
            self.inventory[server_type] = [[1,1]]
            return f"{server_type}-1"
        
        # There is at least one server of this type
        servers = self.inventory[server_type]
        # Find the first missing server number
        new_server = None
        if servers[0][0] > 1:
            new_server = f"{server_type}-1"
            servers.insert(0, [1, 1])
        else:
            first_interval = servers[0]
            new_server = f"{server_type}-{first_interval[1] + 1}"
            
        # merge intervals if necessary
        # merge the first and the second intervals if they are consecutive
        if len(servers) > 1 and servers[0][1] + 1 == servers[1][0]:
            servers[0][1] = servers[1][1]
            servers.pop(1)
        
        return new_server

    def deallocate(self, server_name: str) -> None:
        # do nothing if the server name is invalid
        server_type = server_type.split('-')[0]
        if not server_type in self.inventory:
            return
        
        server_num = int(server_name.split('-')[1])
        servers = self.inventory[server_type]
        for i, (start, end) in enumerate(servers):
            if start <= server_num <= end:
                if start == end:
                    servers.pop(i)
                elif start == server_num:
                    servers[i][0] += 1
                elif end == server_num:
                    servers[i][1] -= 1
                else:
                    servers.insert(i + 1, [server_num + 1, end])
                    servers[i][1] = server_num - 1
                break