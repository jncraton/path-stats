all: test

test:
	python3 -m doctest pathstats.py

clean:
	rm -rf __pycache__
