resource "google_service_account" "hello_agent_runtime" {
    project = var.project_id
    account_id = "hello-agent-runtime"
    display_name = "hello_agent Cloud Run time identity"
}

resource "google_service_account" "terraform_deployer" {
    project = var.project_id
    account_id = "terraform-deployer"
    display_name = "Terraform deployer (CI/local infra provisioning)"
}
