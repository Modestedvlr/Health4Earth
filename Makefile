# Makefile pour HEALTH4EARTH

install:
\tpip install -e .

ingest:
\tpython -m my_module_name.data_ingest

clean:
\tpython -m my_module_name.data_clean

build-site:
\tquarto render website/

test:
\tpytest tests/
