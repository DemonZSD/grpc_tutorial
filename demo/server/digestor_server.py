#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: weshzhu
# @Date: 2019-03-27 14-29
# @FUNCTION: 
from concurrent.futures import ThreadPoolExecutor
import grpc
import time
import hashlib
from demo.generate_src import digestor_pb2
from demo.generate_src import digestor_pb2_grpc


class DigestorServicer(digestor_pb2_grpc.DigestorServicer):
    """
    gRPC server for Digestor Service
    digestor_pb2_grpc.DigestorServicer 类 根据 `digestor.proto` 文件声明的 `service Digestor`生成
    """
    def __init__(self, *args, **kwargs):
        self.server_port = 5001

    def GetDigestor(self, request, context):
        """
        重写digestor_pb2_grpc.DigestorServicer 方法 GetDigestor，用于处理
        :param request: 接收 请求参数
        :param context: 上下文
        :return: DigestedMessage类型
        """
        tobeDigested = request.ToDigest
        hasher = hashlib.sha256()
        hasher.update(tobeDigested.encode())
        digested = hasher.hexdigest()
        print digested
        # result 即为 digestor.proto 文件声明的DigestedMessage 类型
        # 保证变量名称(Digested, WasDigest)与 DigestedMessage 声明的一致
        result = {'Digested': digested, 'WasDigest': True}
        return digestor_pb2.DigestedMessage(**result)

    def start_server(self):
        """
        start gRPC server and receive the clients witch will connect to it
        :return:
        """
        # 实例化 server 对象，接收指定大小的线程池
        digestor_server = grpc.server(ThreadPoolExecutor(max_workers=5))

        # 将服务添加到 server 对象中
        digestor_pb2_grpc.add_DigestorServicer_to_server(DigestorServicer(), digestor_server)

        # 绑定 server 到 端口号
        digestor_server.add_insecure_port('[::]:{port}'.format(port=self.server_port))
        # start the server
        digestor_server.start()
        print ('Digestor Server running ...')
        try:
            # need an infinite loop since the above
            # code is non blocking, and if I don't do this
            # the program will exit
            while True:
                time.sleep(60 * 60 * 60)
        except KeyboardInterrupt:
            digestor_server.stop(0)
            print('Digestor Server Stopped ...')


if __name__ == '__main__':
    curr_server = DigestorServicer()
    curr_server.start_server()
