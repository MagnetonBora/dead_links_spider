#!/bin/bash

if [[ -z $1 ]] 
then
   result_file='results.json'
else
   result_file=$1
fi

scrapy crawl dead-links-spider -o $result_file
