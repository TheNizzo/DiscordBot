import pandas as pd
import requests
import lxml.html as lh



def get_world():
    page = requests.get("https://www.worldometers.info/coronavirus/#countries")
    doc = lh.fromstring(page.content)
    world_cases = doc.xpath('//span[@style="color:#aaa"]/text()')
    world_deaths = doc.xpath('//span[@class="number-table"]/text()')
    res = []
    res.append(world_cases[0].strip())
    deaths = world_deaths[3].strip().rstrip()
    recovered = world_deaths[2]
    res.append(deaths)
    res.append(recovered)
    return res

def get_dataframe():
    page = requests.get("https://www.worldometers.info/coronavirus/#countries")
    doc = lh.fromstring(page.content)

    
    tr_elements = doc.xpath('//tr')


    col = []
    i = 0
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        col.append((name, []))

    for j in range(1, 197):
        T = tr_elements[j]

        if len(T) != 11:
            break

        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:
                try:
                    data = int(data)
                except:
                    pass
            col[i][1].append(data)
            i+=1

    Dict = {title:column for (title, column) in col}
    df = pd.DataFrame(Dict)
    return df


def get_top():
    df = get_dataframe().head(10)
    res = []
    df['TotalCases'] = df['TotalCases'].str.replace(",", "")
    df['TotalCases'] = df['TotalCases'].astype(int) 
    df = df.sort_values(by=['TotalCases'], ascending=False)
    for index, row in df.iterrows():
        res.append((row['Country,Other'], "{:,}".format(row['TotalCases'])))
    return res

def get_lebanon(country):
    df = get_dataframe()
    if country == 'Usa':
        country = 'USA'
    try:
        corona_country = df[df['Country,Other'].str.contains(country)]
    except:
        return False
    res = [country]
    if corona_country['TotalCases'].values[0] == "":
        res.append("No cases")
    else:
        res.append(corona_country['TotalCases'].values[0])
    if corona_country['NewCases'].values[0] == "":
        res.append("No new cases")
    else:
        res.append(corona_country['NewCases'].values[0])
    if str(corona_country['TotalDeaths'].values[0]).strip() == "" or corona_country['TotalDeaths'].values[0] == " ":
        res.append("0")
    else:
        res.append(str(corona_country['TotalDeaths'].values[0]).strip())
    if corona_country['NewDeaths'].values[0] == "":
        res.append("No new deaths")
    else:
        res.append(corona_country['NewDeaths'].values[0])
    if corona_country['TotalRecovered'].values[0] == "":
        res.append("0")
    else:
        res.append(corona_country['TotalRecovered'].values[0])
    return res


get_dataframe()