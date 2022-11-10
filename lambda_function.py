from ping3 import ping
def lambda_handler(event, context):
    result = ping("us.qinyupeng.com")
    if result:
        return{"result": "success"}
    else:
        return{"result": "failed"}
