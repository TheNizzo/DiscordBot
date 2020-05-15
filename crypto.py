import pandas as pd
import lxml.html as lh
import requests

def get_crypto_dataframe():
    page = requests.get("https://coinmarketcap.com/")
    doc = lh.fromstring(page.content)

    tr_elements = doc.xpath('//tr')

    col = []
    i = 0
    for t in tr_elements[0][:-1]:
        i += 1
        name = t.text_content()
        print(name)
        col.append((name, []))

    for j in range(1, 50):
        T = tr_elements[j][:-1]

        if len(T) != 8:
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


