import matplotlib.pyplot as plt
import numpy as np
DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77, 32, 42]

LABELS = ["Monday", "Tuesday", "Wednesday"]

plt.bar(DayOfWeekOfCall, DispatchesOnThisWeekday, align='center')
#plt.hist(DayOfWeekOfCall, DispatchesOnThisWeekday)
plt.xticks(DayOfWeekOfCall, LABELS,rotation="45")
#plt.yticks(np.random.normal(50,2,6))
plt.xlabel("Days")
plt.ylabel("no of calls")
plt.show()





