import asyncio
from asyncio import transports


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.transport = transport
        print('connection_made')

    def data_received(self, data: bytes) -> None:
        data_len = len(data)
        print(f'received: {data_len}')
        self.transport.write(data)


async def handle_connection(reader, writer):
    print('connection_made')
    while True:
        data = await reader.read(100)
        if data:
            data_len = len(data)
            print(f'received: {data_len}')
            writer.write(data)
            await writer.drain()
        else:
            print('closed')
            writer.close()
            break


def run_proto():
    loop = asyncio.get_event_loop()
    server = loop.create_server(EchoServer, '127.0.0.1', 15555)
    loop.run_until_complete(server)
    loop.run_forever()


def run_handler():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.ensure_future(
            asyncio.start_server(handle_connection, '127.0.0.1', 15555), loop=loop
        )
    )
    loop.run_forever()


run_handler()
