[run]
branch = true

[report]
precision = 2
fail_under = 60
show_missing = true
skip_covered = true
exclude_lines = 
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplemented
    if __name__ == (?:'|")__main__(?:'|"):