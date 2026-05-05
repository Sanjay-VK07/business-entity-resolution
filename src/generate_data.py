from faker import Faker
import pandas as pd
import random

fake = Faker()

def make_company_variants(name):
    # create small variations to simulate duplicates
    variants = [
        name,
        name + " Pvt Ltd",
        name.replace(" ", "") + " Ltd",
        "M/s " + name,
    ]
    return random.choice(variants)

data = []
base_names = [fake.company() for _ in range(200)]

for _ in range(500):
    base = random.choice(base_names)
    data.append({
        "name": make_company_variants(base),
        "address": fake.address().replace("\n", ", "),
        "pincode": random.choice(["560001", "560002"]),
        "pan": fake.bothify(text='?????#####?')
    })

df = pd.DataFrame(data)
df.to_csv("data/raw_data.csv", index=False)

print("✅ Data generated: data/raw_data.csv")