#!/bin/bash

watch_record="/data/home/hyw/data/watch_record.csv" 

# 这里的-f参数判断$myFile是否存在 
if [ ! -f "$watch_record" ]; then 
echo "watch_record not exist" 
fi 



#逐行读取文本
cat $watch_record | while read line
do
    #awk 读取
    id=`echo $line | awk -F ';' '{print $1}' |sed 's/\"//g'`	
    device_id=`echo $line | awk -F ';' '{print $2}' |sed 's/\"//g'`	
    res_id=`echo $line | awk -F ';' '{print $3}' |sed 's/\"//g'`	
    res_type=`echo $line | awk -F ';' '{print $4}' |sed 's/\"//g'`	
    person_id=`echo $line | awk -F ';' '{print $5}' |sed 's/\"//g'`	
    watch_time=`echo $line | awk -F ';' '{print $6}' |sed 's/\"//g'`	
    finished=`echo $line | awk -F ';' '{print $7}' |sed 's/\"//g'`	
    watch_record=`echo $line | awk -F ';' '{print $8}' |sed 's/\"//g'`	
    watch_progress=`echo $line | awk -F ';' '{print $9}' |sed 's/\"//g'`
    
    #echo 
    echo "-------------$line----------------"
    echo $id
    echo $device_id
    echo $res_id
    echo $res_type
    echo $person_id
    echo $watch_time
    echo $finished
    echo $watch_record
    echo $watch_progress



    curl -i -X POST -H "Content-Type: application/json" -d '{"robot_id":"22e3f139-8592-11e7-ba8b-7cd30ab71dd0", "table_name" : "user_action",  "table_content": [{"cmd":"add", "fields":{"id": "'$id'", "device_id":"'$device_id'", "res_id":"'$res_id'","res_type": "'$res_type'", "person_id": "'$person_id'", "watch_time":"'$watch_time'", "finished":"'$finished'", "watch_record":"'$watch_record'", "watch_progress":"'$watch_progress'"}}]}' 'http://datareport.dev.ailadui.net/v1/api/report'

done