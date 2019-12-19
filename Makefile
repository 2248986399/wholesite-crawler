SRV_NAME=wholesite-crawler
REPO_EX=docker.pkg.github.com

NAME_SPACE=speechfree
REPO=${REPO_EX}
TAG=$(shell date +%Y%m%d%H%M%S)
FIXTAG?=prod
NAME=${REPO}/${NAME_SPACE}/${SRV_NAME}/${SRV_NAME}

base:
	echo build ${NAME}:base
	cp docker/base/Dockerfile .
	docker build -t ${NAME}:base .
	rm Dockerfile
	docker push ${NAME}:base

build:
	echo build ${NAME}:${TAG}
	cp docker/prod/Dockerfile .
	docker build -t ${NAME}:${FIXTAG} .
	docker tag ${NAME}:${FIXTAG} ${NAME}:${TAG}
	rm Dockerfile

	echo push into ${REPO}
	docker push ${NAME}:${TAG}
	docker push ${NAME}:${FIXTAG}

dev:
	docker-compose up -d

down:
	docker-compose down

exec:
	docker exec -it serverless bash