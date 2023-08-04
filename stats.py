import pandas as pd

sheet_id = '14aW1u18jIfrGjnmoP_xFf_UkPByXBuHfhdG1zOi0cUw'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

tot_declines = 0
tot_applic = 0
tot_int = 0
tot_offers = 0

for row in df.iterrows(): 
    tot_applic += 1
    print(row[1][1], row[1][2])
