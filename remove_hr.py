import click
import re

def add_file_prefix(string, prefix):
    if "/".join(string.split("/")[:-1]) == "":
        return str(prefix) + string.split("/")[-1]
    return "/".join(string.split("/")[:-1]) + "/" + str(prefix) + "/".join(string.split("/")[-1:])

@click.command()
@click.argument('input', nargs=-1)
def remove_hr(input):
    for filename in input:
        with open(filename, "r") as f:
            text = f.read()
        removed_hr = re.sub('<gpxtpx:hr>(\d+\.*\d*)</gpxtpx:hr>', "" , text)
        new_filename = add_file_prefix(filename, "removed_hr_")
        with open(new_filename, "w") as f:
            f.write(removed_hr)
        print("Processed: " + filename)

if __name__ == '__main__':
    remove_hr()