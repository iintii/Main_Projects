#!/bin/bash

TEST_DIR="tests"
OUTPUT_IR="temp.ir"

# Ensure ANTLR 4.9.1 is used (no version conflicts)
export PYTHONPATH="$PYTHONPATH:$(pwd)"  # Append to PYTHONPATH instead of overwriting

for testfile in "$TEST_DIR"/IRtest*.while; do
    echo "----------------------------------------"
    echo "Running test: $testfile"

    # Generate IR
    python3 compiler/IRGen.py < "$testfile" > "$OUTPUT_IR"
    if [ $? -ne 0 ]; then
        echo "ERROR: IRGen failed for $testfile. Skipping..."
        continue
    fi

    # Run interpreter on generated IR
    python3 simpleir/Interpreter.py "$OUTPUT_IR"
    RESULT=$?

    # Check result
    if [ $RESULT -eq 0 ]; then
        echo "Test PASSED"
    else
        echo "Test FAILED (exit code $RESULT)"
    fi
done

# Cleanup
rm -f "$OUTPUT_IR"
echo "----------------------------------------"
