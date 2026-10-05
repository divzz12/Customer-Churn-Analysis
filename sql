-- Calculate Month 3 Churn Probability by Onboarding Completion Status
SELECT 
    completed_onboarding_checklist,
    COUNT(DISTINCT user_id) AS total_users,
    SUM(CASE WHEN churned_at_month_3 = 1 THEN 1 ELSE 0 END) AS churned_users,
    ROUND(
        100.0 * SUM(CASE WHEN churned_at_month_3 = 1 THEN 1 ELSE 0 END) / COUNT(DISTINCT user_id), 
        2
    ) AS churn_rate_pct
FROM (
    SELECT 
        u.user_id,
        u.completed_onboarding_checklist,
        CASE 
            WHEN u.cancellation_date IS NOT NULL 
                 AND DATEDIFF(month, u.signup_date, u.cancellation_date) <= 3 
            THEN 1 ELSE 0 
        END AS churned_at_month_3
    FROM users u
) user_summary
GROUP BY completed_onboarding_checklist;



-- User behavior aggregation across feature logs and support tickets
SELECT 
    u.user_id,
    u.completed_onboarding_checklist,
    COUNT(DISTINCT f.log_id) AS total_feature_interactions,
    COUNT(DISTINCT st.ticket_id) AS support_tickets_raised,
    MAX(CASE WHEN u.cancellation_date IS NOT NULL THEN 1 ELSE 0 END) AS is_churned
FROM users u
LEFT JOIN feature_logs f ON u.user_id = f.user_id
LEFT JOIN support_tickets st ON u.user_id = st.user_id
GROUP BY u.user_id, u.completed_onboarding_checklist;
