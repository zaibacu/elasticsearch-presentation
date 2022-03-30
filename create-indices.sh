#!/bin/bash

curl -X PUT "localhost:9200/cars" -H 'Content-Type: application/json' -d'
{
    "settings": {

    },
    "mappings": {
          "properties": {
            "make": {
              "type": "keyword"
            },
            "model": {
              "type": "keyword"
            },
            "part": {
              "type": "text"
            },
            "total_paid": {
              "type": "float"
            }
          }
      }
}
'
