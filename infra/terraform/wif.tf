resource "google_iam_workload_identity_pool" "github_pool" {
    project = var.project_id
    workload_identity_pool_id = "github-pool"
    display_name = "GitHub Actions Pool"
}

resource "google_iam_workload_identity_pool_provider" "github_provider" {
    project = var.project_id
    workload_identity_pool_id = google_iam_workload_identity_pool.github_pool.workload_identity_pool_id
    workload_identity_pool_provider_id = "github-provider"
    display_name = "GitHub OIDC provider"

    attribute_mapping = {
        "google.subject" = "assertion.sub"
        "attribute.repository" = "assertion.repository"
    }

    attribute_condition = "assertion.repository=='sujithvemi/genai-agent-mastery'"

    oidc {
        issuer_uri = "https://token.actions.githubusercontent.com"
    }
}

resource "google_service_account_iam_member" "deployer_wif_binding" {
    service_account_id = google_service_account.terraform_deployer.name
    role = "roles/iam.workloadIdentityUser"
    member = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.github_pool.name}/attribute.repository/sujithvemi/genai-agent-mastery"
}
