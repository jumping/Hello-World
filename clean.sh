#!/bin/bash
TYPE="collatelog filterFraud"
thisday=`date +%Y%m%d`

for  tp in $TYPE;do
  echo "clean $tp..."

  for d in `find ./  -type d -name $tp -a -not -path "*${thisday}*"`;do
    echo $d && tar czf $d.tgz $d && rm -rf $d
  done

done
