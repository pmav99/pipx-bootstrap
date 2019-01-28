.PHONY: build publish

build:
	python3 -m pip install --upgrade --quiet setuptools wheel twine
	python3 setup.py --quiet sdist bdist_wheel

publish:
	python3 -m twine upload dist/*

clean:
	rm -r build dist
