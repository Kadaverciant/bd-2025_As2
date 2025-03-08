import numpy as np
import pandas as pd
import warnings
import os
import json
import datetime

warnings.filterwarnings('ignore')
folder = "cleaned"

try:
    os.makedirs(f"./data/{folder}")
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

    df.to_csv(f"./data/{folder}/campaigns.csv", index=False)
    df.reset_index().to_json(f"./data/{folder}/campaigns.json", orient='records', date_format='iso', index=False)

    with open(f"./data/{folder}/campaigns.json", 'r+') as f:
        data = json.load(f)
        for k in data:
            k.pop('index')
            if k['started_at'] is not None:
                k['started_at'] = {
                    "$date": datetime.datetime.strptime(k['started_at'], "%Y-%m-%d %H:%M:%S.%f").strftime(
                        "%Y-%m-%dT%H:%M:%S.%fZ")}
            if k['finished_at'] is not None:
                k['finished_at'] = {
                    "$date": datetime.datetime.strptime(k['finished_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}

        f.seek(0)
        f.write(json.dumps(data, indent=2))
        f.truncate()
    return df

print("start cleaning campaigns")
campaigns_df = pd.read_csv("./data/campaigns.csv")
campaigns_cleaned_df = clean_campaigns(campaigns_df)
print("finish cleaning campaigns")

print("start cleaning messages")
messages_df = pd.read_csv("./data/messages.csv")

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


print("start building clients")
clients_from_mes_df = get_clients_info_from_messages(messages_df)

clients_df = pd.read_csv("./data/client_first_purchase_date.csv")
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
fin_clients.to_csv(f"./data/{folder}/clients.csv", index=False)
fin_clients.reset_index().to_json(f"./data/{folder}/clients.json", orient='records', date_format='iso', index=False)
with open(f"./data/{folder}/clients.json", 'r+') as f:
    data = json.load(f)
    for k in data:
        k.pop('index')
        if k['first_purchase_date'] is not None:
            k['first_purchase_date'] = {
                "$date": datetime.datetime.strptime(k['first_purchase_date'], "%Y-%m-%d").strftime("%Y-%m-%dT%H:%M:%SZ")}

    f.seek(0)
    f.write(json.dumps(data, indent=2))
    f.truncate()
print("finish building clients")

def clean_messages(df):
    df = df.drop(columns=['user_id', 'user_device_id', 'email_provider', 'category', 'id'])

    df[["is_opened", "is_clicked", "is_unsubscribed", "is_hard_bounced", "is_soft_bounced", "is_complained", "is_blocked", "is_purchased"]] = messages_df[["is_opened", "is_clicked", "is_unsubscribed", "is_hard_bounced", "is_soft_bounced", "is_complained", "is_blocked", "is_purchased"]].replace({"t": True, "f": False})
    df.to_csv(f"./data/{folder}/messages.csv", index=False)
    df.reset_index().to_json(f"./data/{folder}/messages.json", orient='records', date_format='iso', index=False)
    with open(f"./data/{folder}/messages.json", 'r+') as f:
        data = json.load(f)
        for k in data:
            k.pop('index')
            if k['date'] is not None:
                k['date'] = {
                    "$date": datetime.datetime.strptime(k['date'], "%Y-%m-%d").strftime("%Y-%m-%dT%H:%M:%SZ")}
            if k['sent_at'] is not None:
                k['sent_at'] = {
                    "$date": datetime.datetime.strptime(k['sent_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['opened_first_time_at'] is not None:
                k['opened_first_time_at'] = {
                    "$date": datetime.datetime.strptime(k['opened_first_time_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['opened_last_time_at'] is not None:
                k['opened_last_time_at'] = {
                    "$date": datetime.datetime.strptime(k['opened_last_time_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['clicked_first_time_at'] is not None:
                k['clicked_first_time_at'] = {
                    "$date": datetime.datetime.strptime(k['clicked_first_time_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['clicked_last_time_at'] is not None:
                k['clicked_last_time_at'] = {
                    "$date": datetime.datetime.strptime(k['clicked_last_time_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['unsubscribed_at'] is not None:
                k['unsubscribed_at'] = {
                    "$date": datetime.datetime.strptime(k['unsubscribed_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['hard_bounced_at'] is not None:
                k['hard_bounced_at'] = {
                    "$date": datetime.datetime.strptime(k['hard_bounced_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['soft_bounced_at'] is not None:
                k['soft_bounced_at'] = {
                    "$date": datetime.datetime.strptime(k['soft_bounced_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['complained_at'] is not None:
                k['complained_at'] = {
                    "$date": datetime.datetime.strptime(k['complained_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['blocked_at'] is not None:
                k['blocked_at'] = {
                    "$date": datetime.datetime.strptime(k['blocked_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['purchased_at'] is not None:
                k['purchased_at'] = {
                    "$date": datetime.datetime.strptime(k['purchased_at'], "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
            if k['created_at'] is not None:
                try:
                    k['created_at'] = {
                        "$date": datetime.datetime.strptime(k['created_at'], "%Y-%m-%d %H:%M:%S.%f").strftime(
                            "%Y-%m-%dT%H:%M:%S.%fZ")}
                except:
                    k['created_at'] = {
                        "$date": datetime.datetime.strptime(k['created_at'], "%Y-%m-%d %H:%M:%S").strftime(
                            "%Y-%m-%dT%H:%M:%S.%fZ")}
            if k['updated_at'] is not None:
                try:
                    k['updated_at'] = {
                        "$date": datetime.datetime.strptime(k['updated_at'], "%Y-%m-%d %H:%M:%S.%f").strftime(
                            "%Y-%m-%dT%H:%M:%S.%fZ")}
                except:
                    k['updated_at'] = {
                        "$date": datetime.datetime.strptime(k['updated_at'], "%Y-%m-%d %H:%M:%S").strftime(
                            "%Y-%m-%dT%H:%M:%S.%fZ")}

        f.seek(0)
        f.write(json.dumps(data, indent=2))
        f.truncate()

    return df

cleaned_messages_df = clean_messages(messages_df)
print("finish cleaning messages")

print("start cleaning friends")
friends_df = pd.read_csv("./data/friends.csv")
friends_df.to_csv(f"./data/{folder}/friends.csv", index=False)
friends_df.reset_index().to_json(f"./data/{folder}/friends.json", orient='records', date_format='iso', index=False)
with open(f"./data/{folder}/friends.json", 'r+') as f:
    data = json.load(f)
    for k in data:
        k.pop('index')
    f.seek(0)
    f.write(json.dumps(data, indent=2))
    f.truncate()
print("finish cleaning friends")

print("start cleaning events")
events_df = pd.read_csv("./data/events.csv")

print("start building products")
def get_products_from_events(df):
    products = df[['product_id', 'brand']]
    products = products.drop_duplicates()
    ans = {}
    for i, row in products.iterrows():
        if row['product_id'] in ans and pd.isna(ans[row['product_id']]):
            if not pd.isna(row['brand']):
                ans[row['product_id']] = row['brand']
            else:
                print("Panic, some product has several non null brands")
        else:
            ans[row['product_id']] = row['brand']

    rows = []
    for k, v in ans.items():
        row = {"product_id":k, "brand":v}
        rows.append(row)
    fin_df = pd.DataFrame(rows)
    fin_df.to_csv(f"./data/{folder}/products.csv", index=False)
    fin_df.reset_index().to_json(f"./data/{folder}/products.json", orient='records', date_format='iso', index=False)

    with open(f"./data/{folder}/products.json", 'r+') as f:
        data = json.load(f)
        for k in data:
            k.pop('index')
        f.seek(0)
        f.write(json.dumps(data, indent=2))
        f.truncate()

    return fin_df

products_df = get_products_from_events(events_df)
print("finish building products")

print("start building categories")
def get_categories_from_events(df):
    categories = df[['category_id', 'category_code']]
    categories = categories.drop_duplicates()
    ans = {}
    for i, row in categories.iterrows():
        if row['category_id'] in ans and pd.isna(ans[row['category_id']]):
            if not pd.isna(row['category_code']):
                ans[row['category_id']] = row['category_code']
            else:
                print("Panic, some category_id has several non null category_code")
        else:
            ans[row['category_id']] = row['category_code']

    rows = []
    for k, v in ans.items():
        row = {"category_id":k, "category_code":v}
        rows.append(row)
    fin_df = pd.DataFrame(rows)
    fin_df.to_csv(f"./data/{folder}/categories.csv", index=False)
    fin_df.reset_index().to_json(f"./data/{folder}/categories.json", orient='records', date_format='iso', index=False)
    with open(f"./data/{folder}/categories.json", 'r+') as f:
        data = json.load(f)
        for k in data:
            k.pop('index')
        f.seek(0)
        f.write(json.dumps(data, indent=2))
        f.truncate()

    return fin_df

categories_df = get_categories_from_events(events_df)
print("finish building categories")

def clean_events(df):
    df = df.drop(columns=['category_code', 'brand'])
    df.to_csv(f"./data/{folder}/events.csv", index=False)
    df.reset_index().to_json(f"./data/{folder}/events.json", orient='records', date_format='iso', index=False)
    with open(f"./data/{folder}/events.json", 'r+') as f:
        data = json.load(f)
        for k in data:
            k.pop('index')
            if k['event_time'] is not None:
                k['event_time'] = {
                    "$date": datetime.datetime.strptime(k['event_time'], "%Y-%m-%d %H:%M:%S UTC").strftime(
                        "%Y-%m-%dT%H:%M:%SZ")}
        f.seek(0)
        f.write(json.dumps(data, indent=2))
        f.truncate()

    return df

cleaned_events_df = clean_events(events_df)
print("finish cleaning events")