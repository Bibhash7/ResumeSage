# ResumeSage: Resume Reviewer with AI-Powered Insights

## Overview
This project is an AI-driven Resume Reviewer built using Django and Celery, leveraging Ollama for intelligent resume analysis. The application securely uploads resumes to an S3 bucket, reads and processes their content, and sends the review results directly to the user’s email. The user authentication is managed through PostgreSQL, and asynchronous task management is powered by Celery with AWS LocalStack SQS as the message broker.

This application offers seamless integration between cutting-edge AI and modern backend technologies, ensuring a smooth and efficient user experience.

## System Architecture
[![System-Diagram-Resume-Sage.png](https://i.postimg.cc/0QMgtQdf/System-Diagram-Resume-Sage.png)](https://postimg.cc/S2htRmP2)

## Features

- **AI-Powered Resume Analysis**
  - Utilizes Ollama for reviewing and analyzing resumes to provide insightful feedback.

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

- **Scalable Architecture**
  - Built with scalability in mind, leveraging distributed task queues and robust database support.

## Tech Stack

- **Backend**: Django
- **Task Queue**: Celery
- **AI**: Ollama
- **Storage**: AWS S3
- **Database**: PostgreSQL
- **Broker**: AWS LocalStack SQS

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to update this README file based on your project’s specific requirements or enhancements!
