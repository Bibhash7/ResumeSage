# ResumeSage: Resume Reviewer with AI-Powered Insights

## Overview
This project is an AI-driven Resume Reviewer built using Django and Celery, leveraging **Ollama** for intelligent resume analysis. It streamlines the process of reviewing resumes by integrating modern backend technologies and secure storage solutions, ensuring a seamless and efficient user experience.

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
