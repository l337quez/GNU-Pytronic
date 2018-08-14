# -*- mode: python -*-
#Create by: Ronal Forero (L337)

block_cipher = None


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
sources_files = [('logo.ico', 'C:\\Users\\nombre\\Documents\\Proyecto\\Sources\\logo.ico', 'DATA')]

#licencia
sources= [('LICENSE', 'C:\\Users\\nombre\\Documents\\Proyecto\\Sources\\LICENSE', 'DATA')]

#codigo fuente
sources += [('main.py', 'C:\\Users\\nombre\\Documents\\Proyecto\\Sources\\main.py', 'DATA')]

#logo
sources += [('pytronics.png', 'E:\\Warren\\PythonScripts\\LunarLanderSharable\\pytronics.png', 'DATA')] 

             
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + sources_files,
          name='GNU PYTRONIC.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True, icon='Sources/logo.ico')
          
          
coll = COLLECT(exe,
			   Tree('C:\\Users\\nombre\\Documents\\Proyecto\\Sources','Sources'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')

