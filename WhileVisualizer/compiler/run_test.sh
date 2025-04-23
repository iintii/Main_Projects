#!/bin/bash

TEST_DIR="examples"
export PYTHONPATH=$(pwd)  # Add the current directory to the Python module search path

for testfile in "$TEST_DIR"/*.while; do
    echo "-------------------------------------------------"
    echo "Running test: $testfile"
    python3 -m compiler.TypeChecker < "$testfile"
    RESULT=$?
    if [ $RESULT -eq 0 ]; then
        echo "Test PASSED"
    else
        echo "Test FAILED (exit code $RESULT)"
    fi
    echo "-------------------------------------------------"
done
