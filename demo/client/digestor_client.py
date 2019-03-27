#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: zsd
# @Email: zsd498537806@gmail.com
# @Date: 2019-03-27 15-17
# @FUNCTION: 
import grpc
from demo.generate_src import digestor_pb2_grpc
from demo.generate_src import digestor_pb2


class DigestorClient(object):
    def __init__(self):
        self.server_host = 'localhost'
        self.server_port = 5001

        # 初始化一个 channel 用于建立client 和 server 之间的通信管道
        self.channel = grpc.insecure_channel(
            '{ip}:{port}'.format(ip=self.server_host, port=self.server_port))

        # 绑定 client 到 gRPC server 的 channel
        self.stub = digestor_pb2_grpc.DigestorStub(self.channel)

    def get_digest(self, message):
        # 实例化 DigestMessage 对象
        to_digest_message = digestor_pb2.DigestMessage(ToDigest=message)
        return self.stub.GetDigestor(to_digest_message)


if __name__ == '__main__':
    digestor_client = DigestorClient()
    digestor_client.get_digest('Test')
