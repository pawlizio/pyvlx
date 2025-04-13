import asyncio
import logging

from pyvlx import PyVLX


logger = logging.getLogger("pyvlx")

logging.basicConfig(filename="message.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG)


async def main() -> None:
    pw = "BD92c2J37R"
    ip = "192.168.178.76"
    pyvlx = PyVLX(host=ip, password=pw)
    await pyvlx.connection.connect()
    await pyvlx.klf200.password_enter(pw)
    await pyvlx.klf200.get_systemtable_data()
    await pyvlx.load_nodes()
    pyvlx.connection.disconnect()

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
