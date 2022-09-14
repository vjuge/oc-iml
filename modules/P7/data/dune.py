from duneanalytics import DuneAnalytics
import json
import csv
import pandas as pd

def main():

    # initialize client
    dune = DuneAnalytics('altacryptos', 'Password01#')

    # try to login
    dune.login()

    # fetch token
    dune.fetch_auth_token()

    # fetch query result id using query id
    # query id for any query can be found from the url of the query:
    # for example: 
    # https://dune.com/queries/4494/8769 => 4494
    # https://dune.com/queries/3705/7192 => 3705
    # https://dune.com/queries/3751/7276 => 3751

    result_id = dune.query_result_id(query_id=9618)

    # fetch query result
    data = dune.query_result(result_id)
    data_reduced = data.get('data').get('get_result_by_result_id')
    print(data_reduced[0].get('data'))

    json_object = json.dumps(data_reduced, indent = 4)
    # print(json_object)

    df = pd.json_normalize(data_reduced, sep='_')

    print(df.to_dict(orient='records')[0])
    # print(json_object)


if __name__ =="__main__":
    main()