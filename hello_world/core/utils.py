import datetime 

def decode_request_parameters(request):
    params = {}
    for key, value in request.query_params.items():
        params[key] = value
    return params 

def decode_request_body(request):
    print(request.data,type(request.data))
    if isinstance(request.data,dict):
        return request.data     
    else:
        raise SystemError

def decode_request_args(request):
    return request.parser_context.get('args')

def decode_request_kwargs(request):
    return request.parser_context.get('kwargs')

def convert_to_datetime_string(datetime_obj:datetime):
    return datetime_obj.strftime("%d-%b-%Y %H:%M:%S")

def convert_to_date_string(datetime_obj:datetime):
    return datetime_obj.strftime("%d-%b-%Y")
