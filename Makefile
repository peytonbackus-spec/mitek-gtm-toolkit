.PHONY: data demo test eng ops shared

data:
	python scripts/generate_sample_data.py

shared:
	python -m shared_core.data_quality.dq_monitor
	python -m shared_core.metrics.run_sql gtm_engineer/funnel_analytics/sql/lead_funnel.sql
	python -m shared_core.metrics.run_sql gtm_strategy_ops/pipeline_analytics/sql/pipeline_coverage.sql

eng:
	python -m gtm_engineer.lead_scoring.score_leads
	python -m gtm_engineer.lead_scoring.calibrate_scoring
	python -m gtm_engineer.lead_routing.route_leads
	python -m gtm_engineer.lead_lifecycle.lifecycle_sla
	python -m gtm_engineer.ai_research.account_research
	python -m gtm_engineer.funnel_analytics.funnel_report
	python -m gtm_engineer.sdr_capacity.capacity_model

ops:
	python -m gtm_strategy_ops.pipeline_analytics.pipeline_report
	python -m gtm_strategy_ops.forecasting.forecast_accuracy
	python -m gtm_strategy_ops.ai_deal_risk.deal_risk
	python -m gtm_strategy_ops.renewals.renewal_signals
	python -m gtm_strategy_ops.renewals.closed_lost_analysis

demo: shared eng ops

test:
	python -m pytest -q
