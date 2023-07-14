import io
import json
import logging
import oci

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    
    oci_configuration = oci.config.from_file("config.ini","DEFAULT")
    oci_service_endpoint = "https://cell-1.queue.messaging.us-ashburn-1.oci.oraclecloud.com"
    oci_queue_id = ocid1.fnapp.oc1.iad.aaaaaaaa5vkl66ihuu4qbgddbdgvpe4w725irlcgebanxtbzv27sbechoh7q
    oci_queue_client = oci.queue.QueueClient(config=oci_configuration, service_endpoint=oci_service_endpoint)
    
    tipo = "Peruana"
    
    try:
        
        body = json.loads(data.getvalue())
        
        tipo = body.get("tipo")
        
    except (Exception, ValueError) as ex:
        
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    
    return response.Response(
        
        response = publish_message(oci_queue_client,oci_queue_id,message_content=tipo)
        
    )


def publish_message(oci_queue_client, oci_queue_id, message_content):
        publish_message_response = oci_queue_client.put_messages(
        queue_id=oci_queue_id,
        put_messages_details=oci.queue.models.PutMessagesDetails(
            messages=[
                oci.queue.models.PutMessagesDetailsEntry(content=message_content)])
        )
        return publish_message_response