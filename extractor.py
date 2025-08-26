from argparse import ArgumentParser, Namespace
import sys
import zipfile
import json
import shutil
import os


def main(args: Namespace) -> int:
    print(f"Extracting assets from {args.jar_path}...")
    with zipfile.ZipFile(args.jar_path, "r") as jar:
        for file in jar.namelist():
            if file.startswith("assets/"):
                # Extract the file to the output directory
                jar.extract(file, args.output)
                print(f"Extracted: {file}")
    print("Extraction complete.")

    print(f"Copying assets from index {args.index}...")
    with open(f"{args.asset_path}/indexes/{args.index}.json", "r") as f:
        index_data = json.load(f)
        objects = index_data["objects"]
        for name, info in objects.items():
            path = f"{args.asset_path}/objects/{info['hash'][0:2]}/{info['hash']}"
            output_path = f"{args.output}/assets/{name}"

            if os.path.getsize(path) != info["size"]:
                print(f"Skipping {name}: size mismatch.")
                continue

            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))
            shutil.copyfile(path, output_path)
            print(f"Copied: {name} to {output_path}")
    print("Copying complete.")
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
