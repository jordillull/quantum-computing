test: test-qmath

test-qmath:
	python3 qmath/tests.py --verbose

marble-experiment:
	python3 experiments/marbles.py < experiments/samples/6x6_sample
