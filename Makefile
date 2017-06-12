.PHONY: clean dist-clean all test virtualenv install install-test

PROJECT_NAME=probtextgen

SRCDIR=${PROJECT_NAME}
TESTDIR=test_${PROJECT_NAME}

VIRTUALENV=virtualenv -p python3
VIRTUALENV_DIR=${PWD}/env
PIP=${VIRTUALENV_DIR}/bin/pip
PIP_INSTALL=${PIP} install
PYTHON=${VIRTUALENV_DIR}/bin/python

# the `all` target will install everything necessary to develop
all: virtualenv install install-test

test:
	${VIRTUALENV_DIR}/bin/py.test -s ${TESTDIR}

virtualenv:
	if [ ! -e ${PIP} ]; then \
	${VIRTUALENV} ${VIRTUALENV_DIR}; \
	fi
	${PIP_INSTALL} --upgrade pip

install: virtualenv
	${PIP_INSTALL} -r requirements.txt

install-test: install
	${PIP_INSTALL} -r test-requirements.txt

clean:
	-rm -fv .DS_Store
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '__pycache__' -exec rm -rfv {} \;

dist-clean: clean
	-rm -rfv ${VIRTUALENV_DIR} && \
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;
