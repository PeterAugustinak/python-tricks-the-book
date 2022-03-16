"""8.1 Exploring Python Modules and Objects"""


import datetime
inspect_datetime = dir(datetime)
print(inspect_datetime)

inspect_datetime_date = dir(datetime.date)
print(inspect_datetime_date)

# inspect only specific attrs
only_date_related = [_ for _ in dir(datetime) if 'date' in _.lower()]
print(only_date_related)

# inspect only public
only_public = [_ for _ in dir(datetime) if not (_.startswith('_')
                                                or _.startswith('__'))]
print(only_public)

# check help
# helper = help(datetime)
# print(helper)

specific_helper = help(datetime.date.fromtimestamp)
print(specific_helper)

# print(help(dir))
