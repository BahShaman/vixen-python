#DISPLAY=0:0; sudo python ./VixenViewerC.py
 DISPLAY=0:0; sudo python $1 2>$0.error.log
cat $0.error.log 
