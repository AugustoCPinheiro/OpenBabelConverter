def convert_to_command(loaded, file_path, file_name) :
    smiles = ''
    
    if type(loaded)  is str:
        smiles = loaded
    else:
        smiles = loaded['smiles']
    command = "obabel -:"+'"'+smiles+'"'+ " -O " + file_path + file_name +".png"
    return command


