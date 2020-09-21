import os
#from azure.servicebus import QueueServiceClient, QueueClient
#from azure.servicebus import ServiceBusClient, Message
from azure.servicebus.control_client import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

conn_string = "Endpoint=sb://kanmessagebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=4nmSLvepaBF3xJUDe2tddYdJXeSnDgdcj2+WiN2GJwM="

# sb_client = ServiceBusClient.from_connection_string(conn_string)
# topic_client = sb_client.get_topic("weather_station")



def sendWeatherData(msg):
    try:
        bus_service = ServiceBusService(
        service_namespace='kanmessagebus',
        shared_access_key_name='weather',
        shared_access_key_value='tweaVJ8+++wUl3f568/E9vgAH21FK2SpcPBXn5F8Kts=')

        mesage = Message(msg)
        bus_service.send_topic_message("weather_station", mesage)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def sendWindBeringData(msg):
    try:
        bus_service = ServiceBusService(
        service_namespace='kanmessagebus',
        shared_access_key_name='client',
        shared_access_key_value='dNj7Z+fOvV49WNETUL0Guj3KVVdZude/fqzmj95GHKo=')

        mesage = Message(msg)
        bus_service.send_topic_message("wind_bearing", mesage)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

