import pandas as pd 
import requests
import lxml.html as lh
import matplotlib.pyplot as plt


def get_dataframe():
    page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Lebanon")
    doc = lh.fromstring(page.content)

    timeline = doc.xpath('//table[@class="wikitable"]')
    name = timeline[0].text_content().split("\n\n")
    # name = timeline.text_content().split("\n\n")
    #print(name)
    name = [ s.split('\n') for s in name]
    name = name[:-1]
    #print(name)
    cases_col = []
    deaths_col = []
    recoveries_col = []
    dates_col = []
    i = 0
    for l in name:
        if 'Date' in l:
            break
        i+=1
    i+=1
    while 'Cases' not in name[i]:
        dates_col.append(name[i][0])
        i += 1
    i += 1
    while 'Deaths' not in name[i]:
        cases_col.append(name[i])
        i += 1
    cases_col = [e for e in cases_col[0]]
    i += 1
    while 'Recoveries' not in name[i]:
        deaths_col.append(name[i])
        i += 1
    deaths_col = [ e for e in deaths_col[0]]
    i += 1
    for e in name[i]:
        recoveries_col.append(e)
        i += 1
    array = [dates_col, cases_col, deaths_col, recoveries_col]
    tmp = pd.DataFrame(array, index=['Date', 'Case', 'Death', 'Recovery'])
    df = tmp.T
    df['Case'] = df['Case'].astype(int)
    df['Death'] = df['Death'].astype(int)
    df['Recovery'] = df['Recovery'].astype(int)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def get_graph():
    df = get_dataframe()
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Case"], label='Confirmed', linewidth=5)
    ax.plot(df["Date"], df["Death"], label='Deaths', linewidth=5)
    ax.plot(df["Date"], df["Recovery"], label='Recovered', linewidth=5)
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed Cases')
    ax.set_title('Confirmed Covid-19 cases in Lebanon')
    #fig.autofmt_xdate()
    #ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    fig.set_size_inches(18.5, 10.5)
    ax.legend()
    plt.tight_layout()
    plt.savefig('hello_there.png')
