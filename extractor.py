from argparse import ArgumentParser, Namespace
import sys
import zipfile


def main(args: Namespace) -> int:
    with zipfile.ZipFile(args.jar_path, "r") as jar:
        for file in jar.namelist():
            if file.startswith("assets/"):
                # Extract the file to the output directory
                jar.extract(file, args.output)
                print(f"Extracted: {file}")
    return 0


if __name__ == "__main__":
    parser = ArgumentParser(description="Extract the entirety of Minecraft's assets.")

    parser.add_argument(
        "asset_path",
        type=str,
        help="Path to Minecraft's assets folder.",
    )
    parser.add_argument(
        "index",
        type=int,
        help="The index of the asset index to extract. For example, 19 for 1.21.4.",
    )
    parser.add_argument(
        "jar_path",
        type=str,
        help="Path to the Minecraft jar file.",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="./extracted_assets",
        help="Path to the output folder. Defaults to the current working directory.",
    )

    sys.exit(main(parser.parse_args()))
