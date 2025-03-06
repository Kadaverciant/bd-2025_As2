import numpy as np
import pandas as pd
import warnings
import os

warnings.filterwarnings('ignore')

## Postgres part

try:
    os.makedirs("../data/postgres")
except:
    pass


def clean_campaigns(df):
    df['total_count'] = df['total_count'].astype('object')
    df['hour_limit'] = df['hour_limit'].astype('object')
    df['subject_length'] = df['subject_length'].astype('object')
    df['position'] = df['position'].astype('object')

    for i, row in df.iterrows():
        if not pd.isna(row['total_count']):
            df.at[i, 'total_count'] = int(row['total_count'])
        if not pd.isna(row['hour_limit']):
            df.at[i, 'hour_limit'] = int(row['hour_limit'])
        if not pd.isna(row['subject_length']):
            df.at[i, 'subject_length'] = int(row['subject_length'])
        if not pd.isna(row['position']):
            df.at[i, 'position'] = int(row['position'])
        if pd.isna(row['ab_test']):
            df.at[i, 'ab_test'] = False

    df.to_csv("../data/postgres/campaigns.csv", index=False)
    return df

campaigns_df = pd.read_csv("../data/campaigns.csv")
campaigns_cleaned_df = clean_campaigns(campaigns_df)

messages_df = pd.read_csv("../data/messages.csv")

def get_clients_info_from_messages(df):
    clients = df[['client_id', 'user_id', 'user_device_id', 'email_provider']]
    ans = {}
    for i, row in clients.iterrows():
        if (row['client_id'], row['user_id'], row['user_device_id']) in ans and pd.isna(
                ans[(row['client_id'], row['user_id'], row['user_device_id'])]):
            if not pd.isna(row['email_provider']):
                ans[(row['client_id'], row['user_id'], row['user_device_id'])] = row['email_provider']
        else:
            ans[(row['client_id'], row['user_id'], row['user_device_id'])] = row['email_provider']

    return ans


clients_from_mes_df = get_clients_info_from_messages(messages_df)

clients_df = pd.read_csv("../data/client_first_purchase_date.csv")
clients_df_dict = clients_df.set_index(['client_id', 'user_id', 'user_device_id']).to_dict()['first_purchase_date']

keys = set(clients_from_mes_df.keys())
for k in list(clients_df_dict.keys()):
    keys.add(k)

rows = []
for k in keys:
    row = {"client_id":k[0],"user_id":k[1],"user_device_id":k[2]}
    if k in clients_from_mes_df:
        row["email_provider"] = clients_from_mes_df[k]
    else:
        row["email_provider"] = np.nan

    if k in clients_df_dict:
        row["first_purchase_date"] = clients_df_dict[k]
    else:
        row["first_purchase_date"] = np.nan
    rows.append(row)
fin_clients = pd.DataFrame(rows)
fin_clients.to_csv("../data/postgres/clients.csv", index=False)

def clean_messages(df):
    df = df.drop(columns=['user_id', 'user_device_id', 'email_provider', 'category', 'id'])
    df.to_csv("../data/postgres/messages.csv", index=False)
    return df

cleaned_messages_df = clean_messages(messages_df)

friends_df = pd.read_csv("../data/friends.csv")
friends_df.to_csv("../data/postgres/friends.csv", index=False)

events_df = pd.read_csv("../data/events.csv")
events_df.to_csv("../data/postgres/events.csv", index=False)