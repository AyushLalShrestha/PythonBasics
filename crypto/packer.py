import os
import sys
import zipfile
from beefish import encrypt

PASSWORD = "Y0urS3cretK3yHere"


def zip_dir(path):
    zipname = f"{path}.zip"
    zip = zipfile.ZipFile(zipname, "w")
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))
    zip.close()


def main():
    if len(sys.argv) != 2:
        print("Expected APPLICATION folder as input")
        sys.exit(1)

    path = sys.argv[1]
    zip_dir(path)
    zipfile = f"{path}.zip"
    pakfile = f"{path}.pak"
    with open(zipfile, "rb") as fh:
        with open(pakfile, "wb") as out_fh:
            encrypt(fh, out_fh, PASSWORD)
    if os.path.exists(zipfile):
        os.unlink(zipfile)


if __name__ == "__main__":
    main()
