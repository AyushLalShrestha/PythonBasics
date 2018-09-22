
import re

str = "chart count() device_name"
pattern = r'\w+'
keywords = re.findall(pattern, str)

list_of_queries = [
    "chart count() by device_name, chart count device_name",
    "device_name = \"Ayush\" ",
    "time chart count(log_ts) by something device_name",
    "chart count() device_name"
]

# pattern = r'(.*)?'.join(keywords)
pattern = r'count(.*)?'
print("pattern is as %s " %pattern)

matched_queries = []
for query in list_of_queries:
    result = re.search(pattern, query)
    if result:
        # print result.groups()
        print query

    # result_2 = re.findall(pattern, query)
    # if result_2:
    #     print result_2




