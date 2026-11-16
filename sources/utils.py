import os
import shutil
from pathlib import Path
import importlib
import importlib.util

"""
1- map the file location path  
   
   upstream directory  
      |
      |---- script directory (with the script that will be executed)
                |          
        downstream directory


2- copy the file Parameters_default.py to the sam_python directory in the first path of PYTHONPATH
3- import Parameters_default.py from sam_python directory
"""


"""
Esse parte do código dependia que no PYTHONPATH apenas o pacote estivesse adicionado.
Isso poderia gerar problemas futuros, caso o usuário adicionasse mais de um diretório no PYTHONPATH.
    
pythonpath = os.environ.get("PYTHONPATH")

    if not pythonpath:
        raise EnvironmentError("PYTHONPATH is not set.")

    # 2. Extract the first directory from PYTHONPATH
    valid_paths = [p for p in pythonpath.split(os.pathsep) if p]

    if not valid_paths:
        raise EnvironmentError("PYTHONPATH contains no valid directories.")

    first_path = valid_paths[0]

"""

def copy_parameters_default(model_package_name='sam_python'):
 

    # 1. Get and validate PYTHONPATH only for required package.
    spec = importlib.util.find_spec(model_package_name)
    
    # check if the package is found even if is installed using pip install -e or using an virtual enviroment
    if spec is None or not spec.submodule_search_locations:
        pythonpath = os.environ.get("PYTHONPATH", "<não definido>")
        raise ModuleNotFoundError(
            f"Submodule '{model_package_name}' doesn't found."
            f"Verify the actual PYTHONPATH: {pythonpath}"
        )

    first_path = Path(spec.submodule_search_locations[0]).resolve()


    # 3. Define source and target files
    # solving the trouble with the relative path of the Parameters_default.py file
    
    actual_dir = Path(__file__).parent.resolve() # returns the  directory of the current script only
    source_file = actual_dir.joinpath("Parameters_default.py") # file to copy with the parameters given by the user
    
    target_dir = Path(first_path).resolve()
    target_file = target_dir / source_file.name

    #print("Current directory:", Path.cwd())
    #print("Source:", source_file)
    #print("Target:", target_file)

    shutil.copy2(source_file, target_file)
    #print("Copy completed successfully.")
    #exit()

    # 5. Import Parameters_default
    importlib.invalidate_caches()

    pars = importlib.import_module(
        '.Parameters_default',
        model_package_name
    )
    return pars

"""
if __name__=="__main__":
   print(copy_parameters_default().__file__)
"""   