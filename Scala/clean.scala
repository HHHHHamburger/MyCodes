package main.scala

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import scala.collection.mutable.ListBuffer
import org.apache.hadoop.hbase.util.Bytes
import org.apache.hadoop.hbase.client.Put
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.spark.rdd.RDD.rddToPairRDDFunctions
import scala.collection.mutable.ListBuffer

object ParseClient {
  def main(args: Array[String]) {
    val conf = new SparkConf();
conf.setAppName("ParseClient")
    conf.setMaster("local");
val sc = new SparkContext(conf);
val textRdd = sc.textFile("WW_2016-10-13～2016-10-13.txt");
///数据清洗
var smailList = new ListBuffer[String]();
val arrRdd = textRdd.flatMap { line => {
      val allList = new ListBuffer[ListBuffer[String]]();
if (line == "" || "".equals(line)) {
        allList += smailList;
smailList = new ListBuffer[String]();
} else {
        smailList += line;
}
      allList;
}
    }

    val truncArrRdd = arrRdd.map { arr => {
      val lineArr = new ListBuffer[(String, String, String, String)];
arr.foreach { element => {
        val eleArr = element.split(" ");
if (eleArr.length >= 4) {
          val tuple = (eleArr(0), eleArr(1), eleArr(2), eleArr(3));
lineArr += tuple;
}
      }
      }
      lineArr
    }
    }

    val resultRdd = truncArrRdd.map(tupleArr => {
      var serviceName: String = "";
var cosumerName: String = "";
var date: String = "";
var context: String = "";
for (tuple <- tupleArr) {
        if (tuple._3.contains("官方旗舰店")) {
          serviceName = tuple._3
        } else {
          cosumerName = tuple._3;
}
        date = tuple._1;
context = context + tuple._4 + "\n";
}

      (cosumerName, serviceName, date, context);
})




package main.scala

import java.util

import scala.collection.mutable.{ListBuffer, LinkedHashMap}
import org.apache.hadoop.hbase.util.Bytes
import org.apache.hadoop.hbase.{KeyValue, HBaseConfiguration}
import org.apache.hadoop.mapreduce.Job
import org.apache.spark.SparkContext
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.hbase.client.{Get, Scan, HTable, Result}
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.hadoop.hbase.mapreduce.{TableInputFormat, TableOutputFormat}

class HBaseCommon {
  /**
   * 获取初始化配置
   */
def getConfiguration(): Configuration = {
    val map: LinkedHashMap[String, String] = new LinkedHashMap[String, String]();
val HBASE_CONFIG = new Configuration();
HBASE_CONFIG.set("hbase.zookeeper.quorum", map.getOrElse("zookeeper_quorum", "host1,host2,host3"));
HBASE_CONFIG.set("hbase.zookeeper.property.clientPort", map.getOrElse("zookeeper_port", "2181"));
val configuration = HBaseConfiguration.create(HBASE_CONFIG);
configuration;
}

  /**
   * 获取作业信息
   */
def getJob(tableName: String): Job = {
    val configuration = this.getConfiguration();
configuration.set(TableOutputFormat.OUTPUT_TABLE, tableName);
var job = new Job(configuration)
    job.setOutputKeyClass(classOf[ImmutableBytesWritable])
    job.setOutputValueClass(classOf[Result])
    job.setOutputFormatClass(classOf[TableOutputFormat[ImmutableBytesWritable]])
    job;
}

  /**
   * 读取hbase某个表中的全部内容
   */
def getTableInfo(tableName: String, sc: SparkContext): util.ArrayList[String]= {
    val configuration = this.getConfiguration()
    configuration.set(TableInputFormat.INPUT_TABLE, tableName)

    val hBaseRDD = sc.newAPIHadoopRDD(configuration, classOf[TableInputFormat],
classOf[org.apache.hadoop.hbase.io.ImmutableBytesWritable],
classOf[org.apache.hadoop.hbase.client.Result])

    var strinfo = ""
val count = hBaseRDD.count()
    println("HBase RDD Count:" + count)
    hBaseRDD.cache()

    val table = new HTable(configuration, tableName);
val g = new Get("row1".getBytes)
    val result = table.get(g)
    val value = Bytes.toString(result.getValue("basic".getBytes, "name".getBytes))

    hBaseRDD.cache()
    println("------------------------scan----------")
    val res = hBaseRDD.take(count.toInt)
    val reslist=new util.ArrayList[String]()
    for (j <- 1 until count.toInt) {
      var rs = res(j - 1)._2
      var kvs = rs.raw
      for (kv <- kvs) {
        strinfo += ("rowkey:" + new String(kv.getRow()) +
          " cf:" + new String(kv.getFamily()) +
          " column:" + new String(kv.getQualifier()) +
          " value:" + new String(kv.getValue())+"\n")

        reslist.add(new String(kv.getValue()))
      }
    }
    reslist
  }
}


package com.qifun.csvParserUtil

import com.qifun.csvParser.CsvReader
import java.io.File
import scala.annotation.tailrec

/*
 * 实现将CsvAsArray的数据结构转化成scala的二维数组
 * 封装了两个函数
 * getValue(a),得到第a行的数据
 * getValue(a,b),得到第a行b列的数据
 */
class CsvAsArray(csvReader: CsvReader) {
  val csvArray = searchCsvArray()
  val highLength = csvArray.length
  val wideLength = if (highLength > 0) csvArray(0).length else 0
  
  def getValue(a: Int, b: Int): String = {
    if ((a < highLength) && (b < wideLength)) csvArray(a)(b)
    else throw new Exception("out of range!")
  }
  def getValue(a: Int): Array[String] = {
    if (a < highLength) csvArray(a)
    else throw new Exception("out of range!")
  }
  
  private def searchCsvArray(): Array[Array[String]] = {//把CsvAsArray的数据结构转化成scala的二维数组
    val iterator = csvReader.iterator                   //使用Array.newBuilder
    val csvArray = Array.newBuilder[Array[String]]    //学习尾递归的用法
    @tailrec def getCsvLine() {
      if (iterator.hasNext) {
        csvArray += iterator.next()
        getCsvLine()
      }
    }

    getCsvLine()
    csvArray.result()
  }
}
