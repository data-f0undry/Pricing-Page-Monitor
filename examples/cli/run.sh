#!/usr/bin/env bash
# Apify CLI - install with: npm install -g apify-cli
set -euo pipefail
apify call data_foundry/pricing-page-monitor --input-file input.json --output-dataset
