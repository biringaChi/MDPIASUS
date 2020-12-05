import sys
import os
import argparse

# Usage: java_compile.py [-h] compiler

parser = argparse.ArgumentParser(description="Compiles java files")
parser.add_argument("compiler")
args = parser.parse_args()


def compile_files(path, compiler) -> None:
    # Compiles all java files in datasource
    for (root, subdirectories, files) in os.walk(path):
        for file in files:
            if file.endswith(".java"):
                temp = os.path.join(root, file)
                os.system(compiler + " " + temp)
