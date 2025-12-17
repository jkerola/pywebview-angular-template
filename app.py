from src.pysrc.main import run
from src.pysrc.cli import parse_args

if __name__ == "__main__":
    args = parse_args()
    run(debug=args.debug, reload=args.reload)
