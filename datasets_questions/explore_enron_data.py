#!/usr/bin/python3

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

import joblib

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

#Features
# ['salary', 
# 'to_messages', 
# 'deferral_payments', 
# 'total_payments', 
# 'loan_advances', 
# 'bonus', 
# 'email_address', 
# 'restricted_stock_deferred', 
# 'deferred_income', 
# 'total_stock_value', 
# 'expenses', 
# 'from_poi_to_this_person', 
# 'exercised_stock_options', 
# 'from_messages', 
# 'other', 
# 'from_this_person_to_poi', 
# 'poi', 
# 'long_term_incentive', 
# 'shared_receipt_with_poi', 
# 'restricted_stock', 
# 'director_fees']


#Lesson 6 [14]
# ans = len(enron_data.values())
# print(ans)

#Lesson 6 [15]
# ans = len(enron_data['METTS MARK'].values())
# print(ans)

#Lesson 6 [16]
# ans = sum(d['poi'] == 1 for d in enron_data.values() if d)
# print(ans)

#Lesson 6 [18]
# ans =tuple(key for key, value in enron_data.items() if 'prentice' in key.lower())
# ans = enron_data["PRENTICE JAMES"]['total_stock_value']
# print(ans)

#Lesson 6 [19]
# ans = enron_data["Colwell Wesley".upper()]['from_this_person_to_poi']
# print(ans)

#Lesson 6 [20]
# ans = enron_data['Skilling Jeffrey K'.upper()]['exercised_stock_options']
# print(ans)

#Lesson 6 [25]
# d = {1: enron_data['SKILLING JEFFREY K']['total_payments'],
# 2: enron_data['LAY KENNETH L']['total_payments'],
# 3: enron_data['FASTOW ANDREW S']['total_payments']}
# key = max(d, key = lambda k: d[k])
# print(key, d[key])

#Lesson 6 [27-A]
# ans = (d['salary'] for d in enron_data.values() if d)
# ans = [x for x in ans if not isinstance(x, str)]

#Lesson 6 [27-B]
# ans = (d['email_address'] for d in enron_data.values() if d)
# ans = [x for x in ans if x != 'NaN']
# ans = len(ans)
# print(ans)

#Lesson 6 [29]
# ans = (d['total_payments'] for d in enron_data.values() if d)
# ans = [x for x in ans if x == 'NaN']
# # ans = ( len(ans) / len(enron_data) ) * 100
# print(len(ans))

#Lesson 6 [30]
# ans = (d for d in enron_data.values() if (d['poi'] == 1 and d['total_payments'] == 'NaN') )
# print(len(list(ans)))




# print(len(enron_data.values()))

