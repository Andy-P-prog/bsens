from influxdb import InfluxDBClient
import json


def download(series = 'test',table ='test',database='BSENS_Connect'):
    
     
    client = InfluxDBClient(host='localhost',
                            port=8086,
                            database=database)
    result = client.query('SELECT * FROM test')
    test_points = list(result.get_points(measurement=table))

    client.close()
    with open('data.json ', 'w')  as outfile:
        json.dump(test_points, outfile, indent=4) 
    
download()