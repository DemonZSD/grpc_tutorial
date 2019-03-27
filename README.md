# grpc_tutorial

### Contents:

```
$ tree -L 3 grpc_tutorial
grpc_tutorial
|-- demo
|   |-- client
|   |   |-- digestor_client.py
|   |   `-- __init__.py
|   |-- generate_src
|   |   |-- digestor_pb2_grpc.py
|   |   |-- digestor_pb2.py
|   |   `-- __init__.py
|   |-- __init__.py
|   |-- protos
|   |   `-- digestor.proto
|   `-- server
|       |-- digestor_server.py
|       `-- __init__.py
|-- README.md
`-- requirements.txt
```

### Start gRPC server
```
$ python

>>> from demo.server import digestor_server
>>> Digestor_server = digestor_server.DigestorServicer()
>>> digestor_server = digestor_server.DigestorServicer()
>>> digestor_server.start_server()
Digestor Server running ...
532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25
```

### run gRPC client
```
$ python
>>> from demo.client.digestor_client import DigestorClient
>>> digestor_client = DigestorClient()
>>> digestor_client.get_digest('Test')
Digested: "532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25"
WasDigest: true
```




