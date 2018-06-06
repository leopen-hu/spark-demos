from pyspark.sql import SparkSession
import datetime

if __name__ == "__main__":
    spark = (SparkSession.builder
      .appName("Spark Mysql Simple Application")
      .config("spark.some.config.option", "some-value")
      .getOrCreate())

    df = (spark.read
      .format("jdbc")
      .option("url", "jdbc:mysql://10.25.75.138/jigglypuff?charset=utf8")
      .option("dbtable", "wind_all_data")
      .option("user", "root")
      .option("password", "123123")
      .load())

    # sql operate
    df.groupBy("metric").count().show()


    spark.stop()    
