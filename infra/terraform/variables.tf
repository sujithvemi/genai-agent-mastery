variable "project_id" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  default     = "us-central1"
}

variable "budget_amount_usd" {
  type        = string
  default     = "1000"
}
