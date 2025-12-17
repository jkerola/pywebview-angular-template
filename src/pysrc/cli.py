from argparse import ArgumentParser


class _ArgsNamespace:
    debug: bool
    reload: bool


def _create_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-r",
        "--reload",
        action="store_true",
        dest="reload",
        default=False,
        help="enable live-reloading of the HTML, JS and CSS properties",
        required=False,
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        dest="debug",
        default=False,
        help="enable webview developer console",
        required=False,
    )
    return parser


def parse_args() -> _ArgsNamespace:
    """Parse commandline arguments into a namespace.

    Returns:
        _ArgsNamespace: Namespace for arguments
    """
    parser = _create_parser()
    args = parser.parse_args(namespace=_ArgsNamespace)
    return args
