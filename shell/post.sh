#!/bin/bash

resources="/data/home/hyw/data/resources.csv"
watch_record="/data/home/hyw/data/watch_record.csv" 

# 这里的-x 参数判断$myPath是否存在并且是否具有可执行权限 
if [ ! -x "$filePath"]; then 
echo "no such dir"
fi 

cd $filePath

# 这里的-f参数判断$myFile是否存在 
if [ ! -f "$resources" ]; then 
echo "resources not exist" 
fi 


#逐行读取文本
cat $resources | while read line
do
    echo "File:${line}"
    #awk 读取
    item_id = awk -F ';' '{printf($1,)}'  ${line}
    echo "----"
done


i=1
for ID in $(cat $resources | wc -l)
do 
    NUM=$i
    S_ID=$(awk 'NR=="$SUM" {printf $1}' $resources)
    T_NUM=$(awk 'NR="$SUM" {printf $2}' $resources)
    echo $S_ID
    echo $T_NUM
    : $((i++))
done

# 逐行读取文本
#cat $resources | while read line
#do
#    echo ${file} | awk -F ';' '{printf($0)}' 
#    awk '-F ";" "NR=1" {print($0)}' $resources
#    echo "----"
#done
row=$(cat $resources | wc -l)
#for line in $(seq 1 $row)
for line in 7
do
    echo $line
    #可能出现的问题 字段中有分号 结果格式会乱掉
    video_id=$(awk -F ";" "NR==$line"'{print$1}' $resources |sed 's/\"//g')
    course_type=$(awk -F ";" "NR==$line"'{print$2}' $resources |sed 's/\"//g')
    seqc=$(awk -F ";" "NR==$line"'{print$3}' $resources |sed 's/\"//g')
    grade=$(awk -F ";" "NR==$line"'{print$4}' $resources |sed 's/\"//g')
    section=$(awk -F ";" "NR==$line"'{print$5}' $resources |sed 's/\"//g') 	
    subject1=$(awk -F ";" "NR==$line"'{print$7}' $resources |sed 's/\"//g')	
    subject2=$(awk -F ";" "NR==$line"'{print$8}' $resources |sed 's/\"//g')	
    subject3=$(awk -F ";" "NR==$line"'{print$9}' $resources |sed 's/\"//g')	
    video_name=$(awk -F ";" "NR==$line"'{print$10}' $resources |sed 's/\"//g')	
    video_desc=$(awk -F ";" "NR==$line"'{print$11}' $resources |sed 's/\"//g')	
    video_keyword=$(awk -F ";" "NR==$line"'{print$12}' $resources |sed 's/\"//g')	
    resource_type=$(awk -F ";" "NR==$line"'{print$13}' $resources |sed 's/\"//g')	
    create_time=$(awk -F ";" "NR==$line"'{print$17}' $resources |sed 's/\"//g')	
    video_content=$(awk -F ";" "NR==$line"'{print$20}' $resources |sed 's/\"//g')	
    name=$(awk -F ";" "NR==$line"'{print$21}' $resources |sed 's/\"//g')

 		video_id = `echo $line | awk -F ';' '{print $1}'`
 		course_type = `echo $line | awk -F ';' '{print $2}'`
 		seqc = `echo $line | awk -F ';' '{print $3}'`
 		grade = `echo $line | awk -F ';' '{print $4}'`
 		section = `echo $line | awk -F ';' '{print $5}'`
 		subject1 = `echo $line | awk -F ';' '{print $7}'`
 		subject2 = `echo $line | awk -F ';' '{print $8}'`
 		subject3 = `echo $line | awk -F ';' '{print $9}'`
 		video_name = `echo $line | awk -F ';' '{print $10}'`
 		video_desc = `echo $line | awk -F ';' '{print $11}'`
 		video_keyword = `echo $line | awk -F ';' '{print $12}'`
 		resource_type = `echo $line | awk -F ';' '{print $13}'`
 		create_time = `echo $line | awk -F ';' '{print $17}'`
 		video_content = `echo $line | awk -F ';' '{print $20}'`
 		name = `echo $line | awk -F ';' '{print $21}'`

 		
 		echo "$n1 $n2";

    #curl post
    echo '{"video_id": "'$video_id'", "cource_type":"'$cource_type'", "seqc":"'$seqc'","grade": "'$grade'", "section": "'$section'", "subject1":"'$subject1'", "subject2":"'$subject2'", "subject3":"'$subject3'", "video_name":"'$video_name'", "video_desc":"'$video_desc'", "video_keyword":"'$video_keyword'", "resource_type":"'$resource_type'", "video_content":"'$video_content'","created_time":"'$created_time'", "name":"'$name'" }'
 #   curl -i -X POST -H "Content-Type: application/json" -d '{"robot_id":"22e3f139-8592-11e7-ba8b-7cd30ab71dd0", "table_name" : "educate_item",  "table_content": [{"cmd":"add", "fields": {"video_id": "'$video_id'", "cource_type":"'$cource_type'", "seqc":"'$seqc'","grade": "'$grade'", "section": "'$section'", "subject1":"'$subject1'", "subject2":"'$subject2'", "subject3":"'$subject3'", "video_name":"'$video_name'", "video_desc":"'$video_desc'", "video_keyword":"'$video_keyword'", "resource_type":"'$resource_type'", "video_content":"'$video_content'","created_time":"'$created_time'", "name":"'$name'" }}]}' 'http://datareport.dev.ailadui.net/v1/api/report'
