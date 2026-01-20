import pandas as pd 
import numpy as np 
age=np.random.randint(22,50,size=15)
occupation=np.random.choice(["Teacher","Nurse","Sales Manager","Accountant","Data Analyst","Clerk"],size=15)
salary=np.random.randint(50000,300000,size=15)
location=np.random.choice(["Lagos","Washington","Moscow","Hanoi","Mumbai","Nairobi","Oslo","Warsaw","Burcharest"],size=15)
users_dataset1={
    "Names":["Mary","Jane","Hillary","Napoleon","Terry","Mane","Sane","Mamadou","Claire","Venn","Hill","Joan","Peter","James","John"],
    "Age":age,
    "Occupation":occupation,
    "Salary":salary,
    "Location":location
    
}
#add dataframe
users_table1=pd.DataFrame(users_dataset1)
#save as csv
users_table1.to_csv("users_table1.csv",index=True)
print("\nUsers table 1 saved as csv file\n")