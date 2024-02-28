print ("""ARN example: 
arn:partition:service:region:account-id:resource-id""")
par = str(input("partition: "))
ser = str(input("service: "))
reg = str(input("region: "))
acc_id = int(input("account-id: "))
res_id = int(input("resource-id: "))
result = f'arn:{par}:{ser}:{reg}:{acc_id}:{res_id}'
print (result)