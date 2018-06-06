#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

from pprint import pprint
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

countSalary = 0
countEmail = 0
countPOI = 0
countTPPOI = 0
count = 0
for intex,person in enron_data.iteritems():
	print intex
#	if enron_data[person]["salary"] != 'NaN':
#		countSalary = countSalary+1
#	if enron_data[person]["email_address"] != 'NaN':
#		countEmail = countEmail+1
#	if enron_data[person]["poi"] == True:
#		if enron_data[person]["total_payments"] == 'NaN':
#			countTPPOI = countTPPOI+1
#		countPOI = countPOI+1
#	count = count+1
#print countTPPOI
#print countPOI
#print count
#print (countTPPOI*100)/countPOI

#print countSalary
#print countEmail
#print count

#pprint(enron_data)

#data = len(open("../final_project/poi_names.txt").readlines())
#print data + count
#print(len(open("../final_project/poi_names.txt").readlines()))
#pprint(enron_data["PRENTICE JAMES"])
#pprint(enron_data["COLWELL WESLEY"])
#list = [enron_data["SKILLING JEFFREY K"]["total_payments"],enron_data["LAY KENNETH"]["total_payments"]]
#pprint(list)
#pprint(enron_data["LAY KENNETH LEE"])
