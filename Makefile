data-ingest:
\tpython -m health4earth.data_ingest

data-clean:
\tpython -m health4earth.data_clean

data-transform:
\tpython -m health4earth.data_transform

build-site:
\tquarto render website/
