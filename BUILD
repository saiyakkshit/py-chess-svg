load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_binary(
    name = "main",
    srcs = glob(["*.py"]),
)

py_test(
    name = "test",
    srcs = glob(["*_test.py"]),
    deps = [":main"],
)
