all:
	python nellCoin.py config.cfg

test:
	python test.py

tmp:
	python tmp.py

clean:
	rm -rf ~/.nellCoin

new:
	rm -rf ~/.nellCoin/*
	mkdir -p ~/.nellCoin/leveldb
	cp genesis.dat ~/.nellCoin/blocks.dat
	python nellCoin.py config.cfg

install:
	sudo apt-get install python-gevent libleveldb1 python-leveldb python-bsddb3 
