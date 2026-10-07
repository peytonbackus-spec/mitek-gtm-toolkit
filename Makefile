.PHONY: data demo test eng ops shared brief

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
	python -m gtm_engineer.marketing_ops.campaign_report
	python -m gtm_engineer.marketing_ops.demand_plan

ops:
	python -m gtm_strategy_ops.pipeline_analytics.pipeline_report
	python -m gtm_strategy_ops.forecasting.forecast_accuracy
	python -m gtm_strategy_ops.ai_deal_risk.deal_risk
	python -m gtm_strategy_ops.renewals.renewal_signals
	python -m gtm_strategy_ops.renewals.closed_lost_analysis
	python -m gtm_strategy_ops.sales_leadership.rep_scorecard
	python -m gtm_strategy_ops.sales_leadership.segment_performance
	python -m gtm_strategy_ops.sales_leadership.stage_velocity
	python -m gtm_strategy_ops.sales_leadership.deal_board
	python -m gtm_strategy_ops.sales_leadership.vp_brief
	python -m gtm_strategy_ops.sales_leadership.vp_brief --mode full
	python -m gtm_strategy_ops.sales_leadership.all_hands
	python -m gtm_strategy_ops.sales_planning.capacity_plan
	python -m gtm_strategy_ops.sales_planning.quota_plan
	python -m gtm_strategy_ops.sales_planning.territory_plan
	python -m gtm_strategy_ops.sales_planning.pipeline_distribution
	python -m gtm_strategy_ops.sales_planning.request_triage

demo: shared eng ops

brief:
	python -m gtm_strategy_ops.sales_leadership.vp_brief

test:
	python -m pytest -q
