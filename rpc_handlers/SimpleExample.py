import time

from rpc_handlers import TestTargetServer


class SimpleTest:
    def test_001(self):
        time.sleep(6)
        return "ok.1"

    def test_004(self):
        time.sleep(5)
        return "ok.2"

    def test_003(self):
        raise Exception("Exc")

if __name__ == "__main__":
    srv = TestTargetServer(("0.0.0.0", 1337))
    srv.run_server(test_instance=SimpleTest())

