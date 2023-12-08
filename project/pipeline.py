

import pandas as pd
import sqlite3


wheather_url= 'https://archive-api.open-meteo.com/v1/archive?latitude=41.01&longitude=28.95&start_date=2022-10-01&end_date=2023-09-30&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation,rain,snowfall,snow_depth,windspeed_10m,windspeed_100m&timezone=Europe%2FMoscow&format=csv'



traffic_density_urls = {
    'oct_22': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/72183a60-d47f-4dc9-b1dc-fced0649dcf5/download/traffic_density_202210.csv',
    'nov_22': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/7f463362-a580-41d9-a86a-a542818e7542/download/traffic_density_202211.csv',
    'dec_22': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/dc788908-2b75-434f-9f3f-ef82ff33a158/download/traffic_density_202212.csv',
    'jan_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/42fa7a5f-29f1-4b38-9dfa-ac7c8fe3c77d/download/traffic_density_202301.csv',
    'feb_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/366befd8-defd-4f79-a3d2-0e7948c649ff/download/traffic_density_202302.csv',
    'mar_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/6a60b03a-bf25-4575-9dce-e21fe0e04e77/download/traffic_density_202303.csv',
    'apr_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/ce65562e-0d17-4d7e-8090-9484990a8f2b/download/traffic_density_202304.csv',
    'may_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/d0a71c11-47d2-4f98-8745-c9446b10bf18/download/traffic_density_202305.csv',
    'jun_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/a99913df-dccc-4b7d-b6e3-963ccb5d27b1/download/traffic_density_202306.csv',
    'jul_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/3de18c1e-57c0-4493-9b75-5a896edae0ff/download/traffic_density_202307.csv',
    'agu_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/f6a1e2d7-0d9f-4d84-90c6-2729a0869308/download/traffic_density_202308.csv',
    'sep_23': 'https://data.ibb.gov.tr/en/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/7b9a35a7-dc9c-4044-b117-1c0003104630/download/traffic_density_202309.csv'
}


public_transport_urls = {
    'oct_22': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/01373a9e-7ce5-4d7a-8969-bdd8d7a1ed15/download/hourly_transportation_202210.csv',
    'nov_22': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/e68869f5-8d10-4483-badd-cdec0ef3bc0e/download/hourly_transportation_202211.csv',
    'dec_22': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/22b57697-4d5c-473c-888e-cc0634e5f48b/download/hourly_transportation_202212.csv',
    'jan_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/afc1cec1-fd43-44a9-b5c0-977d3b1d60d7/download/hourly_transportation_202301.csv',
    'feb_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/6b430597-11fc-4d31-b0eb-c172c8e0e50d/download/hourly_transportation_202302.csv',
    'mar_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/eb32254e-3233-4ac9-ade0-cd056ccfa509/download/hourly_transportation_202303.csv',
    'apr_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/862a4927-7d69-4a06-a74e-24f1562d438f/download/hourly_transportation_202304.csv',
    'may_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/5782df57-1862-4fa2-80f2-a614254fad57/download/hourly_transportation_202305.csv',
    'jun_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/e44351e8-d85c-49c8-abc9-d8d5c9ac34ae/download/hourly_transportation_202306.csv',
    'jul_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/f0c798c8-bab4-479e-841b-e82422e38e7f/download/hourly_transportation_202307.csv',
    'agu_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/f4bafb5a-94a0-4ae9-8024-523287649579/download/hourly_transportation_202308.csv',
    'sep_23': 'https://data.ibb.gov.tr/en/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/b3f67274-4ebc-4453-8f6b-1dcc1b1bf008/download/hourly_transportation_202309.csv'
}


sql_doc="../data/data.sqlite"


def pull_public_transport(urls):
    
    
    public_transport_df_type_1 = pd.DataFrame()
    public_transport_df_type_2 = pd.DataFrame()
    public_transport_df_type_3 = pd.DataFrame()
    
    
    for month, url in urls.items():
        df2=pd.read_csv(url)
        df2['DATE_TIME'] = pd.to_datetime(df2['transition_date'] + ' ' + df2['transition_hour'].astype(str) + ':00:00')
        df2.drop(['transition_date', 'transition_hour'], axis=1, inplace=True)
    
        selected_columns =['DATE_TIME','transport_type_id','number_of_passage']
        df3 = df2[selected_columns]
    
        grouped_df2 = df3.groupby(['DATE_TIME', 'transport_type_id']).agg({
        'number_of_passage': 'sum'}).reset_index()
    
        df_transport_type_1 = grouped_df2[grouped_df2['transport_type_id'] == 1].copy()
        df_transport_type_2 = grouped_df2[grouped_df2['transport_type_id'] == 2].copy()
        df_transport_type_3 = grouped_df2[grouped_df2['transport_type_id'] == 3].copy()

        public_transport_df_type_1 = pd.concat([public_transport_df_type_1, df_transport_type_1], ignore_index=True)
        public_transport_df_type_2 = pd.concat([public_transport_df_type_2, df_transport_type_2], ignore_index=True)
        public_transport_df_type_3 = pd.concat([public_transport_df_type_3, df_transport_type_3], ignore_index=True)
    
    
    return public_transport_df_type_1,public_transport_df_type_2,public_transport_df_type_3


def pull_traffic_density(urls):
    traffic_density_df = pd.DataFrame()
    
    
    for month, url in urls.items():
        df1=pd.read_csv(url)
        df1['DATE_TIME'] = pd.to_datetime(df1['DATE_TIME'])
        selected_columns = ['DATE_TIME','AVERAGE_SPEED', 'NUMBER_OF_VEHICLES']
        df = df1[selected_columns]
        df['CUM_AVERAGE_SPEED'] = df.apply(lambda row: row['NUMBER_OF_VEHICLES'] * row['AVERAGE_SPEED'], axis=1)

        grouped_df = df.groupby('DATE_TIME').agg({
                            'NUMBER_OF_VEHICLES': 'sum',
                            'CUM_AVERAGE_SPEED': 'sum'
                                }).reset_index()
    
        grouped_df['AVERAGE_SPEED'] = grouped_df.apply(lambda row:  row['CUM_AVERAGE_SPEED']/row['NUMBER_OF_VEHICLES'], axis=1)
        grouped_df.drop('CUM_AVERAGE_SPEED', axis=1, inplace=True)
        traffic_density_df = pd.concat([traffic_density_df, grouped_df], ignore_index=True)
        
        
    return traffic_density_df


def pull_weather(url):
    df_weather = pd.read_csv(url, skiprows=2)
    return df_weather



def load(df,db,sql_doc):
    con=sqlite3.connect(sql_doc)
    cur=con.cursor()
    
    df.to_sql(name=db, con=con, if_exists="replace", index=False)

    con.commit()
    con.close()


if __name__ == '__main__':
    
    public_transport_df_type_1,public_transport_df_type_2,public_transport_df_type_3 = pull_public_transport(public_transport_urls)

    traffic_density_df=pull_traffic_density(traffic_density_urls)

    df_weather=pull_weather(wheather_url)

    load(public_transport_df_type_1,'public_transport_type_1',sql_doc)
    load(public_transport_df_type_2,'public_transport_type_2',sql_doc)
    load(public_transport_df_type_3,'public_transport_type_3',sql_doc)
    
    load(traffic_density_df,'traffic_density',sql_doc)

    load(df_weather,'weather',sql_doc)

