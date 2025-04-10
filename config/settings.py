import argparse

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="https://reqres.in", help="Target host")
    parser.add_argument("--env", type=str, default="qa", help="Environment name")
    return parser.parse_known_args()[0]
