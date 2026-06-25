import os

if not "SPIRV" in config.root.targets:
    config.unsupported = True

if config.spirv_tools_tests:
    config.available_features.add("spirv-tools")
    from lit.llvm import llvm_config
    llvm_config.add_tool_substitutions(
        ["spirv-dis", "spirv-val", "spirv-as", "spirv-link"]
    )

# Forward these from the shell that runs llvm-lit into every test in this tree,
# but only if they are set (empty values are skipped). Edit the list as needed.
_env_from_host = (
    "UBSAN_OPTIONS",  # e.g. export LLVM_LIT_SPIRV_EXAMPLE=1 for local runs
)
for _name in _env_from_host:
    _val = os.environ.get(_name)
    if _val:
        config.environment[_name] = _val
