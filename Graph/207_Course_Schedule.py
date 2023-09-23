class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = { j:[] for j in range(numCourses) }

        for i in range(len(prerequisites)):
            indegree[prerequisites[i][0]] += 1
            graph[prerequisites[i][1]].append(prerequisites[i][0])

        # BFS
        queue = collections.deque()
        for j in range(numCourses):
            if indegree[j] == 0:
                queue.append(j)
        
        while queue:
            cur = queue.popleft()
            toTake = graph[cur]
            for num in toTake:
                indegree[num] -= 1
                if indegree[num] == 0:
                    queue.append(num)

        for i in range(numCourses):
            if indegree[i]!= 0: return False
        return True