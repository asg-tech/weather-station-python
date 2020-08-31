import os
#from azure.servicebus import QueueServiceClient, QueueClient
from azure.servicebus import ServiceBusClient, Message

conn_string = "Endpoint=sb://kanmessagebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=4nmSLvepaBF3xJUDe2tddYdJXeSnDgdcj2+WiN2GJwM="

sb_client = ServiceBusClient.from_connection_string(conn_string)
topic_client = sb_client.get_topic("weather_station")

def sendMessageToQueue(msg):
    try:

        message_one = Message(msg)

        with topic_client.get_sender() as sender:
            sender.send(message_one)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)


