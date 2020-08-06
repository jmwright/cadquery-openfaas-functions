# cadquery-openfaas-functions
Functions allowing CadQuery to be used via the OpenFaaS platform.

## Pull templates
From within this repo's root directory, run the following.
```
faas-cli template pull https://github.com/jmwright/cadquery-openfaas-templates

```

## Deploy
Be sure to specify the `DOCKER_USER` variable when deploying.
```
DOCKER_USER="your_user_name" faas-cli up
```

## Invoke
From the command line:
```
echo "import cadquery as cq;result = cq.Workplane('XY').box(1,1,1);show_object(result)" | faas-cli invoke tjs-export
```
