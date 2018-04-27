# -*- mode: python -*-
import os
block_cipher = None
datas = []

files_str = """card_commander_cardlist.txt
card_commander_library.json.gz
card_text_corpus.mm
card_text_corpus.mm.index
card_text_dictionary.dict
card_text_lsi.index
card_text_lsi.model
card_text_lsi.model.projection
card_text_tfidf.model"""

for f in files_str.split('\n'):
    datas.append((f, '.'))
packages_to_copy = [
    'scipy',
]
datas.extend([
    ('static', 'static'),
    ('templates', 'templates'),
])
for p in packages_to_copy:
    datas.append((os.path.dirname(__import__(p).__file__), p))

hidden_imports = [
    'nltk',
    'nltk.stem',
    'wget',
    'gensim',
    'scipy',
    'scipy.optimize',
    'scipy.optimize._trlib',
    'scipy.optimize._trlib._trlib',
]
a = Analysis(
    ['app.py'],
    pathex=['/home/christopher/repos/card_codex-dev/webapp'],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='app',
    debug=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='app',
)
