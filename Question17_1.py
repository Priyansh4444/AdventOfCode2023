from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open('lines.txt')]

seen = set()
pq = [(0, 0, 0, 0, 0, 0)]
# (heatloss, x, y, dirx, diry, consecutivesteps)

while pq:
    hl, r, c, dr, dc, n = heappop(pq)
    
    if (r, c, dr, dc,n) in seen:
        continue
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print(hl)
        break

    seen.add((r, c, dr, dc, n)) 

    if n < 3 and (dr,dc) != (0,0):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))
    
    for ndr, ndc in [(0,1), (0,-1), (1,0), (-1,0)]:
        if (ndr,ndc) != (-dr,-dc) and (ndr,ndc) != (dr,dc):
            nr = r + ndr
            nc = c + ndc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))
