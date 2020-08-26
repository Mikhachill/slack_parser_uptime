i = 0
col = ['alert', 'time', 'date']
df = pd.DataFrame(columns=col)
for i in range(len(data)):
    df.loc[i, 'alert'] = data.loc[i, 'alert']
    i += 1
print(i)

i = 0
for tag in soup.select(".c-timestamp__label"):
    df.loc[i, 'time'] = tag.text
    i += 1
print(i)

i = 0
for i in range(len(data)):
    df.loc[i, 'date'] = data.loc[i, 'date']
    i += 1
print(i)
