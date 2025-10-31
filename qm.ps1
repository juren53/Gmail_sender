#!/usr/bin/env pwsh
# Quickmail launcher script for PowerShell
# Runs quickmail.py with all passed arguments

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "quickmail.py"

if (Test-Path $pythonScript) {
    python $pythonScript $args
} else {
    Write-Error "Error: quickmail.py not found in $scriptDir"
    exit 1
}
