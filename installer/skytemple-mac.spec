# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import shutil
import pkg_resources
from pathlib import PurePosixPath, Path

pkg_path = os.path.abspath(os.path.join('..', 'skytemple'))
site_packages = next(p for p in sys.path if 'site-packages' in p)

additional_datas = [
    (os.path.join(pkg_path, 'data'), 'skytemple/data'),
    (os.path.join(pkg_path, 'data'), 'data'),
    (os.path.join(pkg_path, '*.glade'), '.'),
    (os.path.join(pkg_path, '*.css'), '.'),
    (os.path.join(site_packages, 'skytemple_icons', 'hicolor'), 'skytemple_icons/hicolor'),
    (os.path.join(site_packages, 'skytemple_ssb_debugger', 'data'), 'skytemple_ssb_debugger/data'),
    (os.path.join(site_packages, 'skytemple_ssb_debugger', '*.glade'), 'skytemple_ssb_debugger'),
    (os.path.join(site_packages, 'skytemple_ssb_debugger', '*.lang'), 'skytemple_ssb_debugger'),
    (os.path.join(site_packages, 'skytemple_ssb_debugger', 'controller', '*.glade'), 'skytemple_ssb_debugger/controller'),
    (os.path.join(site_packages, 'skytemple_files', '_resources'), 'skytemple_files/_resources'),
    (os.path.join('.', 'armips'), 'skytemple_files/_resources'),
    (os.path.join(site_packages, 'desmume', 'frontend', 'control_ui', '*.glade'), 'desmume/frontend/control_ui'),
    (os.path.join(site_packages, "cairocffi", "VERSION"), "cairocffi"),
    (os.path.join(site_packages, "cssselect2", "VERSION"), "cssselect2"),
    (os.path.join(site_packages, "tinycss2", "VERSION"), "tinycss2"),
    (os.path.join(site_packages, "cairosvg", "VERSION"), "cairosvg"),
    (os.path.join(site_packages, "pygal", "css", "*"), 'pygal/css'),

    # Themes
    ('Mojave-dark', 'share/themes/Mojave-dark'),
    ('Mojave-light', 'share/themes/Mojave-light'),
]

additional_binaries = [
    (os.path.join(site_packages, "desmume", "libdesmume.so"), "."),
    (os.path.join(os.sep, "usr", "local", "lib", "libSDL.dylib"), "."), # Must be installed with Homebrew
    (os.path.join(os.sep, "usr", "local", "lib", "libenchant-2.dylib"), "."), # Must be installed with Homebrew
    (os.path.join(os.sep, "usr", "local", "opt", "cairo", "lib", "libcairo.2.dylib"), "."),
    (os.path.join(site_packages, "skytemple_tilequant", "aikku", "libtilequant.so"), "skytemple_tilequant/aikku"),
]

# Add all module *.glade files.
for (path, directories, filenames) in os.walk(os.path.join(pkg_path, 'module')):
    for filename in filenames:
        if filename.endswith('.glade'):
            additional_datas.append((os.path.abspath(os.path.join('..', path, filename)),
                                     f'skytemple/{str(PurePosixPath(Path(path.replace(pkg_path + "/", ""))))}'))

block_cipher = None


a = Analysis(['../skytemple/main.py'],
             pathex=[os.path.abspath(os.path.join('..', 'skytemple'))],
             binaries=additional_binaries,
             datas=additional_datas,
             hiddenimports=['pkg_resources.py2_warn', 'packaging.version', 'packaging.specifiers',
                            'packaging.requirements', 'packaging.markers', '_sysconfigdata__win32_', 'win32api'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='run_skytemple',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='skytemple')

app = BUNDLE(coll,
             name='SkyTemple.app',
             icon='skytemple.icns',
             bundle_identifier='de.parakoopa.skytemple')
