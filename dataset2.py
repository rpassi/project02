import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/riapassi/Documents/GitHub/rpassi.github.io/CS40 In class/olympic.csv')

male = df[df['Sex'] == 'M']
female = df[df['Sex'] == 'F']

plt.figure(figsize=(8,6))

scatter = plt.scatter(df.Year, 
    df.Height,
    c=df.Sex.astype('category').cat.codes, 
    s= 2)
plt.legend(handles=scatter.legend_elements()[0],labels = ["F", "M"], title="species")
plt.title("Olympic Height of Males and Females by Year")
plt.xlabel("Year")
plt.ylabel("Height (cm)")
plt.show()

