build:
	docker build -t sex-mans -f Dockerfile .

run: build
	docker container run -it --rm sex-mans:latest /bin/bash

start: build
	docker container run -dit --name sex-mans sex-mans:latest

stop:
	docker container stop sex-mans

clean: stop
	docker container rm sex-mans

build-force:
	docker build -t sex-mans -f Dockerfile --no-cache .
