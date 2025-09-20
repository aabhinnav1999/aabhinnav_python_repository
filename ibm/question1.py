# def getSessionCount(timeout, userIds, timestamps):
#     count = 0
#     # Write your code here
#     for i in range(0,len(userIds)-1):
#         if userIds[i] == userIds[i+1]:
#             if timestamps[i+1] - timestamps[i] <= timeout:
#                 continue
#             else:
#                 count += 1
#     return count

# print(getSessionCount(10, ["A", "A", "A", "B", "B", "A"], [1, 5, 16, 2, 12, 20]))  # Output: 4
           

from typing import List, Dict

def getSessionCount(timeout: int, userIds: List[str], timestamps: List[int]) -> int:
    events = sorted(zip(userIds, timestamps), key=lambda x: (x[0], x[1]))
    
    last_time: Dict[str, int] = {}
    sessions = 0
    
    for uid, t in events:
        if uid not in last_time:
            sessions += 1
        else:
            if t - last_time[uid] > timeout:
                sessions += 1
        last_time[uid] = t
    return sessions


