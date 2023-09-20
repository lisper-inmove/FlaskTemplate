dev:
	make api && make entity && export PYTHONPATH=`pwd`/src && source bin/util.sh && APPROOT=`pwd`/src python src/app.py
run:
	make api && make entity && export PYTHONPATH=`pwd`/src && source bin/util.sh && APPROOT=`pwd`/src gunicorn --workers 2 --threads 2 --bind 0.0.0.0:8000 app:app

api:
	cd src/proto && make api-python
entity:
	cd src/proto && make entity

build:
	sudo docker build . -t mh.com:8890/test/demo:v1.0
	sudo docker push mh.com:8890/test/demo:v1.0
restart:
	kubectl delete -f k8s/deployment.yaml
	kubectl apply -f k8s/deployment.yaml

create:
	/bin/bash bin/create.sh
clear:
	echo "输入要删除的entity: "; \
	read entity; \
	echo "Just For Test"; \
	rm src/manager/$${entity}_manager.py; \
	rm src/proto/api/api_$${entity}.proto; \
	rm src/dao/$${entity}_dao.py; \
	rm src/ctrl/$${entity}_ctrl.py; \
	rm src/proto/entities/$${entity}.proto
