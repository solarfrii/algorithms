import os
from pathlib import Path
import pytest
from dataclasses import dataclass
from subprocess import Popen, PIPE, TimeoutExpired


base_dir = Path('./binary_search')
tests_dir = base_dir.joinpath('tests')


@pytest.mark.parametrize('test_file', tests_dir.iterdir())
def test_prepared(test_file):
    with open(test_file, 'r') as lines:
        input, expected_output = _parse_test(lines)
    p = Popen(
        ['python3', base_dir.joinpath('main.py')],
        stdin=PIPE, stdout=PIPE, stderr=PIPE,
    )
    try:
        output, error = p.communicate(
            input='\n'.join(input).encode(),
            timeout=5,
        )
    except TimeoutExpired:
        p.kill()
        output, error = p.communicate()
    output = output.decode()
    output = list(filter(len, output.split('\n')))
    assert output == expected_output


def _parse_test(lines: [str]) -> [str, str]:
    input, output = [], []
    accumulator = input
    for line in [l.strip() for l in lines]:
        if len(line) == 0:
            accumulator = output
            continue
        label, line = line.split(':')
        line = line.strip()
        accumulator.append(line)
    return input, output
