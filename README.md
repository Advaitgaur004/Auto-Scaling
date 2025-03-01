# Cloud-Based Flask Application Repository

This repository contains the source code and setup scripts for a scalable Flask web application deployed on Google Cloud Platform (GCP) using VM instances, a load balancer, and an instance template.

## Components
- `startup.sh`: Script to configure VM instances, install dependencies, and start the Flask app.
- `app.py`: Flask application that calculates the factorial of 1000 and serves it via a web endpoint.

## Setup Instructions
1. Clone this repository: `git clone <repository-url>`.
2. Use `startup.sh` in your VM instance template (e.g., via GCP Console or gcloud CLI).
3. Ensure `app.py` is placed in the VM’s filesystem (the startup script handles this by default).

## Prerequisites
- Python 3
- Flask (`pip3 install flask`)
- A cloud environment (e.g., GCP) with VM instances and a load balancer.

## Notes
- The Flask app runs on port 5000 and is accessible via the load balancer’s external IP.
- See the video demonstration [here](#) for a full walkthrough.