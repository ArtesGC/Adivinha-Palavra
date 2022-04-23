# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['./ap/__init__.py'],
             pathex=['./ap/'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib', 'tkinter', 'PySide2', 'pygame', 'PyQt5'],
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
          name='adivinhapalavra',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon="./ap/icons/favicon-256x256.ico",
          disable_windowed_traceback=False,
          target_arch=['Linux-5.13.0-35-generic-x86_64', 'Win-x86_64'],
          codesign_identity='Nurul-GC',
          entitlements_file=None )
