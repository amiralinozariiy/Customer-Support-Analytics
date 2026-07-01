import pandas as pd

data = {
    "Agent": ["Ali", "Sara", "Reza", "Maryam"],
    "Tickets": [120, 98, 140, 110],
    "Average Response Time (min)": [4.5, 5.2, 3.8, 4.1],
    "Customer Satisfaction": [92, 88, 95, 91]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Satisfaction:")
print(df["Customer Satisfaction"].mean())
