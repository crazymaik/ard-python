
.PHONY: run
run:
	python3 -m ard.main

.PHONY: test
test:
	pytest tests

.PHONY: clean
clean:
	python3 setup.py clean
	rm -rf ard.egg-info dist .cache
	find . -iname \*.pyc -delete
	find . -iname __pycache__ -delete

