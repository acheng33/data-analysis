# data-analysis
CS 125 Course Development

## Setup
In order to set up your environment properly, you will need a `.env` file which should include any environment variables that will need to be used in the files of code. 
Ensure that `pymongo` and `json` have been downloaded locally before trying to run to ensure correct results. 

## File Descriptions
#### PrintJson.py
Prints the document structure of the first document in each collection within a given database into a text file. Each collection name is untabbed with the first layer of the document structure having one tab and each subsequent layer using more tabs. There is a line of white space between collections for identification and ease of reading. For example:
`
collection name
    first object
        values within the object
    second object

second collection
`
To run, run `python3 PrintJson.py`. 