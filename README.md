# Flask CI/CD Pipeline Project with Jenkins and Docker

## About This Project

This project is my hands-on journey to build a simple yet effective CI/CD pipeline for a Flask application using Jenkins and Docker. I created it to understand how to automate the build and deployment of containerized applications.

---

## How I Created This Project

### 1. **Starting with the Flask App**

I began by writing a basic Flask app (`app.py`) — a simple web server that runs on port 5000 and displays a welcome message. I also added a `requirements.txt` file listing the Python packages needed.

### 2. **Containerizing the App with Docker**

Next, I created a `Dockerfile` to containerize the Flask app. The Dockerfile:

- Uses a lightweight Python 3.9 image as the base.
- Copies the app code and dependencies.
- Installs required Python packages.
- Specifies the command to start the Flask server.

This helped me learn how to package an app into a portable container.

### 3. **Setting Up Jenkins**

I installed Jenkins on my machine and configured it for pipeline builds. To make Jenkins talk to GitHub and Docker:

- I installed necessary plugins like Git, Pipeline, and Docker Pipeline.
- Added my GitHub repository URL in the Jenkins job configuration.
- Configured credentials in Jenkins for GitHub access (if private).
- Ensured the Jenkins user had permission to run Docker commands by adding it to the Docker group.

### 4. **Writing the Jenkins Pipeline**

I wrote a `Jenkinsfile` using the Declarative Pipeline syntax that defines the following stages:

- **Checkout SCM:** Pulls the latest code from GitHub.
- **Build Docker Image:** Builds a Docker image for the Flask app.
- **Run Container:** Runs the Docker container on the Jenkins host.

This pipeline helped me automate the build and deployment process seamlessly.

### 5. **Testing and Debugging**

I ran multiple builds and carefully checked the Jenkins console output to debug permission issues (like Docker socket access) and Git checkout errors. After some trial and error, the pipeline ran successfully, building the Docker image and running the Flask app container.

### 6. **Next Steps**

Now that the CI/CD pipeline is working locally, I plan to:

- Push Docker images to a registry like Docker Hub.
- Deploy the containerized app to a cloud platform or Kubernetes.
- Add automated testing and notifications to the pipeline.

---

## What I Learned

- How to containerize Python applications with Docker.
- The basics of Jenkins pipelines and pipeline syntax.
- Managing Jenkins credentials and permissions for Docker.
- Automating code deployment workflows.

---

## How to Use This Project

If you want to try this yourself:

1. Clone the repo.
2. Set up Jenkins with Docker access.
3. Create a pipeline job pointing to this repo.
4. Run the pipeline and visit `http://<jenkins-host>:5000` to see the Flask app live.

---

## Final Thoughts

This project gave me practical experience with DevOps tools and helped me understand the automation of application delivery. I hope this can serve as a simple starting point for anyone looking to learn CI/CD with Jenkins and Docker.

---

## About Me

I’m Ashutosh Shrungare, a cloud and DevOps enthusiast. Feel free to connect or check out more projects on my [GitHub](https://github.com/Ashutosh-9216).

---

## License

MIT License
