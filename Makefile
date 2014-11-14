all:

test: test-complex test-operations

test-complex:
	python3 qmath/tests/complex_tests.py --verbose

test-operations:
	python3 qmath/tests/operations_tests.py --verbose

marble-experiment:
	python3 experiments/marbles.py < experiments/samples/6x6_sample

qstate-experiments: qstate-experiment0 qstate-experiment1 qstate-experiment2

qstate-experiment0:
	python3 experiments/quantum_state.py < experiments/samples/qstate_0.txt

qstate-experiment1:
	python3 experiments/quantum_state.py < experiments/samples/qstate_1.txt

qstate-experiment2:
	python3 experiments/quantum_state.py < experiments/samples/qstate_2.txt
