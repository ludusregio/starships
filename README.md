## Starships
Python script to query an API from an alpine docker container.

### Prerequisites
Have docker and git installed, locally.

### Steps
Clone this repository and cd into the directory startships

```
git clone https://github.com/ludusregio/starships.git && cd ./startships
```
Build a local image.

```
docker built -t startships:latest .
```
Run a container with the image.

```
docker run -it --rm --name starwars startships:latest
```
