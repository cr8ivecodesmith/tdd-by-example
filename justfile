set unstable
set shell := ["bash", "-eu", "-o", "pipefail", "-c"]


[doc(
"Run tests using pytest.
Modes: 'full' runs all tests, 'changed' runs only modified test files."
)]
test mode="changed":
    #!/bin/env bash
    if [ "{{mode}}" = "full" ]; then
        uv run pytest
    else
        mapfile -t test_files < <(git ls-files -m -o --exclude-standard -- tests)
        if [ "${#test_files[@]}" -gt 0 ]; then
            echo "Running changed test files:"
            printf ' - %s\n' "${test_files[@]}"
            uv run pytest --maxfail=1 "${test_files[@]}"
        else
            echo "No changed test files detected."
        fi
    fi


[doc(
"Run linting using ruff.
Modes: 'check' checks for issues, 'fix' automatically fixes them."
)]
lint mode="check":
    #!/bin/env bash
    if [ "{{mode}}" = "fix" ]; then
        uv run ruff check --fix src tests
    else
        uv run ruff check src tests
    fi
