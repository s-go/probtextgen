# probtextgen

Dependencies
------------

* python3
* make
* virtualenv


Building
--------

To build the complete project, execute:

    make

To delete all files that are normally created by building the program, except
distribution files, execute:

    make clean

To delete all files that are normally created by building the program,
including distribution files, execute:

    make dist-clean

Dependencies (including versions) are defined in:

	requirements.txt
	test-requirements.txt

Testing
-------

To run all tests, execute:

	make test
