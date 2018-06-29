# NELL-MDCOINS 

NellMDCoins is the worlds first crypto-currency with "Reversible Transactions". NellMDCoins proof-of-concept is based on Bitcoinpy. Final version of NellMDCoins will be based on Bitcoin code, using Proof-of-Stake (PoS) for mining.

With NellMDCoins, you can create two different kinds of accounts: Standard Accounts and Vault Accounts. Standard accounts behave very much like your Bitcoin accounts and allow you to send and receive money for daily purposes. Vault accounts behave much like you bank savings account, where you can deposit large amount of coins and keep them safe from hackers. Each vault account has a configurable timeout and is backed by two key pairs, one online and one offline. You only need online keypair to transfer coins from vault. When you transfer your coins using online keypair, your transactions get confirmed after they live in blockchain for the timeout period.

If someone steals your online key pair and transfers coins to them, the transactions will have to wait in block chain for the timeout period. During which, you can use your offline key pair and reverse those transactions and restore your coins to your other address. You can also use your offline key pair for immediate transfer of coins in your Vault, instead of waiting for timeout period. In a sentence, Vault account has the ease of use of hot wallets (online account) and security of cold wallets (offline accounts). We are also working on a monitoring service, to send you real-time alerts, when your coins are transferred from your addresses. To know more about NellMDCoins, read our white paper or even better play with the vaultcoin, to see for yourself how NellMDCoins works. In order to make it easy, the code is sandboxed and difficulty is reduced so that blocks are produced one every minute. Below is a brief tutorial to show how vaultcoin works.

In order to keep the code lightweight we built NellMDCoins based on Bitcoinpy and reused the libraries including the Bitcoinlib by Jeff Garzik and others. Code contains all the components including the NellMDCoins server, client, wallet and miner. We will add support for missing functionality, albeit slowly. If you would like to contribute, please feel free to fork the project, hack it and send a pull request. We will gladly accept your changes. Any contributions including documentation are welcome.

### Motivation
Cryptocurrencies and smart-contracts on top of a blockchain aren't the most trivial concepts to understand,things like wallets, addresses, block proof-of-work, transactions and their signatures, make more sense when they are in a broad context. Inspired by [naivechain](https://github.com/lhartikk/naivechain) and [jeff Garzik](https://github.com/jgarzik/pynode) by, which
is inturn based on [ArtForz' public domain half-a-node](http://pastebin.com/ZSM7iHZw), this project is an attempt to provide as concise and simple cryptocurrency for the blockchain and AI research. More than that, anyone could also use these coins to buy the NELL services or products and reference it to understand the core workings of bitcoin and debug new altcoins

### What is cryptocurrency
[From Wikipedia](https://en.wikipedia.org/wiki/Cryptocurrency) : A cryptocurrency (or crypto currency) is a digital asset designed to work as a medium of exchange using cryptography to secure the transactions and to control the creation of additional units of the currency.

### Key concepts of Nell-MDCoins
* Components
    * HTTP Server
    * Node
    * Blockchain
    * Operator
    * Miner
* HTTP API interface to control everything
* Synchronization of blockchain and transactions
* Simple proof-of-work (The difficulty increases every 5 blocks)
* Addresses creation using a deterministic approach [EdDSA](https://en.wikipedia.org/wiki/EdDSA)
* Data is persisted to a folder

> NELL-MDCOIN uses websocket for p2p communication, but it was dropped to simplify the understanding of message exchange. It is relying only on REST communication.


### Contribution and License Agreement

If this implementation does something wrong, please feel free to contribute by opening an issue or sending a PR. The main goal of this project is to create a full-featured cryptocurrency for research fundings and educational purposes. Also , this project aims to use this cryptocurrency as the mai currency for exhchange of NELL services and products.

In order to keep the code lightweight we reused the libraries including the Bitcoinlib by Jeff Garzik and others. Code contains all the components including the full bitcoin client, server, wallet and miner. However, some of the components like P2SH, alert messages and more are missing. We will add support for missing functionality, albeit slowly. if you would like to contrinute, please feel free to fork the project, hack it and send a pull request. We will gladly accept your changes. Any contributions including documentation are welcome.

There is also a __todo.md__ file , which states the features and other help needed. Make sure , you go through the docs.
