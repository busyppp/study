#리스트와 dict형 api 불러오기
import urllib.request
import json
import csv

url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1'
res = urllib.request.urlopen(url).read()
output = json.loads(res)
output = output['storeInfos']
# print(type(output))
# print(output)

# print(output[0].keys())
output_file = 'api_out.csv'

try:
    with open(output_file, 'w', newline='', encoding='cp949') as csvfile:
        writer = csv.DictWriter(csvfile, output[0].keys())
        writer.writeheader()
        for data in output:
            writer.writerow(data)
except:
    print('Error')

########################################마스크api를 이용한 저장####################################
# import urllib.request
# import json
# import pandas as pd
# from pandas import json_normalize
#
# url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1'
# response = urllib.request.urlopen(url)
# json_str = response.read().decode("utf-8")
#
# json_object = json.loads(json_str)
# # print(json_object)
# body = [json_object['storeInfos']]
# print(body)
#
# output = json_normalize(json_object['storeInfos']) #리스트 앞에서 끊어주기
# print(output)
#
# data = pd.DataFrame(output) #저장하기
# data.columns = ['addr', 'code', 'lat', 'lng', 'name', 'type']
# data.to_csv('api_out1.csv', encoding='cp949')