from __future__ import print_function
from datetime import date, datetime, timedelta
from kafka import KafkaConsumer
import mysql.connector
import json

consumer = KafkaConsumer(
    'ulima',
     bootstrap_servers= 'kub757l47naa.streaming.us-ashburn-1.oci.oraclecloud.com:9092',
     consumer_timeout_ms= -1,
     group_id='my-group',
     security_protocol =  'SASL_SSL',
     sasl_mechanism = 'PLAIN',
     sasl_plain_username = 'r0192549/20192549@aloe.ulima.edu.pe/ocid1.streampool.oc1.iad.amaaaaaa62teq4ia6updji4ih272qizl44ibd6x55divrogskub757l47naa',
     sasl_plain_password = '<<C5i2)odI))IO434+Fl')


for dato in consumer:



  body = json.loads(dato.value.decode())
  tipo = body.get("tipo")
  fecha = body.get("fecha")[:10]

  print(f"El dato es: {body}")

  print(f"datos son: {tipo} {fecha}")

  cnx = mysql.connector.connect(user='admin', password='.1adminSQL1.',
                              host='20.1.2.234',
                              database='exam4')
  cursor = cnx.cursor()

  query = f"INSERT INTO votacion (tipo, fecha) VALUES ('{tipo}','{fecha}');"

  cursor.execute(query)
  cnx.commit()

  cursor.close()
  cnx.close()

  print("%s:%d:%d: key=%s valor%s" % (dato.topic,dato.partition,dato.offset,dato.key,dato.value))

