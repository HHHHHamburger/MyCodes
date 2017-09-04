#!/bin/bash

resources="/data/home/hyw/data/resources.csv"

# 这里的-f参数判断$myFile是否存在 
if [ ! -f "$resources" ]; then 
echo "resources not exist" 
fi 

#逐行读取文本
cat $resources | while read line
do
    #awk 读取
    video_id=`echo $line | awk -F ';' '{print $1}' |sed 's/\"//g'`
    course_type=`echo $line | awk -F ';' '{print $2}'|sed 's/\"//g'`
    seqc=`echo $line | awk -F ';' '{print $3}'|sed 's/\"//g'`
    grade=`echo $line | awk -F ';' '{print $4}'|sed 's/\"//g'`
    section=`echo $line | awk -F ';' '{print $5}'|sed 's/\"//g'`
    subject1=`echo $line | awk -F ';' '{print $7}'|sed 's/\"//g'`
    subject2=`echo $line | awk -F ';' '{print $8}'|sed 's/\"//g'`
    subject3=`echo $line | awk -F ';' '{print $9}'|sed 's/\"//g'`
    video_name=`echo $line | awk -F ';' '{print $10}'|sed 's/\"//g'`
    video_desc=`echo $line | awk -F ';' '{print $11}'|sed 's/\"//g'`
    video_keyword=`echo $line | awk -F ';' '{print $12}'|sed 's/\"//g'`
    resource_type=`echo $line | awk -F ';' '{print $13}'|sed 's/\"//g'`
    create_time=`echo $line | awk -F ';' '{print $17}'|sed 's/\"//g'`
    video_content=`echo $line | awk -F ';' '{print $20}'|sed 's/\"//g'`
    name=`echo $line | awk -F ';' '{print $21}'|sed 's/\"//g'`
    
    #echo 
    echo "-------------$line----------------"
    echo $video_id
    echo $course_type
    echo $seqc
    echo $grade
    echo $section
    echo $subject1
    echo $subject2
    echo $subject3
    echo $video_name
    echo $video_desc
    echo $video_keyword
    echo $resource_type
    echo $create_time
    echo $video_content
    echo $name

    echo '{"video_id": "'$video_id'", "cource_type":"'$course_type'", "seqc":"'$seqc'","grade": "'$grade'", "section": "'$section'", "subject1":"'$subject1'", "subject2":"'$subject2'", "subject3":"'$subject3'", "video_name":"'$video_name'", "video_desc":"'$video_desc'", "video_keyword":"'$video_keyword'", "resource_type":"'$resource_type'", "video_content":"'$video_content'","created_time":"'$created_time'", "name":"'$name'" }'
    curl -i -X POST -H "Content-Type: application/json" -d '{"robot_id":"22e3f139-8592-11e7-ba8b-7cd30ab71dd0", "table_name" : "educate_item",  "table_content": [{"cmd":"add", "fields": {"video_id": "'$video_id'", "cource_type":"'$cource_type'", "seqc":"'$seqc'","grade": "'$grade'", "section": "'$section'", "subject1":"'$subject1'", "subject2":"'$subject2'", "subject3":"'$subject3'", "video_name":"'$video_name'", "video_desc":"'$video_desc'", "video_keyword":"'$video_keyword'", "resource_type":"'$resource_type'", "video_content":"'$video_content'","created_time":"'$created_time'", "name":"'$name'" }}]}' 'http://datareport.dev.ailadui.net/v1/api/report'

done
