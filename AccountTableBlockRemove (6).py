# import boto3
# from boto3.dynamodb.conditions import Key
import csv
# import pprint

    # table_name = "AmstackInProdCognitoUserAccountLevelInfo"
    # dynamodb = boto3.resource('dynamodb')
    # account_table = dynamodb.Table(table_name)


with open("Input_file.csv", 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        ABO = str(row[0])
        print("ABO: ", ABO)
        
        # keyConditionExpression = Key('accountNumber').eq(ABO)
        # response1 = account_table.query(KeyConditionExpression=keyConditionExpression)
# try:
#     account_response = account_table.update_item(
        Key={
             'accountNumber': ABO
             },
        print(ABO + "+") 
#             UpdateExpression='REMOVE blockPrivilegeList',
#             ConditionExpression= 'accountNumber= :accNum',
#             ExpressionAttributeValues={
#                 ':accNum': ABO
# 				},
#             ReturnValues="ALL_NEW"
#         )
#     print(ABO)
# # exception handling
# except Exception as e:
#     print(f'Exception occured while updating Accounts table. Exception is : {e}')              
  
# else:
#     print(f'Account table updated successfully')






