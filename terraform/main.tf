# TW2 3.2 - simple IaC: create a local file (output.txt)
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

resource "local_file" "output" {
  content  = "Hello from Terraform! DevOps lab, generated on the openterminal box.\n"
  filename = "${path.module}/output.txt"
}
