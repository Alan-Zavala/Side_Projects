import pandas as pd

sheet_id = '14aW1u18jIfrGjnmoP_xFf_UkPByXBuHfhdG1zOi0cUw'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# cols == company, pos, date applied, no response, decline, assesment, interview, offer
no_responses ,tot_declines , tot_assesments, tot_applic, tot_int, tot_offers = 0, 0, 0, 0, 0, 0


for row in df.iterrows(): 
    # check if application row is valid
    if row[1][1] != row[1][1]:
        continue

    tot_applic += 1
    if row[1][3] is True:
        no_responses += 1
    if row[1][4] is True:
        tot_declines += 1
    if row[1][5] is True:
        tot_assesments += 1
    if row[1][6] is True:
        tot_int += 1
    if row[1][7] is True:
        tot_offers += 1

# percentage calculations
no_resp_per = round(no_responses/tot_applic, 4)*100
int_per = round(tot_int/tot_applic, 4)*100
offer_int_per = round(tot_offers/tot_int, 4)*100
dec_per = round(tot_declines/tot_applic, 4)*100
assesment_per = round(tot_assesments/tot_applic, 4)*100

print('-------'*10)
print('These are your Job Hunt Statistics!\n')
print(f'You applied to {tot_applic} jobs and {no_resp_per}% of them were a no response')
print(f'{dec_per}% got a formal decline, while {assesment_per}% requiered an assesment\n')
print(f'{int_per}% resulted in an interview and {offer_int_per}% of those led to an offer\n')
