# ResumeSage: Resume Reviewer with AI-Powered Insights

## Overview
This project is an AI-driven Resume Reviewer built using Django and Celery, leveraging Ollama for intelligent resume analysis. The application securely uploads resumes to an S3 bucket, reads and processes their content, and sends the review results directly to the user’s email. The user authentication is managed through PostgreSQL, and asynchronous task management is powered by Celery with AWS LocalStack SQS as the message broker. The application also securely fetches database credentials from AWS Secrets Manager to ensure the security of sensitive information and provides a score based on the structure, format, and professionalism of the resume. Also based on the resume, it will generate 10 interview questions.

This application offers seamless integration between cutting-edge AI and modern backend technologies, ensuring a smooth and efficient user experience.

## System Architecture
[![System-Diagram-Resume-Sage-Redefined.png](https://i.postimg.cc/dQpgXNQK/System-Diagram-Resume-Sage-Redefined.png)](https://postimg.cc/rzGhRJth)

## Features

- **AI-Powered Resume Analysis, Scoring and Interview Questions**
  - Utilizes Ollama Gemma2 LLM for reviewing and analyzing resumes to provide insightful feedback and overall score.
  - **Upd**: It also generate 10 sample interview questions based on the resume.

- **Secure File Handling**
  - Resumes are securely uploaded to an Aws Localstack S3 bucket via presigned url for processing.

- **Email Notifications**
  - Sends review results to the user’s email stored in Django sessions.

- **User Authentication**
  - User login and sign-up data are securely stored and managed in a PostgreSQL database.

- **Asynchronous Task Management**
  - Background tasks are handled efficiently using Celery.

- **LocalStack SQS Integration**
  - AWS LocalStack SQS serves as the message broker for Celery tasks.

- **Database Credentials Security**
  - The application securely fetches database credentials from AWS Secrets Manager to ensure the security of sensitive information.

- **Scalable Architecture**
  - Built with scalability in mind, leveraging distributed task queues and robust database support.

## Demo

https://github.com/user-attachments/assets/f350657c-3495-4e35-abdf-f3b1cd0ad505


## Screenshot
**Home**

[![Home-screen.png](https://i.postimg.cc/mrxR07kn/Home-screen.png)](https://postimg.cc/3kZPG4gj)

**Review Screen**

[![Review-Screen.png](https://i.postimg.cc/0NQS6RPm/Review-Screen.png)](https://postimg.cc/QF2CPzBx)

**Email: Review and Interview Questions**

[![Resume-Sage-redefined-prompt.png](https://i.postimg.cc/HntPVxmX/Resume-Sage-redefined-prompt.png)](https://postimg.cc/5Q6mrf62)

**LocalStack S3 Bucket Snapshot**

[![S3-bucket-snapshot.png](https://i.postimg.cc/wBmS0Z77/S3-bucket-snapshot.png)](https://postimg.cc/B8JYvh50)

## Tech Stack

- **Backend**: Django
- **Task Queue**: Celery
- **AI**: Ollama Gemma 2B
- **Storage**: AWS LocalStack S3
- **Database**: PostgreSQL
- **Broker**: AWS LocalStack SQS
- **Secret Manager**: AWS LocalStack Secrets Manager, .env
- **Containerization**: Docker

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
