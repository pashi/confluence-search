# confluence-search

Why: I need to find confluence pages which include tags (label) with "python"

This script login to cloud confluence instance with credentials and search pages by tags. As well print them by pdf local directory.

## build docker

docker-compose build

## setup docker
````
cp config/example config/confluence
code config/confluence
````

## run examples

* docker-compose run search-python
* docker-compose run save-python-pdf
