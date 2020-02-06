[aliases]
test = pytest

[isort]
not_skip =
    __init__.py,
multi_line_output = 3
force_grid_wrap = 2
combine_as_imports = true
combine_star = true
include_trailing_comma = true
lines_after_import = 2
lines_between_types = 1

[pycodestyle]
max-line-length = 120