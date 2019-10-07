RUNTEST=python -m unittest discover -s 'rules/tests' -p 'Test*.py' -v
TEST_DIR=./rules/tests

.PHONY: test

test:
	${RUNTEST} 

