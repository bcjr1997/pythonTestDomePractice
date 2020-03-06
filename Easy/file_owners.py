#Easy Problem

def group_by_owners(files):
    group_by_owners_dict = {}
    
    for file in files:
        if files[file] not in group_by_owners_dict:
            new_list = [];
            new_list.append(file);
            group_by_owners_dict[files[file]] = new_list;
        else:
            current_arr = group_by_owners_dict[files[file]];
            current_arr.append(file);
            group_by_owners_dict[files[file]] = current_arr;
            
    return group_by_owners_dict

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))