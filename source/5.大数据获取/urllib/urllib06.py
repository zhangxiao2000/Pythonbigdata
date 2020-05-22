from urllib.parse import parse_qs
query = "school=nwpu && loc = shanxi"
print(parse_qs(query))     ## {'school': ['nwpu '], ' loc ': [' shanxi']}
