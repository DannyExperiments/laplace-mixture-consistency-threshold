# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay uses exact rational Taylor brackets to check 528 interior ratio comparisons across 16 inverse scales and the corresponding mass/tail and cubic bounds. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/laplace-shapes-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font paths. [Build the paper](paper/BUILD.md).
