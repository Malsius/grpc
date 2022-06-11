import os


def load_credential_from_file(filepath):
    real_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(real_path, 'rb') as f:
        return f.read()


SERVER_CERTIFICATE = load_credential_from_file('credentials/server.crt')
SERVER_CERTIFICATE_KEY = load_credential_from_file('credentials/server.key')
ROOT_CERTIFICATE = load_credential_from_file('credentials/root.crt')
