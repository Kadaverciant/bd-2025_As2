import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


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

    df.to_csv("../data/campaigns_cleaned.csv", index=False)
    return df


pd.read_csv("../data/campaigns.csv")

messages_df = pd.read_csv("../data/messages.csv")
clients_df = pd.read_csv("../data/client_first_purchase_date.csv")
available_users = clients_df["client_id"].values.tolist()

messages_cleaned_df = messages_df[messages_df["client_id"].isin(available_users)]
messages_cleaned_df.to_csv("../data/messages_cleaned.csv", index=False)