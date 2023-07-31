import requests
from datetime import datetime
import pandas as pd


def get_session():
    session = requests.Session()
    url = 'http://banggia.shs.com.vn/f/df.asmx/do'
    payload = {'a': 'v', 'p': []}
    resp = session.post(url=url, json=payload)
    if not resp.ok:
        raise Exception(resp.text)
    return session


def parse_timestep_data(data):
    r = {}
    fs = data.split('|')
    fI = 0
    p = None
    v = None
    for it in fs:
        p = it.split('^')
        if len(p) == 2:
            v = p[1]
            fI = int(p[0])
        else:
            v = p[0]
        if fI == 0:
            r['TotalVolumeTraded'] = int(v)
        elif fI == 1:
            r['TotalValueTraded'] = int(v)
        elif fI == 2:
            r['LastMatchedPrice'] = int(v)
        elif fI == 3:
            r['LastMatchedVolume'] = int(v)
        elif fI == 4:
            r['BestBidPrice1'] = int(v)
        elif fI == 5:
            r['BestBidVolume1'] = int(v)
        elif fI == 6:
            r['BestBidPrice2'] = int(v)
        elif fI == 7:
            r['BestBidVolume2'] = int(v)
        elif fI == 8:
            r['BestBidPrice3'] = int(v)
        elif fI == 9:
            r['BestBidVolume3'] = int(v)
        elif fI == 10:
            r['BestAskPrice1'] = int(v)
        elif fI == 11:
            r['BestAskVolume1'] = int(v)
        elif fI == 12:
            r['BestAskPrice2'] = int(v)
        elif fI == 13:
            r['BestAskVolume2'] = int(v)
        elif fI == 14:
            r['BestAskPrice3'] = int(v)
        elif fI == 15:
            r['BestAskVolume3'] = int(v)
        elif fI == 16:
            r['HighPrice'] = int(v)
        elif fI == 17:
            r['LowPrice'] = int(v)
        elif fI == 18:
            r['OpenPrice'] = int(v)
        elif fI == 19:
            r['ForeignBuy'] = int(v)
        elif fI == 20:
            r['ForeignSell'] = int(v)
        elif fI == 21:
            r['TotalAskVolume'] = int(v)
        elif fI == 22:
            r['TotalBidVolume'] = int(v)
        elif fI == 23:
            r['TradingTime'] = v
        elif fI == 24:
            r['PtVolume'] = int(v)
        elif fI == 25:
            r['PtValue'] = int(v)
        elif fI == 26:
            r['CurrentRoom'] = int(v)
        elif fI == 27:
            r['OpenInterest'] = int(v)
        fI += 1
    return r


def get_hist(symbol, date=None):
    url = 'http://banggia.shs.com.vn/f/df.asmx/do'
    symbol = symbol.strip().upper()
    if not date:
        date = datetime.today().strftime('%Y%m%d')
    session = get_session()
    page = 0
    time_series = []
    while True:
        payload = {'a': 'h', 'p': [symbol, date, page]}
        resp = session.post(url, json=payload)
        page_data = resp.json()['d'][0]
        if page_data == '':
            break
        else:
            for timestep in page_data.split('#'):
                time_series.append(parse_timestep_data(timestep))
            page += 1
    df = pd.DataFrame(time_series)
    df = df.fillna(method='ffill')
    return df
