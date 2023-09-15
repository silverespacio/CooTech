# CooTech: Cooperativa Tecnológica
Este es un proyecto elaborado para procesar transacciones con tarjetas en dispositivos POS, de manera a poder analizar los datos 
y presentar informes que permita tomar decisiones a la gerencia de la empresa.
Para lograr esto utilizamos las siguientes Herramientas:
* Docker: Automatización del despliegue de aplicaciones en contenedores.
* Procesamiento de Transacciones a partir de un archivo csv
* Redpanda: Plataforma de streaming de datos para procesamiento en tiempo real.
* KSQLDB: Herramienta SQL para procesamiento de streaming en tiempo real.

# Iniciamos la configuración de los contenedores y el procesamiento de los datos
1. Clonamos el repositorio de Git
   <p><code>git clone https://github.com/silverespacio/CooTech.git</code></p>
   
2. Creamos los contenedores y las iniciamos
   <p><code>docker-compose up -d</code></p>

3. Iniciar el procesamiento de las transacciones
   * Archivo: formato csv con transacciones
   * Topic redpanda: tran-tarjeta
   * Frecuencia de Procesamiento: 5 segundos
   <p><code>$ py -m producer Transacciones.csv tran-tarjeta 5</code></p>

4. Iniciamos la interación con el sqldb-cli
   <p><code>docker exec -it ksqldb-cli ksql http://ksqldb-server:8088</code></p>

5. Ejecutar Script Inicial
   <p><code>RUN SCRIPT '\files\ksql_crear.sql';</code></p>
   
6. Configurar ksqlDB para leer desde el inicio de la secuencia
   <p><code>SET 'auto.offset.reset' = 'earliest';</code></p>

8. Sentencias adicionales para la visualización de los datos
   <p><code>'\files\ksql_mostrar.sql';</code></p>
   
9. Consumir los datos procesados en formato json
   <p><code>$ py -m consumer tran-tarjeta</code></p>  
 
