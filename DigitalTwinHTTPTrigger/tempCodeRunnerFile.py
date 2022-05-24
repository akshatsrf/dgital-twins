 service_client = DigitalTwinsClient(url, credential)
    query_expression = 'SELECT * FROM digitaltwins'
    query_result = service_client.query_twins(query_expression)
    print('DigitalTwins:')
    # dataset = []
    for twin in query_result:
        print(twin)