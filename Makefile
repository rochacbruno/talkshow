.PHONY: test install pep8 clean

test: pep8
	py.test  -v --cov-config .coveragerc --cov=talkshow -l --tb=short --maxfail=1 tests/

install:
	pip install --upgrade pip
	pip install -e .[dev] --upgrade --no-cache
	flask adduser -u admin -p 1234

pep8:
	# Flake8 ignores 
	#   F841 (local variable assigned but never used, useful for debugging on exception)
	#   W504 (line break after binary operator, I prefer to put `and|or` at the end)
	#   F403 (star import `from foo import *` often used in __init__ files)
	@flake8 talkshow --ignore=F403,W504,F841
	@flake8 tests --ignore=F403,W504,F841

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .[dev] --upgrade --no-cache
