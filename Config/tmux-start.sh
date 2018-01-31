#!/bin/sh                                              
#                                                      
                                                       
cmd=$(which tmux) # tmux path                          
session=h1   # session name                            
                                                       
if [ -z $cmd ]; then                                   
  echo "You need to install tmux."                     
  exit 1                                               
fi                                                     
                                                       
$cmd has -t $session                                   
                                                       
if [ $? != 0 ]; then                                   
  $cmd new -d -n n1 -s $session                        
  $cmd splitw -v -p 20 -t $session                     
  $cmd select-pane -U                                  
  $cmd splitw -h -p 50 -t $session                     
  $cmd neww -n n2 -t $session                          
  $cmd splitw -h -p 50 -t $session                     
  $cmd splitw -v -p 50 -t $session                     
  $cmd selectw -t $session:n2                          
fi                                                     
                                                       
$cmd att -t $session                                   
                                                       
exit 0                                                 
