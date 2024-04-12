import unittest
import docker

class TestDocker(unittest.TestCase):

    def test_docker_containers(self):
        client = docker.from_env()

        # Sjekker om det finnes en konteiner med navnet "ada502-kode"
        ada502_kode_container = client.containers.get("ada502-kode")
        self.assertIsNotNone(ada502_kode_container)

        # Sjekker om konteineren "ada502-kode" inneholder to konteinere med navnene "app-1" og "frcm"
        container_names = [container.name for container in ada502_kode_container.containers()]
        self.assertIn("app-1", container_names)
        self.assertIn("frcm", container_names)

if __name__ == '__main__':
    unittest.main()