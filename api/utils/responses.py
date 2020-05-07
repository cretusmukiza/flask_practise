from flask import jsonify,make_response
def response_with(response=None,value=None,
message=None,errors=None,headers={},pagination=None):
    result = {}
    if value is not None:
        result.update(value)
    
    if response.get('message',None) is not None:
        result.update({'message':response['message']})
    
    result.update({'code',response['code']})

    if errors is not None:
        result.update({'errors': errors})

    if pagination is not None:
        response.update({'pagination':pagination})
    
    headers.update({'Access-Control-Allow-Origin':'*'})
    headers.update({'server':'Flask Rest Api'})

    return make_response(jsonify(result),response['http_code'],headers)


INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "code": "invalidField",
    "message": "Invalid fields found"
}





    
    