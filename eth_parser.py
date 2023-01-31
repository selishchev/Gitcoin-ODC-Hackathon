import pandas as pd
import requests


def get_address_info(address_list):
    API_key = ''  # insert an API key
    req = requests.get(
        f'https://api.etherscan.io/api?module=account&action=txlist&address={address_list[0]}&startblock=0&endblock=15650000&offset=10&sort=desc&apikey={API_key}')
    req2 = requests.get(
        f'https://api.etherscan.io/api?module=account&action=tokentx&address={address_list[0]}&startblock=0&endblock=15650000&sort=desc&apikey={API_key}')
    normal_txs = pd.json_normalize(pd.read_json(req.text)['result'])
    token_txs = pd.json_normalize(pd.read_json(req2.text)['result'])
    normal_txs['value'] = normal_txs['value'].astype('float64') / 1000000000000000000
    token_txs['value'] = token_txs['value'].astype('float64') / 1000000
    token_txs.loc[token_txs['tokenName'] == 'Dai Stablecoin', 'value'] = \
    token_txs.loc[token_txs['tokenName'] == 'Dai Stablecoin']['value'] / 1000000000000
    tokens = token_txs.groupby('tokenName', as_index=False).value.sum().round()
    summary_df = pd.DataFrame({'address': [f'{address_list[0]}'],
                               'eth_volume': [normal_txs.value.sum()],
                               'stablecoins_volume': [tokens.loc[(tokens['tokenName'] == 'USD Coin') | (
                                           tokens['tokenName'] == 'Tether USD') | (
                                                                             tokens['tokenName'] == 'Dai Stablecoin')][
                                                          'value'].sum()],
                               'num_of_txs': [normal_txs.shape[0] + token_txs.shape[0]]
                               })
    address_list.pop(0)
    with open('eth_stats.csv', 'a') as f:
        f.write(summary_df.to_csv(index=False))
    for address in address_list:
        req = requests.get(
            f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=15650000&offset=10&sort=desc&apikey={API_key}')
        req2 = requests.get(
            f'https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=15650000&sort=desc&apikey={API_key}')
        normal_txs1 = pd.json_normalize(pd.read_json(req.text)['result'])
        token_txs1 = pd.json_normalize(pd.read_json(req2.text)['result'])
        normal_txs1['value'] = normal_txs1['value'].astype('float64') / 1000000000000000000
        try:
            token_txs1['value'] = token_txs1['value'].astype('float64') / 1000000
            token_txs1.loc[token_txs1['tokenName'] == 'Dai Stablecoin', 'value'] = \
            token_txs1.loc[token_txs1['tokenName'] == 'Dai Stablecoin']['value'] / 1000000000000
            tokens1 = token_txs1.groupby('tokenName', as_index=False).value.sum().round()
        except(KeyError):
            token_txs1['value'] = 0
            tokens1['value'] = 0
        summary_df1 = pd.DataFrame({'address': [f'{address}'],
                                    'eth_volume': [normal_txs1.value.sum()],
                                    'stablecoins_volume': [tokens1.loc[(tokens1['tokenName'] == 'USD Coin') | (
                                                tokens1['tokenName'] == 'Tether USD') | (tokens1[
                                                                                             'tokenName'] == 'Dai Stablecoin')][
                                                               'value'].sum()],
                                    'num_of_txs': [normal_txs1.shape[0] + token_txs1.shape[0]]
                                    })
        with open('eth_stats.csv', 'a') as f:
            f.write(summary_df1.to_csv(index=False, header=False))


get_address_info(list(pd.read_csv('main_df_eth.csv')['address'].unique()))
