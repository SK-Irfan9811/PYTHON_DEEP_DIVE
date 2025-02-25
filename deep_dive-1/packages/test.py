import sys
import types

# import package1.module_a
# import package1.package2.module_d
import package1.package2


def check_module_attributes(mod: types.ModuleType) -> None:
    print("--------------------------------------------------------------------------------------------------")
    mod_name = mod.__name__
    print(f"Module Name: {mod.__name__}")
    print(f"File: {getattr(mod, '__file__', 'N/A')}")
    print(f"Package: {getattr(mod, '__package__', 'N/A')}")
    print(f"Path: {getattr(mod, '__path__', 'N/A') if hasattr(mod, '__path__') else 'Not a package'}")
    # check if module is in sys.modules(cache)
    in_sys_modules = mod_name in sys.modules
    print(f"Present in sys.modules (cache): {in_sys_modules}")

    # Check if module is in globals()
    in_globals = mod_name in globals()
    print(f"Present in globals(): {in_globals}")
    print("--------------------------------------------------------------------------------------------------")


# check_module_attributes(package1)
check_module_attributes(package1)
print(id(sys.modules['package1.package2']), id(package1))
print("package1.package2.module_d" in sys.modules)
