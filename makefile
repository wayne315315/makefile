all: config.json clean

config.json: build.sh
	bash build.sh

build.sh: setup.py
	python3 setup.py

clean: 
	rm build.sh
	@echo 'All clean'