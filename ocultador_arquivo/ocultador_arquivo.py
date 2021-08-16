import ctypes

atributo_ocultar = 0x02

#retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)
SetFileAttributes = ctypes.windll.kernel32.SetFileAttributesW
SetFileAttributes.argtypes = ctypes.wintypes.LPWSTR, ctypes.wintypes.DWORD
SetFileAttributes.restype = ctypes.wintypes.BOOL

#FILE_ATTRIBUTE_HIDDEN = 0x02

retorno = SetFileAttributes('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')
