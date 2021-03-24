# Execution
## with Docker 
```shell script
docker build -t kodgemisi-assigment .
docker run --net=host kodgemisi-assigment
```

## without Docker
```shell script
pip3 install -r requirements.txt
python3 main.py
```