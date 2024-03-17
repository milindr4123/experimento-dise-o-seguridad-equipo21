import unittest
from app import create_app
from flask_jwt_extended import create_access_token, JWTManager


class FlaskJWTTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.jwt_manager = JWTManager(self.app)

    def test_access_with_valid_token(self):
        # Generar un token válido para un usuario 'admin'
        with self.app.app_context():
            access_token = create_access_token(identity='admin')
        headers = {'Authorization': f'Bearer {access_token}'}

        # Intentar acceder a la ruta protegida con el token válido
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('logged_in_as', response.get_json())

    def test_access_without_token(self):
        # Intentar acceder a la ruta protegida sin proporcionar un token
        response = self.client.get('/protected')
        self.assertNotEqual(response.status_code, 200)

    def test_access_with_invalid_token(self):
        # Utilizar un token inválido
        invalid_token = 'Bearer thisisnotavalidtoken'
        headers = {'Authorization': invalid_token}

        # Intentar acceder a la ruta protegida con el token inválido
        response = self.client.get('/protected', headers=headers)
        self.assertNotEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
