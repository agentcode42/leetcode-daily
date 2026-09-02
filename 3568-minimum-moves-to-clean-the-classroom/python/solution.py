class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        start_x,start_y = 0,0
        count = 0
        litter = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if classroom[i][j]=="S":
                    start_x = i
                    start_y = j
                elif classroom[i][j]=="L":
                    litter[i][j]=1<<count
                    count+=1
        total = 1<<count
        max_energy = [
            [[-1]* total for _ in range(cols)]
            for _ in range(rows)
        ]

        queue = deque([(start_x,start_y,energy,0,0)]) # x,y,curr_energy,mask , steps 
        max_energy[start_x][start_y][0] = energy

        while queue:
            x,y,curr_energy,mask,steps = queue.popleft()

            if mask==total-1:
                return steps
            if curr_energy==0:
                continue
            for dx,dy in directions:
                nx =x+ dx 
                ny = y+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if classroom[nx][ny]=="X":
                    continue
                new_energy = curr_energy-1
                if classroom[nx][ny]=="R":
                    new_energy = energy
                new_mask = mask|litter[nx][ny]
                
                if new_energy>max_energy[nx][ny][new_mask]:
                    max_energy[nx][ny][new_mask]=new_energy
                    queue.append((nx,ny,new_energy,new_mask,steps+1))
        return -1
                    