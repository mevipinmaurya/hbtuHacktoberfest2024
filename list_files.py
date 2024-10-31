import os

files = []
main_dir = "../"

def collect_paths(directory, files):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            collect_paths(filepath, files)        # call recursive récursive if folder
        elif filename.endswith(".py"):
            files.append(filepath)
    with open("list_path.txt", "w") as outfile:
        for f in files:
            outfile.write(f)
            outfile.write("\n")
        outfile.close()
        os.chdir("../")
        
collect_paths(main_dir, files)