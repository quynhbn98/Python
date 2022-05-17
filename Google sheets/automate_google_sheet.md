## I. Task overview:
... based on a true story... I mean task

#### 1. Objective: 
measure an NLP model's performance (with each product name, suggest which category it belongs, eg: 'Black mini skirt' belongs to 'Skirt')

#### 2. Team involved:
- NLP engineer: take data input from DA team, train model, give an api as an output
- Data entry team: verify if suggestion from the model is right or not
- Data analyst team: prepare data input for 2 above teams, do statistics for report of model performance, add new categories if neccessary
- Product team: intergrate api for category suggestion feature

## II. Steps:
- Get data of products from server
- Call suggestion api for each product  
- Write suggest data into a google sheet for data entry team to verify if suggestion is right or not
- Do statistics for report of model performance
- Summerize data after verification, input back in the model as data input

## III. Skills:
- Python 
- Open connection, get data from server 
- Call api and format data 
- Use google sheet api (code in this folder)
- Google sheets functions to automate report, assign data for each data entry member (sheet design and function updating)

## IV. Fun facts:
- Google server usually has trouble at around 2p.m...