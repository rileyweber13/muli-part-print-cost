# -*- mode: python -*-

block_cipher = None
added_files = []

a = Analysis(['../multipartprintpy/gui.py'],
             pathex=['/home/riley/Documents/code/muli-part-print-cost'],
             binaries=[],
             datas=added_files,
             hiddenimports=['requests'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='multi-part-print-cost',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
