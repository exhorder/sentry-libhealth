test:
	@py.test --tb=short tests -vv

lint:
	@flake8 libtervis

.PHONY: test lint
