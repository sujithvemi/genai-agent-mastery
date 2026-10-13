resource "google_storage_bucket" "tfstate" {
    name = "sujithvemi-genai-learning-dev-tfstate"
    project = var.project_id
    location = "US-CENTRAL1"
    uniform_bucket_level_access = true

    versioning {
        enabled = true
    }

    lifecycle {
        prevent_destroy = true
    }
}
