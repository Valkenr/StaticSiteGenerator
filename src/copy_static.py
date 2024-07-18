import os
import shutil


def copy_dir(source, target):
    # print(f"Source: {source} | Target: {target}")
    if os.path.exists(target):
        shutil.rmtree(target)
    if os.path.exists(source):
        source_tree = os.listdir(source)
        # print(f"Tree: {source_tree}")
        for node in source_tree:
            # print(f"Processing {node}")
            if os.path.isfile(os.path.join(source, node)):
                # print(f"Copying {node}")
                if not os.path.exists(target):
                    # print(f"Making {target}")
                    os.mkdir(target)
                shutil.copy(os.path.join(source, node), os.path.join(target, node))
            else:
                # print(f"At {node}")
                # print(f"Joining {os.path.join(source, node)}")
                if not os.path.exists(target):
                    # print(f"Making {target}")
                    os.mkdir(target)
                copy_dir(os.path.join(source, node), os.path.join(target, node))

    else:
        raise ValueError("Invalid source filepath")

