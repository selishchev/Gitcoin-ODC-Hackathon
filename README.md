# Exploratory Data Analysis

<b>Gitcoin_ODC_Hackathon_Analysis.ipynb</b> - The notebook with the Exploratory Data Analysis (it's better to view through <a href="https://nbviewer.org/github/selishchev/Gitcoin-ODC-Hackathon/blob/main/Gitcoin_ODC_Hackathon_Analysis.ipynb">this link</a> because GitHub can't show interactive plots from the "plotly" library)

<b>eth_parser.py</b> - A script for parsing and processing of data for the "eth_stats.csv" dataset

<b>eth_stats.csv</b> - A dataset with the stats of the addresses that donated on the Ethereum chain in GR15. <a href="https://market.oceanprotocol.com/asset/did:op:4cb99c7d3375c86730a951895edbdfed3cc45ac711642b4e1460e7407d675d27">Ocean Protocol link</a>

<b>labeled_eth_stats.csv</b> - The labeled "eth_stats.csv" dataset (1 - potential Sybils, 0 - not marked addresses). <a href="https://market.oceanprotocol.com/asset/did:op:be61c10b47128819b9eb33c994da1f3202542d153f194df1aa4ddd13f60fd612">Ocean Protocol link</a>


<b>main_df_eth.csv</b> - A dataset for the "eth_parser.py" (for using unique addresses from all the donations on the Ethereum chain in GR15) <a href="https://market.oceanprotocol.com/asset/did:op:c42f43298b05d14ba350e61649ab4b1913bf19f6f4cda130b242b8cd850d73e8">Ocean Protocol link</a>

<h2>Challenge Description</h2>

In this challenge, you will analyze any sources you find relevant, likely to include the data sets from the Fantom and Unicef Gitcoin public goods rounds. This bounty in particular rewards innovative exploratory data analysis - including your approach to analysis and the data sets that you select. The goal is to more efficiently find Sybils.

<a href="https://gitcoin.co/issue/29675">Full description of the hackathon section</a>

<h2>Summary of the analysis</h2>

<a href="https://nbviewer.org/github/selishchev/Gitcoin-ODC-Hackathon/blob/main/Gitcoin_ODC_Hackathon_Analysis.ipynb">The notebook with the full analysis</a>

<h3>Insights:</h3>

- 75% of donations are no more than 1.5 usdt with an average of 2.85 usdt, with a maximum donation of 60 000 usdt

- 75% of donations on the Ethereum chain are no more than 2.5 usdt with an average of 7.32 usdt that is more than these stats across all chains

- 50% of the addresses that donated on the Ethereum chain have no more than 2.67 volume in ETH, 352 volume in stablecoins, and 72 transactions

- There may be more suspicious donations on the zkSync chain than on other chains due to the ratio of the number of transactions to the amount of all donations (we can see this on the barplots)

- There are grants to which suspicious addresses donate more, it may make sense, in addition to marking suspicious wallets, to also look at the share of marked donations to a particular grant (sybil donations to a grant). Perhaps the grant may be involved in the fact that many suspicious donations are received by it (to take a bigger share of the total donations because of the quadratic funding)

- Almost all grants with share of marked donation more than 0.2 have less than 100 donations and the donated amount in USDT less than ~800

<h3>Possible solutions to find Sybils:</h3>

- Mark addresses that have less than 0.1 volume in ETH and less than 30 volume in stablecoins and less than 30 transactions as suspicious (but it's just an example, address marking conditions may vary)

- Give less donation weight to marked wallets

- Give less donation weight to suspicious grants with a high share of marked donations

- A note: If the marked wallets are connected with each other (maybe through another address) and donate small amounts to the same grant (and the grant has a high share of marked donations), then these are probably Sybils
