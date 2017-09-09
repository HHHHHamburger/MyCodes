
package org.zige.recommend.algorithm.demo

import org.apache.hadoop.hbase.{HBaseConfiguration, HTableDescriptor, TableName}  
import org.apache.hadoop.hbase.client.HBaseAdmin  
import org.apache.hadoop.hbase.mapreduce.TableInputFormat  
import org.apache.spark._  
import org.apache.hadoop.hbase.client.HTable  
import org.apache.hadoop.hbase.client.Put  
import org.apache.hadoop.hbase.util.Bytes  
import org.apache.hadoop.hbase.io.ImmutableBytesWritable  
import org.apache.hadoop.hbase.mapreduce.TableOutputFormat  
import org.apache.hadoop.mapred.JobConf  
import org.apache.hadoop.io._   
import org.slf4j.LoggerFactory  
import com.typesafe.scalalogging.Logger 
  
object TestHBase {  
  
  def main(args: Array[String]): Unit = {  

    val logger = Logger(LoggerFactory.getLogger("name"))
    val sparkConf = new SparkConf().setAppName("HBaseTest")
    val sc = new SparkContext(sparkConf)  
      
    val tablename = "user_action"  

    val conf = HBaseConfiguration.create()  

    conf.set("hbase.zookeeper.quorum","LaDuiHbaseM01,LaDuiHbaseS02,LaDuiHbaseS03")  
    conf.set("hbase.zookeeper.property.clientPort", "2181")  
    
	//conf.set("zookeeper.znode.parent", "/hbase") 
    conf.set(TableInputFormat.INPUT_TABLE, tablename)  
	//conf.set(TableInputFormat.SCAN_ROW_START, "f15f0f6b-73b6-4cd4-be60-46b660551") 
	//conf.set(TableInputFormat.SCAN_ROW_STOP, "ff559eb2-0037-4eb6-a18a-cfd3de165") 
    
	logger.info("create hbase config")

    val hBaseRDD = sc.newAPIHadoopRDD(conf, classOf[TableInputFormat],  
      classOf[org.apache.hadoop.hbase.io.ImmutableBytesWritable],  
      classOf[org.apache.hadoop.hbase.client.Result])  
  
    val count = hBaseRDD.count()  

	logger.info("RDD COUNT")

    println(s"RDD count:$count")  

	
    hBaseRDD.foreach{case (_,result) =>{  
		  val key = Bytes.toString(result.getRow)  
		  val user_id = Bytes.toString(result.getValue("info".getBytes,"user_id".getBytes))  
		  val robot_id = Bytes.toString(result.getValue("info".getBytes,"robot_id".getBytes))  
		  println("Row key:"+key+" user_id:"+user_id+" robot_id:"+robot_id)  
		}
	}  
	
    sc.stop()  
  }  
  
}  
