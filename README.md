# cadquery-openfaas-functions
Functions allowing CadQuery to be used via the OpenFaaS platform.

## Deploying
Be sure to specify the `DOCKER_USER` variable when deploying.
```
DOCKER_USER="your_user_name" faas-cli up
```

## Invoking
From the command line:
```
echo "import cadquery as cq;result = cq.Workplane('XY').box(1,1,1);show_object(result)" | faas-cli invoke tjs-export
```
