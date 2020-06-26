from pyspark import SparkConf, SparkContext
conf = SparkConf()

# Tengo suficiente espacio en home para cargar la base de datos, mientras
# que no tengo suficiente en tmp
conf.set('spark.local.dir', '/home')

sc = SparkContext()

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.csv('all_data.csv', header='true')

#df.show()

df.printSchema()

# Total de registros
df.count()
# 62530715 registros

# Creamos la tabla temporal llamada Profeco
df.registerTempTable("Profeco")

sqlContext.sql("Select Count(categoria) From Profeco").show()
# 61643377 Categorias
sqlContext.sql("Select Count(Distinct(categoria)) From Profeco").show()
 # 41 categorias distintas

sqlContext.sql("Select Count(cadenaComercial) From Profeco").show()
# 62529531 Cadenas Comerciales
sqlContext.sql("Select Count(Distinct(cadenaComercial)) From Profeco").show()
# 705 Cadenas Comerciales distintas

# Tomamos solo lineas de productos en Guanajuato para hacer el mapa interactivo
Guanajuato_table = sqlContext.sql("Select * From Profeco Where estado='GUANAJUATO'")

Guanajuato_table.count()
# Hay 2'638,456 registros

# Lo exportare a un csv para trabajar esta parte por separado
Guanajuato_table.coalesce(1).write.csv('Guanajuato_table.csv', header = True)
