#!/usr/bin/env bash
# Set the GitHub "About" panel (description, website, topics) and enable the wiki.
#   bash scripts/set_repo_about.sh
set -euo pipefail
REPO="peytonbackus-spec/mitek-gtm-toolkit"

gh repo edit "$REPO" \
  --description "GTM Engineer (lead → opportunity) and GTM Strategy & Ops (opportunity → renewal) toolkit for Mitek: scoring, routing, funnel, forecasting, deal-risk and renewal tooling on a shared Salesforce + AI-governance core. Synthetic data." \
  --homepage "https://github.com/${REPO}/wiki" \
  --enable-wiki \
  --add-topic gtm-engineering \
  --add-topic revenue-operations \
  --add-topic revops \
  --add-topic salesforce \
  --add-topic clari \
  --add-topic salesloft \
  --add-topic clay \
  --add-topic lead-scoring \
  --add-topic forecasting \
  --add-topic ai-governance \
  --add-topic python \
  --add-topic sql

echo "About panel updated: https://github.com/${REPO}"
