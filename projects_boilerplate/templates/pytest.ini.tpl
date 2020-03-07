[pytest]
testpaths = tests/ $project_sources_dir/
cache_dir = .cache
mccabe-complexity = 10
log_format =
    %(filename)s:%(lineno)d: [%(name)s:%(levelname)s] %(asctime)s: %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
addopts =
    --cov-config coverage.ini
    --cov-report term
    --cov-report html:coverage/html
    --cov $project_sources_dir/
    --pycodestyle
    --isort
    --mccabe
    --mypy
    --pylint --pylint-rcfile pylint.ini
    --verbose