import io
import json
import logging
import oci

from fdk import response
from base64 import b64encode

ociMessageEndpoint = "https://kub757l47naa.streaming.us-ashburn-1.oci.oraclecloud.com"
ociStreamOcid = "ocid1.stream.oc1.iad.amaaaaaa62teq4iakgzdobxobtobdf3mrjt2fdj74muyzcguq34jaaukwhsq"
ociConfigFilePath = "/function/conf.ini"
ociProfileName = "DEFAULT"

config = oci.config.from_file(ociConfigFilePath, ociProfileName)
stream_client = oci.streaming.StreamClient(config, service_endpoint=ociMessageEndpoint)


def handler(ctx, data: io.BytesIO = None):
    
    key = "ulima"
    tipo = "variable"
    fecha = "variable2"

    value = json.dumps({'tipo':tipo, 'fecha':fecha})

    try:
        
        
        encoded_key = b64encode(key.encode()).decode()
        encoded_value = b64encode(value.encode()).decode()
        mensaje = oci.streaming.models.PutMessagesDetailsEntry(key=encoded_key, value=encoded_value)
        
        lista_mensaje = oci.streaming.models.PutMessagesDetails(messages=[mensaje])

        put_message_result = stream_client.put_messages(ociStreamOcid, lista_mensaje)

        logging.getLogger().info(put_message_result)
        
    except (Exception,ValueError) as identifier:
        logging.getLogger().info(str(identifier))
    
    return response.Response( 
        ctx, response_data=json.dumps({'tipo':tipo, 'fecha':fecha}),headers={"Content-Type":"application/json"}
    )