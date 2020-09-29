
from beefish import decrypt
import os
import sys
import zipfile


secret_key = "Y0urS3cretK3yHere"
current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    out_zip_path = os.path.join(current_dir, "unzipped.zip")

    if len(sys.argv) != 2:
        print("Expected pak file")
        sys.exit(0)

    file_to_unpack = sys.argv[1]

    with open(file_to_unpack, "rb") as fh:
        with open(out_zip_path, "wb") as out_fh:
            decrypt(fh, out_fh, secret_key)

    zip_file = zipfile.ZipFile(out_zip_path, "r")
    zip_file.extractall(current_dir)
    zip_file.close()

    os.unlink(out_zip_path)


if __name__ == "__main__":
    main()