done


awk -F ";" "NR==18"'{print$1}' $resources

video_id=$(awk -F ";" "NR==$line"'{print$1}' $resources |sed 's/\"//g')
course_type=$(awk -F ";" "NR==$line"'{print$2}' $resources)
seqc=$(awk -F ";" "NR==$line"'{print$3}' $resources)
grade=$(awk -F ";" "NR==$line"'{print$4}' $resources)
section=$(awk -F ";" "NR==$line"'{print$5}' $resources)	
subject1=$(awk -F ";" "NR==$line"'{print$7}' $resources)	
subject2=$(awk -F ";" "NR==$line"'{print$8}' $resources)	
subject3=$(awk -F ";" "NR==$line"'{print$9}' $resources)	
video_name=$(awk -F ";" "NR==$line"'{print$10}' $resources)	
video_desc=$(awk -F ";" "NR==$line"'{print$11}' $resources)	
video_keyword=$(awk -F ";" "NR==$line"'{print$12}' $resources)	
resource_type=$(awk -F ";" "NR==$line"'{print$13}' $resources)		
create_time=$(awk -F ";" "NR==$line"'{print$17}' $resources)	
video_content=$(awk -F ";" "NR==$line"'{print$20}' $resources)	
name=$(awk -F ";" "NR==$line"'{print$21}' $resources)


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

#curl post
curl -i -X POST -H "Content-Type: application/json" -d '{"robot_id":"22e3f139-8592-11e7-ba8b-7cd30ab71dd0", "table_name" : "educate_item",  "table_content": [{"cmd":"add", "fields": {"video_id": "'"$video_id"'", "cource_type":"'"$cource_type"'", "seqc":"'"$seqc"'","grade": "'"$grade"'", "Section": "'"$Section"'", "subject1":"'"$subject1"'", "subject2":"'"$subject2"'", "subject3":"'"$subject3"'", "video_name":"'"$video_name"'", "video_desc":"'"$video_desc"'", "video_keyword":"'"$video_keyword"'", "resource_type":"'"$resource_type"'", "video_content":"'"$video_content"'","created_time":"'"$created_time"'", "name":"'"$name"'", }}]}' 'http://datareport.dev.ailadui.net/v1/api/report'

curl -i -X POST -H "Content-Type: application/json" -d '{"robot_id":"22e3f139-8592-11e7-ba8b-7cd30ab71dd0", "table_name" : "educate_item", "table_content": [{"cmd":"add", "fields": {"video_id": "1", "cource_type": "1", "seq":"2","grade": "2", "Section": "0","subject1":"物质科学", "subject2":"物质的特征", "subject3":"物质的外观描述（颜色、形状、外观、质量、体积、温度等特征描述）", "video_name":"Unit5 My day Lesson2", "video_desc":"不规则物体可以通过物体排出水的体积来计算不规则物体的体积1", "video_keyword":"物质-科学", "resource_type":"3", "video_content":"Lesson 1 Li Ming Comes Home|Welcome back. I missed you.|Thank you, Bill. I missed you, too.|Did you have a good trip?|Yes! We had a great trip!|Where did you go?|We went to Beijing. It’s the capital of China.|What did you do there?|We visited many interesting places. I would tell you a story about Chinese year.|Great! How about yesterday?|We walked to Wangfujing Street and shopped here last night. Look! A gift is for you.|Thank you.", "created_time":"2017-08-01 17:22:55","name":"如何测量不规则物体的体积1"}}]}' 'http://datareport.dev.ailadui.net/v1/api/report'

curl -i -X POST -H "Content-Type: application/json" -d '{"robot_id":"22e3f139-8592-11e7-ba8b-7cd30ab71dd0", "table_name" : "user_action", "table_content": [{"cmd":"add", "fields": {"user_id": "1111","item_id": "6033654", "item_type": 1,"action_type": "play","created_time": 1503714136}}]}' 'http://datareport.dev.ailadui.net/v1/api/report'




awk -F ";" "NR==2"'{print$18}' $resources |sed 's/\"//g'
resources="/data/home/hyw/data/resources.csv"

{"video_id": "6", "cource_type":"", "seqc":"6","grade": "6", "section": "0", "subject1":"物质科学", "subject2":"物质的特征", "subject3":"物质的外观描述（颜色、形状、外观、质量、体积、温度等特征描述）", "video_name":"Unit6 Jobs Lesson2", "video_desc":"空气和水都是无色透明的，都具有流动性，但空气看不见摸不着，水看得见，摸得到，水比空气重。", "video_keyword":"", "resource_type":"3", "video_content":"z0.598042e445a2650c996c3b1c","created_time":"", "name":"http://7xkpsq.com2.z0.glb.qiniucdn.com/1501664338387" }



1:A 2:B 3:C 4:D 5:E 6:F 7:G 8:H 9:I 10:J 11:K 12:L 13:M 14:N 15:O 
16:P 17:Q 18:R 19:S 20:T 21:U 22:V 23:W 24:X 25:Y 26:Z
