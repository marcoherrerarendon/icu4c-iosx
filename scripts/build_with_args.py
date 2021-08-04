import argparse

if __name__ == "__main__":
    cli = argparse.ArgumentParser(
        description='Builds all mac configurations in TeamCity',
        epilog='Copyright 2020, MakeMusic, Inc. All Rights Reserved.')
    cli.add_argument('buildTypeID', type=str, help='The build type ID of the build configuration you want to build.')
    cli.add_argument('-a', '--agentName', type=str, help=agentNameHelpStr)
    cli.add_argument('-x', '--xcodeVersion', type=str, help='Xcode version to use ("10", "11", or "12"). If 12, defaults to universal build')
    cli.add_argument('-c', '--comment', type=str, help='Build trigger comment')
    cli.add_argument('-r', '--recursive', action='store_true', help='Also builds dependencies')
    cli.add_argument('-d', '--delay', action='store_true', help='If set, and if recursive build, delays buildTypeID build by 2 hours')
    args = cli.parse_args()