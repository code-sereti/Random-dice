import pandas as pd 
import random
import matplotlib.pyplot as plt

data = []
for i in range(600):
    roll_6 = random.randint(1, 6)
    roll_4 = random.randint(1, 4)
    roll_2 = random.randint(1, 2)
    d = {"roll_6": roll_6, "roll_4": roll_4, "roll_2": roll_2}
    data.append(d)

df = pd.DataFrame(data)

# Scatter plotting with 'roll_6' and 'roll_4'
df[['roll_6', 'roll_4']].plot(kind='scatter', x='roll_6', y='roll_4')
plt.title('Scatter Plot of roll_6 vs. roll_4')
plt.xlabel('roll_6')
plt.ylabel('roll_4')
plt.show()
