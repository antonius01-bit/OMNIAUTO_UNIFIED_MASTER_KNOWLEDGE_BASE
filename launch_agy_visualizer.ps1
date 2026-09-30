#!/usr/bin/env pwsh
$htmlPath = Join-Path $PSScriptRoot 'agy_workflow_visualizer.html'
Write-Host '[⚡] Launching AGY Workflow Visualizer...' -ForegroundColor Cyan
Start-Process $htmlPath
