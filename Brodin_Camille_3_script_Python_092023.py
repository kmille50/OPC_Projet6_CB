# %%
import requests
from pprint import pprint
from IPython import display

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

querystring = {"ingr": "champagne"}

headers = {
    "X-RapidAPI-Key": "je_garde_la_clef_et_vous_presente_les_outputs_conserves_ci_dessous",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
record = response.json()
pprint(record)

# %%
# foodId, label, category, foodContentsLabel, image
print('record entries', record.keys())
hints = record['hints']
print('len hints', len(hints))
hint = hints[1]
food = hint['food']
result = {key: val for key, val in food.items(
) if key in {'foodId', 'label', 'category', 'image', 'foodContentsLabel'}}
result

# %%


# %%
import pandas as pd


def extract_from_hint(hint):
    food = hint['food']
    result = {key: val for key, val in food.items(
    ) if key in {'foodId', 'label', 'category', 'image', 'foodContentsLabel'}}
    return result


def extract_from_record(record):
    hints = record['hints']
    results = [extract_from_hint(hint) for hint in hints]
    return results

#results = extract_from_record(record)

results = pd.read_csv('results.csv')
df = pd.DataFrame.from_records(results)
df.head()

# %%
print(df.shape)
# df = df.dropna(thresh=2)
df = df.head(10)
print(df.shape)

# %%
df.to_csv('extraction_produits.csv')
