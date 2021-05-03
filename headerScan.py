import os


def scan_header (work_space_path):
    ''' Taking in the Abs Path to a work_space
    Return a list of abs path to header files in that work_space'''
    headerList = []
    for root, dirs, files in os.walk(work_space_path):
        for file in files:
            if file.endswith(".h"):
                headerList.append(os.path.join(root,file))
    return headerList