terraform {
  backend "gcs" {
    bucket = "sujithvemi-genai-learning-dev-tfstate"
    prefix = "hello-agent"
  }
}
