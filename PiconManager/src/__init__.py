# -*- coding: utf-8 -*-

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext

PluginLanguageDomain = "PiconManager"
PluginLanguagePath = "Extensions/PiconManager/locale"


def localeInit():
	lang = language.getLanguage()[:2]
	print("[%s] set language to %s" % (PluginLanguageDomain, lang))
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)


DEFAULT_PICON_PATH = '/usr/share/enigma2/'
ALTERN_PICON_PATH = [
	'/usr/share/enigma2/',
	'/media/usb/',
	'/media/hdd/',
	'/',
	'/data/',
	'/media/mmc/',
	'/media/sdcard/',
	'/media/hdd/XPicons/',
	'/media/hdd/ZZPicons/',
	'/media/usb/XPicons/',
	'/media/usb/ZZPicons/',
	'/usr/share/enigma2/XPicons/',
	'/usr/share/enigma2/ZZPicons/',
	'user_defined'
]


def getConfigPathList():
	ChoicePath = []
	for path in ALTERN_PICON_PATH:
		if len(path) == 2:
			ChoicePath.append(path)
		else:
			ChoicePath.append((path, _(path)))

	return ChoicePath
