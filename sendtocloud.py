import os
from azure.storage.queue import QueueServiceClient, QueueClient
from azure.servicebus  import ServiceBusClient

class QueueHelloWorldSamples(object):

    #connection_string = os.getenv(DefaultEndpointsProtocol=https;AccountName=kanstoragequeue;AccountKey=d+GcN9AHk7ptVQwwco5jChRwTbgHhod2Z8aMvqIxOwPVPAu+fgC4atuaq53rPw1orDG5hdwDWWv5yAyd0t407A==;EndpointSuffix=core.windows.net)

    # def create_client_with_connection_string(self):
    #     # Instantiate the QueueServiceClient from a connection string
    #     #from azure.storage.queue import QueueServiceClient
    #     ####queue_service = QueueServiceClient.from_connection_string(conn_str='Endpoint=sb://kanmessagebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey="4nmSLvepaBF3xJUDe2tddYdJXeSnDgdcj2+WiN2GJwM="')
    #     queue_service = ServiceBusService(service_namespace = "kanmessagebus ",
    #                     shared_access_key_name=key_name,
    #                     shared_access_key_value=key_value)
    #     from_connection_string(conn_str='Endpoint=sb://kanmessagebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey="4nmSLvepaBF3xJUDe2tddYdJXeSnDgdcj2+WiN2GJwM="')
    #     #queue_service = QueueServiceClient.from_connection_string(conn_str="d+GcN9AHk7ptVQwwco5jChRwTbgHhod2Z8aMvqIxOwPVPAu+fgC4atuaq53rPw1orDG5hdwDWWv5yAyd0t407A==")
    #     # Get queue service properties
    #     properties = queue_service.get_service_properties()

    def SetupAzure(self):   
        try:
            conStr = 'Endpoint=sb://kanmessagebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=4nmSLvepaBF3xJUDe2tddYdJXeSnDgdcj2+WiN2GJwM='
            client = ServiceBusClient.from_connection_string(conStr)
            return client.get_topic("weatherflowjsondatagaatp")
            #return client.get_queue("weatherflowjsondatagaa")

        except:
            print("Azure setup error")
            return None

    # def queue_and_messages_example(self,pushvar):
    #     # Instantiate the QueueClient from a connection string
    #     #from azure.storage.queue import QueueClient
    #     #queue = QueueClient.from_connection_string(conn_str='Endpoint=sb://kanmessagebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey="4nmSLvepaBF3xJUDe2tddYdJXeSnDgdcj2+WiN2GJwM="', queue_name="weatherflowjsondatagaa")
    #     #queue = ServiceBusService()
    #     # Create the queue
    #     # [START create_queue]
    #     #queue.create_queue()
    #     # [END create_queue]
    #     pass
    #     # try:
    #     #     # Send messages
    #     #     #queue.send_queue_message(pushvar)
    #     #     #queue.send_message(u"This is my second message")
    #     #     print("try")
    #     #     # Receive the messages
    #     #     #response = queue.receive_queue_message()

    #     #     # Print the content of the messages
    #     #     # for message in response:
    #     #     #     print(message.content)

    #     # finally:
    #     #     pass
    #     #     # [START delete_queue]
    #     #     # queue.delete_queue()
    #     #     # [END delete_queue]

if __name__ == '__main__':
    #sample = QueueHelloWorldSamples()
    #sample.create_client_with_connection_string()
    #sample.queue_and_messages_example()
    print("h")