from processing import filter_operations, sort_operations_by_date

# Example data of bank operations
transaction_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Example usage of functions
filtered_transactions = filter_operations(transaction_list, status='EXECUTED')
sorted_transactions = sort_operations_by_date(filtered_transactions)

print("Filtered Operations:", filtered_transactions)
print("Sorted Operations:", sorted_transactions)
