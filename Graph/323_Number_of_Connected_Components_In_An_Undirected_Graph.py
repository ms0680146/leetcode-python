from collections import deque, defaultdict

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if n - 1 > len(connections):
            return -1

        # Create a defaultdict with lists to represent the connections between nodes
        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Initialize a variable to keep track of the number of connected components
        components = 0

        # Initialize a set to keep track of visited nodes
        visited = set()

        # Perform BFS to find connected components
        for node in range(n):
            if node not in visited:
                components += 1
                queue = deque([node])

                while queue:
                    current_node = queue.popleft()
                    visited.add(current_node)
                    for neighbor in adj_list[current_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)

        return components - 1  # Number of additional connections needed is (components - 1)

# Test cases
solution = Solution()
print(solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))  # Output: 2
print(solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))  # Output: -1
