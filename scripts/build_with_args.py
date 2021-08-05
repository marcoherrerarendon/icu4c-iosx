import argparse

if __name__ == "__main__":
    cli = argparse.ArgumentParser(
        description='Calls build script with arguments.')
    cli.add_argument('-r', '--release', type=str, help='Release tag to build. Builds latest if not specified.')
    cli.add_argument('-a', '--architecture', type=str, help='Architecture to build. Builds with native architecture if not specified.')
    args = cli.parse_args()