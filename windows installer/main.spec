# -*- mode: python -*-
#Create by: Ronal Forero (L337)

block_cipher = None
recursos= 'C:\\Users\\Lion02\\Downloads\\GNU-Pytronic-master\\GNU-Pytronic-master\\gnu-pytronic\\Sources\\'


a = Analysis(['main.py'],
             pathex=['/home/ronal/MEGAsync/python/GNU_Pytronic'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


#icono para la venta en windows 
sources_files = [('logo.ico', 'C:\\Users\\Lion02\\Downloads\\GNU-Pytronic-master\\GNU-Pytronic-master\\gnu-pytronic\\Sources\\logo.ico', 'DATA')]

#licencia
Source= [('LICENSE', 'C:\\Users\\Lion02\\Downloads\\GNU-Pytronic-master\\GNU-Pytronic-master\\gnu-pytronic\\Sources\\LICENSE', 'DATA')]

#codigo fuente
Source += [('main.py', 'C:\\Users\\Lion02\\Downloads\\GNU-Pytronic-master\\GNU-Pytronic-master\\gnu-pytronic\\main.py', 'DATA')]

#logo
Source += [('pytronics.png', 'C:\\Users\\Lion02\\Downloads\\GNU-Pytronic-master\\GNU-Pytronic-master\\gnu-pytronic\\pytronics.png', 'DATA')] 

#banner
Source += [('banner.png', 'C:\\Users\\Lion02\\Downloads\\GNU-Pytronic-master\\GNU-Pytronic-master\\gnu-pytronic\\Sources\\banner.png', 'DATA')] 


             
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + sources_files + Source,
          name='GNU PYTRONIC.exe',
          debug=False,
          strip=None,
          upx=True,
          console=None, icon='Sources/logo.ico')
          



coll = COLLECT(exe,
               a.binaries,
               Tree(recursos,'Sources'),
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')


