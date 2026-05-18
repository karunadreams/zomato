import pytest
from click.testing import CliRunner
from milestone1.cli import main

def test_info_command():
    runner = CliRunner()
    result = runner.invoke(main, ["info"])
    assert result.exit_code == 0
    assert "Zomato Recommendation System" in result.output
    assert "Phase 0 Initialized" in result.output

def test_doctor_command():
    runner = CliRunner()
    result = runner.invoke(main, ["doctor"])
    assert result.exit_code == 0
    assert "Running system check..." in result.output
