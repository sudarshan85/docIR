PEP_IGNORE_ERRORS=C901 E501 W503 E203 E231 E266 F403

install: FORCE ## Install docIR package
	pip install -e .

clean: FORCE ## Uninstall docIR package and cleanup
	pip uninstall -y docIR
	find . -name "__pycache__" -exec rm -rf {} +
	rm -rf build dist docIR.egg-info

.PHONY: help

.DEFAULT_GOAL := install

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n]", $$1, $$2}'

FORCE:
