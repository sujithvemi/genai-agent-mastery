locals {
    deployer_roles = [
        "roles/artifactregistry.admin",
        "roles/iam.serviceAccountAdmin",
        "roles/iam.serviceAccountUser",
        "roles/run.admin",
        "roles/serviceusage.serviceUsageAdmin",
        "roles/storage.admin"
    ]
}

resource "google_project_iam_member" "deployer" {
    for_each = toset(local.deployer_roles)
    project = var.project_id
    role = each.value
    member = "serviceAccount:${google_service_account.terraform_deployer.email}"
}

resource "google_project_iam_member" "runtime_aiplatform_user" {
    project = var.project_id
    role = "roles/aiplatform.user"
    member = "serviceAccount:${google_service_account.hello_agent_runtime.email}"
}
