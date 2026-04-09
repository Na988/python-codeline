from contextlib import contextmanager

@contextmanager
def myopenfunc(file_path, mode):
  file_pointer = open(file_path, mode)
  
  try:
    yield file_pointer
  finally:
    file_pointer.close()