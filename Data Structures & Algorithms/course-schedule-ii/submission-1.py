class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
            
        # --------------------------
        # Implementation Steps:
        # 1. Build a graph using an adjacency list to track prerequisites.
        # 2. For each course, run DFS to visit all prerequisites.
        # 3. Use a set (cycle) to detect cycles in the DFS path.
        # 4. If you ever revisit a node in the current DFS path, a cycle exists → impossible schedule.
        # 5. If no cycle, append course to output after visiting its prerequisites (post-order).
        # 6. At the end, output contains a valid topological order of courses.

        # --------------------------
        # Dry Run Example:
        # numCourses = 4
        # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        # prereq = {0:[], 1:[0], 2:[0], 3:[1,2]}
        # DFS will build order: 0, 1, 2, 3 (or 0, 2, 1, 3)

        # --------------------------
        # Time Complexity: O(V + E)
        # - V: number of courses
        # - E: number of prerequisite pairs
        # Each course and prerequisite edge is visited once.

        # Space Complexity: O(V + E)
        # - The adjacency list stores up to E edges
        # - The recursion stack and sets can use up to V space
