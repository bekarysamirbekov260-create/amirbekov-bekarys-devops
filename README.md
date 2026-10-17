# amirbekov-bekarys-devops
DevOps Laboratory Work 1 — Bekarys Amirbekov, group IT2 2309, Student ID 37898.
Pipeline: Linux -> Git -> GitHub -> Docker -> Jenkins

## How to run
    docker build -t amirbekov-bekarys-devops .
    docker run -d --name amirbekov-bekarys-container amirbekov-bekarys-devops
    docker logs amirbekov-bekarys-container
