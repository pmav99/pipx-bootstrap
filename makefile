.PHONY: build publish

build:
	python -m pip install --upgrade --quiet setuptools wheel twine
	python setup.py --quiet sdist bdist_wheel

publish:
	python -m twine upload dist/*

clean:
	rm -r build dist
