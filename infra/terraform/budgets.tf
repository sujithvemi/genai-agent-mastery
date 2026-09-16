resource "google_monitoring_notification_channel" "budget_email" {
  project      = var.project_id
  display_name = "Budget alerts"
  type         = "email"

  labels = {
    email_address = var.alert_email
  }
}

resource "google_billing_budget" "project_budget" {
  billing_account = var.billing_account_id
  display_name    = "hello-agent-learning-budget"

  budget_filter {
    projects = ["projects/${var.project_number}"]
  }

  amount {
    specified_amount {
      units         = var.budget_amount_usd
    }
  }

  # Actual-spend thresholds (CURRENT_SPEND is the default)
  threshold_rules {
    threshold_percent = 0.5
  }

  threshold_rules {
    threshold_percent = 0.9
  }

  threshold_rules {
    threshold_percent = 1.0
  }

  # Forecasted-spend threshold
  threshold_rules {
    threshold_percent = 1.0
    spend_basis       = "FORECASTED_SPEND"
  }

  all_updates_rule {
    monitoring_notification_channels = [google_monitoring_notification_channel.budget_email.id]
    disable_default_iam_recipients   = false
  }
}
