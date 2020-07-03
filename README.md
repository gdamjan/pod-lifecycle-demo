# a pod

* k8s cluster
* schedules pods on nodes

# what and why is pod lifecycle

* Is the pod ready?
* Is the pod healthy?
* Is the pod alive?
* What happens when the pod is updated.

## liveness
## healthiness
## readiness





# minikube preparations

https://minikube.sigs.k8s.io/docs/handbook/pushing/#4-pushing-to-an-in-cluster-using-registry-addon

* `minikube addons add registry`
* `minikube start --insecure-registry 192.168.39.0/24`
* `docker build --tag $(minikube ip):5000/demo-img:v1 --build-arg version=v1 .`
* `docker build --tag $(minikube ip):5000/demo-img:v2 --build-arg version=v2 .`
* `docker push $(minikube ip):5000/demo-img:v1`
* `kubectl create deployment demo-node --image=$(minikube ip):5000/demo-img:v1`
* `kubectl expose deployment demo-svc --type=LoadBalancer --port=5000`
* `minikube service demo-svc --url`
