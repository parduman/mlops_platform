# MLOps Platform Backend Service

This project is a backend service for an MLOps platform, designed to manage user authentication, organization membership, cluster resource allocation, and deployment scheduling. The service optimizes deployment priority, resource utilization, and maximizes successful deployments.

## Features

- **User Authentication**: Basic authentication with username and password.
- **Organization Management**: Users can join organizations using invite codes.
- **Cluster Management**: Create and manage clusters with specified resources (RAM, CPU, GPU).
- **Deployment Management**: Deploy Docker images to clusters with resource allocation and queuing.
- **Scheduling Algorithm**: Preemption-based scheduling prioritizing high-priority deployments.

## Technologies Used

- **Backend Framework**: Django
- **Database**: sqlite3
- **Task Queue**: Celery with Redis
- **Containerization**: Docker

## Prerequisites

- Python 3.8+
- Docker
- Docker Compose
- sqlite3
- Redis

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/mlops-backend.git
   cd mlops-backend
