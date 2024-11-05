
# Terarea (Project: Area)

![The teraria icon](https://raw.githubusercontent.com/bazar-de-komi/terarea/refs/heads/main/docs/markdown/favicon_markdown.png)

## Table of Contents

- [Project Overview](#project-overview)
- [Authors](#authors)
- [Repository](#repository)
- [Documentation](#documentation)
- [Active Website](#active-website)
- [Project Setup](#project-setup)
- [Frameworks and Languages](#frameworks-and-languages)
- [Deployment Instructions](#deployment-instructions)
- [License](#license)
- [Additional Considerations](#additional-considerations)
- [Commit norm](#commit-norm)
- [Acknowledgments](#acknowledgments)
- [References](#references)

---

## Project Overview

**Area** (repository name: `terarea`) is a platform designed to mimic the functionality of an **IFTTT** (If This Then That) website. The project includes:

- A **web page** and a **mobile app**.
- Interaction with a backend for data management and logic execution.
- The use of **different frameworks** for the web and mobile apps.

The project aims to showcase seamless communication between the frontend and backend, ensuring a rich user experience both on desktop and mobile devices.

---

## Authors

This project is authored by:

- **Harleen Singh-Kaur**
- **Eric Xu**
- **Flavien Maillard**
- **Thomas Lebouc**
- **Henry Letellier**

Ownership belongs to **Epitech**, with development conducted during **September**.

---

## Repository

The source code and version control for the project can be found at the following GitHub repository:

- [Terarea GitHub Repository](https://github.com/bazar-de-komi/terarea)

---

## Documentation

Comprehensive project documentation can be accessed here:

- [Area Documentation](https://ifttt-area.pingpal.news/)

---

## Active Website

The live version of the website can be found here:

- [Active Website](https://pingpal.news/)

---

## Project Setup

### Prerequisites

To set up the project locally, ensure you have the following tools installed:

- **Git** (or at least a local version of the repository): This will be used as the source for the tutorial
- **Docker**: To run containerized services.
- **Docker Compose**: To manage multi-container Docker applications.

### Local Deployment

If you already have an instance of the repository on your computer you can skip step 1.
The following lines are written assuming that you do not need privileges in order to use docker.
If this is the case (i.e. non-root linux user), you can add the `sudo` in front of the commands.

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/bazar-de-komi/terarea.git
    cd terarea
    ```

2. Make sure you have created the .env files in their respective folders

 > The following environments are for if you plan on running the services in the docker compose environement.
 > They do not contain sensitive data, hence: you will need to fill the sections that contained sensitive information by yourself.

- `app/back/db`:

  ```bash
  # [something] is to be considered as a placeholder for actual sensitive data.

  MYSQL_USER=my_user
  MYSQL_DATABASE=terarea
  MYSQL_PASSWORD=my_password
  MYSQL_ROOT_PASSWORD=root
  ```

- `app/back/s3`:

  ```bash
  # [something] is to be considered as a placeholder for actual sensitive data.

  MINIO_ROOT_USER=root     # min length 3
  MINIO_ROOT_PASSWORD=my_root_password # min length 8
  ```

- `app/back/server`:

  ```bash
  # [something] is to be considered as a placeholder for actual sensitive data.

  # e-mail sending data
  SENDER_ADDRESS=[the-address-of-the-account-sending]  # The e-mail address for the server to send e-mails
  SENDER_KEY=[16-character-auth-key]                   # Your authentication key
  SENDER_HOST=smtp.gmail.com                           # If you are using a gmail account
  SENDER_PORT=465                                      # If you are using a gmail account

  # Server Oauth variables
  REDIRECT_URI=[the-redirect-url-once-the-user-is-connected]

  # Databse login details
  DB_HOST=maria-db
  DB_PORT=3306
  DB_USER=my_user
  DB_PASSWORD=my_password
  DB_DATABASE=terarea

  # Bucket login details
  MINIO_HOST=minio
  MINIO_PORT=9000
  MINIO_ROOT_USER=root
  MINIO_ROOT_PASSWORD=my_root_password
  ```

- `app/front/mobile`:

  ```bash
    # [something] is to be considered as a placeholder for actual sensitive data.

    # Docker volume related information

    docker_volume_path="/shared_folder"
  ```

- `app/front/web`:

  ```bash
    # [something] is to be considered as a placeholder for actual sensitive data.

    # Docker volume related information

    docker_volume_path="/shared_folder"
  ```

3. To deploy the full stack locally, run the following command at the root of the repository:

    ```bash
    docker compose up
    ```

4. After the deployment is complete:
   - The frontend is accessible at: [http://localhost:8080](http://localhost:8080)
   - The backend is accessible at: [http://localhost:8081](http://localhost:8081)

If you wish to stop the docker compose, use the following command:

```bash
docker compose down
```

### Automated testing

In order to run the tests for this projects an instance of the docker compose is strongly recommended to be running.

The following sections will assume that this is the case.

When it comes to docker, remember to add the `sudo` command if it is required.

#### Server side

In order to run the test on the server side, please run:

```bash
docker exec -it t-server /bin/bash -c "pytest -s"
```

#### Front web

In order to run the tests on the web container, please run:

```bash
docker exec -it t-web /bin/bash -c "npm run tests"
```

#### Front mobile

In order to run the tests on the mobile container, please run:

```bash
docker exec -it t-mobile /bin/bash -c "npm run tests"
```

---

## Frameworks and Languages

### Project Constraints

Each technology can only be used **twice** in different contexts (e.g., frontend, mobile, backend). The breakdown is as follows:

- **Frontend (Web)**: **Vue.js**
- **Mobile App**: **React Native**
- **Backend**: **Python (uvicorn + FastAPI)**

### Frontend and Mobile Frameworks

The front and mobile app utilize different frameworks. For example:

- **Web Frontend**: Using **Vue.js**.
- **Mobile App**: Built with **React Native**, ensuring a distinct technology stack from the web.

### Backend Framework

The backend is developed using **FastAPI**, allowing for efficient server-side logic and data handling without relying on **Node.js**, given its usage in the frontend and mobile app.

---

## Deployment Instructions

### Frontend (Port 8080)

The web-based frontend will be exposed on **port 8080** once the Docker containers are up. Users can interact with the web interface through their browser.

### Backend (Port 8081)

The backend API will be accessible on **port 8081**, handling all server-side logic and data communication for both the web frontend and mobile app.

### Mobile (No port)

The installer for the mobile application will be provided in the front-end at [https://pingpal.news/download](https://pingpal.news/download).

---

## License

This project is under the ownership of **[Epitech](https://epitech.eu)** all rights reserved

---

## Additional Considerations

- **Contributions**: Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

---

## Commit norm

You can find the norm used for this repository here:

- [Commit norm](./COMMIT_CONVENTION.md)

---

## Acknowledgments

Thank you to the following people that have made this project possible:

Main contributors:

- **[Harleen-sk](https://github.com/Harleen-sk)**
- **[KomiWolf](https://github.com/KomiWolf)**
- **[OrionPX4k](https://github.com/OrionPX4k)**
- **[flavienepitech](https://github.com/flavienepitech)**
- **[Henry Letellier](https://github.com/HenraL)**

Everybody else:

[![All the contributors of terarea.](https://contrib.rocks/image?repo=bazar-de-komi/terarea)](https://contrib.rocks/image?repo=bazar-de-komi/terarea)

---

## References

- [Epitech](https://epitech.eu)
- [Epitech GitHub](https://github.com/epitech)
- [Project home page](https://pingpal.news)
- [Project documentation](https://ifttt-area.pingpal.news/)
- [Project API documentation]()
- [Project commit convention](./COMMIT_CONVENTION.md)
