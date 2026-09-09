import subprocess, sys

def test_cli_help():
    """Ensure the CLI entry point runs and shows help."""
    result = subprocess.run([sys.executable, '-m', 'nlp_engine.cli', '--help'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'nlp' in result.stdout.lower()
