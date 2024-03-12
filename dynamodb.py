import boto3

my_table = "my_table"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(my_table)

item = table.get_item(Key={"id": "2"})
print("item['Item']:", item['Item'])

items = table.scan()
print("items['Items']:", items['Items'])


