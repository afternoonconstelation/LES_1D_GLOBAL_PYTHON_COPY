import os
import shutil
from pathlib import Path
import importlib
import importlib.util



def copy_parameters_default(model_package_name:str=None):
 

    #  Get and validate PYTHONPATH only for required package.
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
    source_file = Path("Parameters_default.py").resolve()
    target_dir = Path(first_path).resolve()
    target_file = target_dir / source_file.name
    
    print("Current directory:", Path.cwd())
    print("Source:", source_file)
    print("Target:", target_file)
    
    shutil.copy2(source_file, target_file)
  

    # 5. Import Parameters_default
    importlib.invalidate_caches()

    pars = importlib.import_module(
        '.Parameters_default',
        f'{model_package_name}'
    )
    return pars