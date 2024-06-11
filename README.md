# Python API Debug

```sh
# Create a namespace
oc new-project api-debug

# Create application in OpenShift
oc new-app  --strategy=docker --name api-debug --context-dir=service https://github.com/clbartolome/python-rest-debug
```




